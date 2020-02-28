from hashlib import sha1
import base58
from packaging.version import parse
from pyds8k import exceptions
from controller.common.csi_logger import get_stdout_logger
from controller.array_action.array_mediator_interface import ArrayMediator
from controller.array_action.utils import classproperty
from controller.array_action.ds8k_rest_client import RESTClient
import controller.array_action.errors as array_errors
from controller.array_action import config
from controller.array_action.array_action_types import Volume


logger = get_stdout_logger()


# system
SYSTEM_ID = 'id'   # 2107-{sn}
SYSTEM_WWNN = 'wwnn'
SYSTEM_CODE_LEVEL = 'bundle'
SYSTEM_NAME = 'name'
SYSTEM_MODEL = 'MTM'  # 2421-961, Machine type and Model

# volume
VOLUME_ID = 'id'
VOLUME_NAME = 'name'
VOLUME_POOL_ID = 'pool'
VOLUME_LOGICAL_CAP = 'cap'
VOLUME_PHYSICAL_CAP = 'real_cap'
VOLUME_USED_CAP = 'capalloc'
VOLUME_STORAGE_ALLOCATION_METHOD = 'tp'  # none|tse|ese

# response keys
RES_STATUS = 'status'
RES_CODE = 'code'
RES_MSG = 'message'

# response values
RES_SUCCESS_STAUTS = ('ok', 'successful', )

# response error codes
INVALID_CREDENTIALS = 'BE7A002D'


def parse_version(bundle):
    """
    Parse ds8k version number from bundle.

    rule is:
    87.51.34.0 => 7.5.1
    87.50.21.1 => 7.5.0
    88.0.151.0 => 8.0.0
    """

    v1, v2, _ = bundle.split('.', 2)
    v2 = '{0:0{1}}'.format(int(v2), 2)

    return '.'.join([v1[-1], v2[0], v2[1]])


def get_volume_id_from_scsi_identifier(scsi_id):
    return scsi_id[-4:]


# shorten volume name to 16 characters if it is too long.
def shorten_volume_name(name):
    if len(name) <= 16:
        return name
    return base58.b58encode(sha1(name.encode()).digest()).decode()[-16:]


class DS8KArrayMediator(ArrayMediator):
    SUPPORTED_FROM_VERSION = '7.5.1'

    @classproperty
    def array_type(self):
        return 'DS8K'

    @classproperty
    def port(self):
        return 8452

    @classproperty
    def max_vol_name_length(self):
        return 63

    @classproperty
    def max_connections(self):
        # max for rest api is 128.
        return 50

    @classproperty
    def minimal_volume_size_in_bytes(self):
        return 512  # 1 block, 512 bytes

    @classproperty
    def max_lun_retries(self):
        return 10

    def __init__(self, user, password, endpoint):
        self.user = user
        self.service_address = \
            endpoint[0] if isinstance(endpoint, list) else endpoint
        self.password = password

        self._connect()

    def _connect(self):
        try:
            self.client = RESTClient(service_address=self.service_address,
                                     user=self.user,
                                     password=self.password,
                                     )

            self.system_info = self.get_system_info()

            if parse(self.version) < parse(self.SUPPORTED_FROM_VERSION):
                raise array_errors.UnsupportedStorageVersionError(
                    self.version, self.SUPPORTED_FROM_VERSION
                )
        except exceptions.ClientError as e:
            # BE7A002D=Authentication has failed because the user name and
            # password combination that you have entered is not valid.
            if INVALID_CREDENTIALS in str(e.message).upper():
                raise array_errors.CredentialsError(self.service_address)
            else:
                raise ConnectionError()
        except exceptions.ClientException as e:
            logger.error(
                'Failed to connect to DS8K array {}, reason is {}'.format(
                    self.identifier,
                    e.details
                    )
                )
            raise ConnectionError()

    def disconnect(self):
        pass

    def get_system_info(self):
        return self.client.get_system()[0]

    @property
    def identifier(self):
        return self.system_info[SYSTEM_ID]

    @property
    def name(self):
        return self.system_info.get(SYSTEM_NAME, None) \
            or self.identifier

    @property
    def version(self):
        return parse_version(self.system_info[SYSTEM_CODE_LEVEL])

    @property
    def wwnn(self):
        return self.system_info[SYSTEM_WWNN]

    def _generate_volume_scsi_identifier(self, volume_id):
        return '6{}000000000000{}'.format(self.wwnn[1:], volume_id)

    def _generate_volume_response(self, res):
        return Volume(
            vol_size_bytes=int(res[VOLUME_LOGICAL_CAP]),
            vol_id=self._generate_volume_scsi_identifier(res[VOLUME_ID]),
            vol_name=res[VOLUME_NAME],
            array_address=self.service_address,
            pool_name=res[VOLUME_POOL_ID],
            array_type=self.array_type
        )

    def get_se_capability_value(self, capabilities):
        capability = capabilities.get(config.CAPABILITIES_SPACEEFFICIENCY)
        if capability:
            capability = capability.lower()
            if capability == config.CAPABILITY_THIN:
                return "ese"
        return "none"

    def create_volume(self, name, size_in_bytes, capabilities, pool_id):
        logger.info(
            "Creating volume with name: {}, size: {}, in pool: {}, "
            "with capabilities: {}".format(
                name, size_in_bytes, pool_id,
                capabilities
            )
        )
        try:
            cli_kwargs = {}
            cli_kwargs.update({
                'name': shorten_volume_name(name),
                'capacity_in_bytes': size_in_bytes,
                'pool_id': pool_id,
                'tp': self.get_se_capability_value(capabilities),

            })
            logger.debug(
                "Start to create volume with parameters: {}".format(cli_kwargs)
            )
            res = self.client.create_volume(**cli_kwargs)[0]
            if 'id' in res:
                logger.info("finished creating volume {}".format(name))
                return self._generate_volume_response(res)
            elif RES_STATUS in res and \
                    res[RES_STATUS].lower() not in RES_SUCCESS_STAUTS:
                msg = 'Failed to create volume {} on array {}. {}'.format(
                    name,
                    self.identifier,
                    res.get(RES_MSG, '')
                    )
                logger.error(msg)
                raise array_errors.VolumeCreationError(name)
            else:
                logger.error('Failed to create volume {} on array {}.'.format(
                    name,
                    self.identifier,
                    )
                )
                raise array_errors.VolumeCreationError(name)
        except exceptions.ClientException as ex:
            logger.error(
                "Failed to create volume {} on array {}, reason is: {}".format(
                    name,
                    self.identifier,
                    ex.details
                )
            )
            raise array_errors.VolumeCreationError(name)

    def delete_volume(self, volume_id):
        logger.info("Deleting volume {}".format(volume_id))
        try:
            self.client.delete_volume(
                volume_id=get_volume_id_from_scsi_identifier(volume_id)
            )
            logger.info("Finished deleting volume {}".format(volume_id))
        except exceptions.NotFound:
            raise array_errors.VolumeNotFoundError(volume_id)
        except exceptions.ClientException as ex:
            logger.error(
                "Failed to delete volume {} on array {}, reason is: {}".format(
                    volume_id,
                    self.identifier,
                    ex.details
                )
            )
            raise array_errors.VolumeDeletionError(volume_id)

    def get_volume(self, name, volume_context=None):
        logger.debug("Getting volume {}".format(name))
        if not volume_context:
            logger.error(
                "volume_context is not specified, can not get volumes from storage."
            )
            raise array_errors.VolumeNotFoundError(name)

        volume_candidates = []
        if config.CONTEXT_POOL in volume_context:
            volume_candidates = self.client.list_extentpool_volumes(
                volume_context[config.CONTEXT_POOL]
            )
        for vol in volume_candidates:
            if vol[VOLUME_NAME] == shorten_volume_name(name):
                logger.debug("Found volume: {}".format(vol))
                return self._generate_volume_response(vol)

        raise array_errors.VolumeNotFoundError(name)

    def get_volume_mappings(self, volume_id):
        # TODO: CSI-1197
        pass

    def map_volume(self, volume_id, host_name):
        # TODO: CSI-1198
        pass

    def unmap_volume(self, volume_id, host_name):
        # TODO: CSI-1199
        pass

    def get_array_iqns(self):
        return []

    def get_array_fc_wwns(self, host_name=None):
        # TODO: CSI-1200
        pass

    def get_host_by_host_identifiers(self, initiators):
        # TODO: CSI-1201
        pass

    def validate_supported_capabilities(self, capabilities):
        logger.debug("Validating capabilities: {0}".format(capabilities))

        # Currently, we only support one capability "SpaceEfficiency"
        # The value should be: "thin"
        if (capabilities and capabilities.get(
                config.CAPABILITIES_SPACEEFFICIENCY).lower() not in
                [config.CAPABILITY_THIN, ]):
            logger.error("capabilities is not supported.")
            raise array_errors.StorageClassCapabilityNotSupported(
                capabilities)

        logger.debug("Finished validating capabilities.")
