# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: storageagent.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='storageagent.proto',
  package='storageagent',
  syntax='proto3',
  serialized_options=_b('\n\024com.ibm.storageagentB\021StorageAgentProtoP\001\242\002\003HLW'),
  serialized_pb=_b('\n\x12storageagent.proto\x12\x0cstorageagent\"r\n\x04Host\x12\x12\n\nidentifier\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\x12\r\n\x05\x61rray\x18\x05 \x01(\t\x12\x0c\n\x04iqns\x18\x06 \x03(\t\x12\r\n\x05wwpns\x18\x07 \x03(\t\"+\n\x0bIscsiTarget\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0b\n\x03iqn\x18\x02 \x01(\t\"\xbb\x01\n\x11\x43reateHostRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0c\n\x04iqns\x18\x03 \x03(\t\x12\r\n\x05wwpns\x18\x04 \x03(\t\x12=\n\x07secrets\x18\x05 \x03(\x0b\x32,.storageagent.CreateHostRequest.SecretsEntry\x1a.\n\x0cSecretsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"3\n\x0f\x43reateHostReply\x12 \n\x04host\x18\x01 \x01(\x0b\x32\x12.storageagent.Host\"\xa4\x01\n\x11\x44\x65leteHostRequest\x12\x12\n\nidentifier\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12=\n\x07secrets\x18\x03 \x03(\x0b\x32,.storageagent.DeleteHostRequest.SecretsEntry\x1a.\n\x0cSecretsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x11\n\x0f\x44\x65leteHostReply\"\xa2\x01\n\x10ListHostsRequest\x12\x12\n\nidentifier\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12<\n\x07secrets\x18\x03 \x03(\x0b\x32+.storageagent.ListHostsRequest.SecretsEntry\x1a.\n\x0cSecretsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"3\n\x0eListHostsReply\x12!\n\x05hosts\x18\x01 \x03(\x0b\x32\x12.storageagent.Host\"\x8e\x01\n\x17ListIscsiTargetsRequest\x12\x43\n\x07secrets\x18\x01 \x03(\x0b\x32\x32.storageagent.ListIscsiTargetsRequest.SecretsEntry\x1a.\n\x0cSecretsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"C\n\x15ListIscsiTargetsReply\x12*\n\x07targets\x18\x01 \x03(\x0b\x32\x19.storageagent.IscsiTarget2\xdd\x02\n\x0cStorageAgent\x12N\n\nCreateHost\x12\x1f.storageagent.CreateHostRequest\x1a\x1d.storageagent.CreateHostReply\"\x00\x12N\n\nDeleteHost\x12\x1f.storageagent.DeleteHostRequest\x1a\x1d.storageagent.DeleteHostReply\"\x00\x12K\n\tListHosts\x12\x1e.storageagent.ListHostsRequest\x1a\x1c.storageagent.ListHostsReply\"\x00\x12`\n\x10ListIscsiTargets\x12%.storageagent.ListIscsiTargetsRequest\x1a#.storageagent.ListIscsiTargetsReply\"\x00\x42\x31\n\x14\x63om.ibm.storageagentB\x11StorageAgentProtoP\x01\xa2\x02\x03HLWb\x06proto3')
)




_HOST = _descriptor.Descriptor(
  name='Host',
  full_name='storageagent.Host',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='storageagent.Host.identifier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='storageagent.Host.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='storageagent.Host.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='storageagent.Host.status', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='array', full_name='storageagent.Host.array', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iqns', full_name='storageagent.Host.iqns', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wwpns', full_name='storageagent.Host.wwpns', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=150,
)


_ISCSITARGET = _descriptor.Descriptor(
  name='IscsiTarget',
  full_name='storageagent.IscsiTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='storageagent.IscsiTarget.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iqn', full_name='storageagent.IscsiTarget.iqn', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=195,
)


_CREATEHOSTREQUEST_SECRETSENTRY = _descriptor.Descriptor(
  name='SecretsEntry',
  full_name='storageagent.CreateHostRequest.SecretsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='storageagent.CreateHostRequest.SecretsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='storageagent.CreateHostRequest.SecretsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=339,
  serialized_end=385,
)

_CREATEHOSTREQUEST = _descriptor.Descriptor(
  name='CreateHostRequest',
  full_name='storageagent.CreateHostRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='storageagent.CreateHostRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='storageagent.CreateHostRequest.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iqns', full_name='storageagent.CreateHostRequest.iqns', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wwpns', full_name='storageagent.CreateHostRequest.wwpns', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secrets', full_name='storageagent.CreateHostRequest.secrets', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATEHOSTREQUEST_SECRETSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=385,
)


_CREATEHOSTREPLY = _descriptor.Descriptor(
  name='CreateHostReply',
  full_name='storageagent.CreateHostReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='storageagent.CreateHostReply.host', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=387,
  serialized_end=438,
)


_DELETEHOSTREQUEST_SECRETSENTRY = _descriptor.Descriptor(
  name='SecretsEntry',
  full_name='storageagent.DeleteHostRequest.SecretsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='storageagent.DeleteHostRequest.SecretsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='storageagent.DeleteHostRequest.SecretsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=339,
  serialized_end=385,
)

_DELETEHOSTREQUEST = _descriptor.Descriptor(
  name='DeleteHostRequest',
  full_name='storageagent.DeleteHostRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='storageagent.DeleteHostRequest.identifier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='storageagent.DeleteHostRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secrets', full_name='storageagent.DeleteHostRequest.secrets', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DELETEHOSTREQUEST_SECRETSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=441,
  serialized_end=605,
)


_DELETEHOSTREPLY = _descriptor.Descriptor(
  name='DeleteHostReply',
  full_name='storageagent.DeleteHostReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=607,
  serialized_end=624,
)


_LISTHOSTSREQUEST_SECRETSENTRY = _descriptor.Descriptor(
  name='SecretsEntry',
  full_name='storageagent.ListHostsRequest.SecretsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='storageagent.ListHostsRequest.SecretsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='storageagent.ListHostsRequest.SecretsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=339,
  serialized_end=385,
)

_LISTHOSTSREQUEST = _descriptor.Descriptor(
  name='ListHostsRequest',
  full_name='storageagent.ListHostsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='storageagent.ListHostsRequest.identifier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='storageagent.ListHostsRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secrets', full_name='storageagent.ListHostsRequest.secrets', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTHOSTSREQUEST_SECRETSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=627,
  serialized_end=789,
)


_LISTHOSTSREPLY = _descriptor.Descriptor(
  name='ListHostsReply',
  full_name='storageagent.ListHostsReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hosts', full_name='storageagent.ListHostsReply.hosts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=791,
  serialized_end=842,
)


_LISTISCSITARGETSREQUEST_SECRETSENTRY = _descriptor.Descriptor(
  name='SecretsEntry',
  full_name='storageagent.ListIscsiTargetsRequest.SecretsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='storageagent.ListIscsiTargetsRequest.SecretsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='storageagent.ListIscsiTargetsRequest.SecretsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=339,
  serialized_end=385,
)

_LISTISCSITARGETSREQUEST = _descriptor.Descriptor(
  name='ListIscsiTargetsRequest',
  full_name='storageagent.ListIscsiTargetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='secrets', full_name='storageagent.ListIscsiTargetsRequest.secrets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTISCSITARGETSREQUEST_SECRETSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=845,
  serialized_end=987,
)


_LISTISCSITARGETSREPLY = _descriptor.Descriptor(
  name='ListIscsiTargetsReply',
  full_name='storageagent.ListIscsiTargetsReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targets', full_name='storageagent.ListIscsiTargetsReply.targets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=989,
  serialized_end=1056,
)

_CREATEHOSTREQUEST_SECRETSENTRY.containing_type = _CREATEHOSTREQUEST
_CREATEHOSTREQUEST.fields_by_name['secrets'].message_type = _CREATEHOSTREQUEST_SECRETSENTRY
_CREATEHOSTREPLY.fields_by_name['host'].message_type = _HOST
_DELETEHOSTREQUEST_SECRETSENTRY.containing_type = _DELETEHOSTREQUEST
_DELETEHOSTREQUEST.fields_by_name['secrets'].message_type = _DELETEHOSTREQUEST_SECRETSENTRY
_LISTHOSTSREQUEST_SECRETSENTRY.containing_type = _LISTHOSTSREQUEST
_LISTHOSTSREQUEST.fields_by_name['secrets'].message_type = _LISTHOSTSREQUEST_SECRETSENTRY
_LISTHOSTSREPLY.fields_by_name['hosts'].message_type = _HOST
_LISTISCSITARGETSREQUEST_SECRETSENTRY.containing_type = _LISTISCSITARGETSREQUEST
_LISTISCSITARGETSREQUEST.fields_by_name['secrets'].message_type = _LISTISCSITARGETSREQUEST_SECRETSENTRY
_LISTISCSITARGETSREPLY.fields_by_name['targets'].message_type = _ISCSITARGET
DESCRIPTOR.message_types_by_name['Host'] = _HOST
DESCRIPTOR.message_types_by_name['IscsiTarget'] = _ISCSITARGET
DESCRIPTOR.message_types_by_name['CreateHostRequest'] = _CREATEHOSTREQUEST
DESCRIPTOR.message_types_by_name['CreateHostReply'] = _CREATEHOSTREPLY
DESCRIPTOR.message_types_by_name['DeleteHostRequest'] = _DELETEHOSTREQUEST
DESCRIPTOR.message_types_by_name['DeleteHostReply'] = _DELETEHOSTREPLY
DESCRIPTOR.message_types_by_name['ListHostsRequest'] = _LISTHOSTSREQUEST
DESCRIPTOR.message_types_by_name['ListHostsReply'] = _LISTHOSTSREPLY
DESCRIPTOR.message_types_by_name['ListIscsiTargetsRequest'] = _LISTISCSITARGETSREQUEST
DESCRIPTOR.message_types_by_name['ListIscsiTargetsReply'] = _LISTISCSITARGETSREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Host = _reflection.GeneratedProtocolMessageType('Host', (_message.Message,), {
  'DESCRIPTOR' : _HOST,
  '__module__' : 'storageagent_pb2'
  # @@protoc_insertion_point(class_scope:storageagent.Host)
  })
_sym_db.RegisterMessage(Host)

IscsiTarget = _reflection.GeneratedProtocolMessageType('IscsiTarget', (_message.Message,), {
  'DESCRIPTOR' : _ISCSITARGET,
  '__module__' : 'storageagent_pb2'
  # @@protoc_insertion_point(class_scope:storageagent.IscsiTarget)
  })
_sym_db.RegisterMessage(IscsiTarget)

CreateHostRequest = _reflection.GeneratedProtocolMessageType('CreateHostRequest', (_message.Message,), {

  'SecretsEntry' : _reflection.GeneratedProtocolMessageType('SecretsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CREATEHOSTREQUEST_SECRETSENTRY,
    '__module__' : 'storageagent_pb2'
    # @@protoc_insertion_point(class_scope:storageagent.CreateHostRequest.SecretsEntry)
    })
  ,
  'DESCRIPTOR' : _CREATEHOSTREQUEST,
  '__module__' : 'storageagent_pb2'
  # @@protoc_insertion_point(class_scope:storageagent.CreateHostRequest)
  })
_sym_db.RegisterMessage(CreateHostRequest)
_sym_db.RegisterMessage(CreateHostRequest.SecretsEntry)

CreateHostReply = _reflection.GeneratedProtocolMessageType('CreateHostReply', (_message.Message,), {
  'DESCRIPTOR' : _CREATEHOSTREPLY,
  '__module__' : 'storageagent_pb2'
  # @@protoc_insertion_point(class_scope:storageagent.CreateHostReply)
  })
_sym_db.RegisterMessage(CreateHostReply)

DeleteHostRequest = _reflection.GeneratedProtocolMessageType('DeleteHostRequest', (_message.Message,), {

  'SecretsEntry' : _reflection.GeneratedProtocolMessageType('SecretsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DELETEHOSTREQUEST_SECRETSENTRY,
    '__module__' : 'storageagent_pb2'
    # @@protoc_insertion_point(class_scope:storageagent.DeleteHostRequest.SecretsEntry)
    })
  ,
  'DESCRIPTOR' : _DELETEHOSTREQUEST,
  '__module__' : 'storageagent_pb2'
  # @@protoc_insertion_point(class_scope:storageagent.DeleteHostRequest)
  })
_sym_db.RegisterMessage(DeleteHostRequest)
_sym_db.RegisterMessage(DeleteHostRequest.SecretsEntry)

DeleteHostReply = _reflection.GeneratedProtocolMessageType('DeleteHostReply', (_message.Message,), {
  'DESCRIPTOR' : _DELETEHOSTREPLY,
  '__module__' : 'storageagent_pb2'
  # @@protoc_insertion_point(class_scope:storageagent.DeleteHostReply)
  })
_sym_db.RegisterMessage(DeleteHostReply)

ListHostsRequest = _reflection.GeneratedProtocolMessageType('ListHostsRequest', (_message.Message,), {

  'SecretsEntry' : _reflection.GeneratedProtocolMessageType('SecretsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LISTHOSTSREQUEST_SECRETSENTRY,
    '__module__' : 'storageagent_pb2'
    # @@protoc_insertion_point(class_scope:storageagent.ListHostsRequest.SecretsEntry)
    })
  ,
  'DESCRIPTOR' : _LISTHOSTSREQUEST,
  '__module__' : 'storageagent_pb2'
  # @@protoc_insertion_point(class_scope:storageagent.ListHostsRequest)
  })
_sym_db.RegisterMessage(ListHostsRequest)
_sym_db.RegisterMessage(ListHostsRequest.SecretsEntry)

ListHostsReply = _reflection.GeneratedProtocolMessageType('ListHostsReply', (_message.Message,), {
  'DESCRIPTOR' : _LISTHOSTSREPLY,
  '__module__' : 'storageagent_pb2'
  # @@protoc_insertion_point(class_scope:storageagent.ListHostsReply)
  })
_sym_db.RegisterMessage(ListHostsReply)

ListIscsiTargetsRequest = _reflection.GeneratedProtocolMessageType('ListIscsiTargetsRequest', (_message.Message,), {

  'SecretsEntry' : _reflection.GeneratedProtocolMessageType('SecretsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LISTISCSITARGETSREQUEST_SECRETSENTRY,
    '__module__' : 'storageagent_pb2'
    # @@protoc_insertion_point(class_scope:storageagent.ListIscsiTargetsRequest.SecretsEntry)
    })
  ,
  'DESCRIPTOR' : _LISTISCSITARGETSREQUEST,
  '__module__' : 'storageagent_pb2'
  # @@protoc_insertion_point(class_scope:storageagent.ListIscsiTargetsRequest)
  })
_sym_db.RegisterMessage(ListIscsiTargetsRequest)
_sym_db.RegisterMessage(ListIscsiTargetsRequest.SecretsEntry)

ListIscsiTargetsReply = _reflection.GeneratedProtocolMessageType('ListIscsiTargetsReply', (_message.Message,), {
  'DESCRIPTOR' : _LISTISCSITARGETSREPLY,
  '__module__' : 'storageagent_pb2'
  # @@protoc_insertion_point(class_scope:storageagent.ListIscsiTargetsReply)
  })
_sym_db.RegisterMessage(ListIscsiTargetsReply)


DESCRIPTOR._options = None
_CREATEHOSTREQUEST_SECRETSENTRY._options = None
_DELETEHOSTREQUEST_SECRETSENTRY._options = None
_LISTHOSTSREQUEST_SECRETSENTRY._options = None
_LISTISCSITARGETSREQUEST_SECRETSENTRY._options = None

_STORAGEAGENT = _descriptor.ServiceDescriptor(
  name='StorageAgent',
  full_name='storageagent.StorageAgent',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1059,
  serialized_end=1408,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateHost',
    full_name='storageagent.StorageAgent.CreateHost',
    index=0,
    containing_service=None,
    input_type=_CREATEHOSTREQUEST,
    output_type=_CREATEHOSTREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteHost',
    full_name='storageagent.StorageAgent.DeleteHost',
    index=1,
    containing_service=None,
    input_type=_DELETEHOSTREQUEST,
    output_type=_DELETEHOSTREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListHosts',
    full_name='storageagent.StorageAgent.ListHosts',
    index=2,
    containing_service=None,
    input_type=_LISTHOSTSREQUEST,
    output_type=_LISTHOSTSREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListIscsiTargets',
    full_name='storageagent.StorageAgent.ListIscsiTargets',
    index=3,
    containing_service=None,
    input_type=_LISTISCSITARGETSREQUEST,
    output_type=_LISTISCSITARGETSREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STORAGEAGENT)

DESCRIPTOR.services_by_name['StorageAgent'] = _STORAGEAGENT

# @@protoc_insertion_point(module_scope)
