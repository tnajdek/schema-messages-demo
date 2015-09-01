# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='demo',
  serialized_pb=_b('\n\x0emessages.proto\x12\x04\x64\x65mo\"%\n\x0eRequestMessage\x12\x13\n\x0bpixel_count\x18\x01 \x02(\r\"D\n\x0b\x44\x61taMessage\x12\t\n\x01x\x18\x01 \x02(\r\x12\t\n\x01y\x18\x02 \x02(\r\x12\t\n\x01r\x18\x03 \x02(\r\x12\t\n\x01g\x18\x04 \x02(\r\x12\t\n\x01\x62\x18\x05 \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REQUESTMESSAGE = _descriptor.Descriptor(
  name='RequestMessage',
  full_name='demo.RequestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pixel_count', full_name='demo.RequestMessage.pixel_count', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=61,
)


_DATAMESSAGE = _descriptor.Descriptor(
  name='DataMessage',
  full_name='demo.DataMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='demo.DataMessage.x', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='demo.DataMessage.y', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='r', full_name='demo.DataMessage.r', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='g', full_name='demo.DataMessage.g', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b', full_name='demo.DataMessage.b', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=131,
)

DESCRIPTOR.message_types_by_name['RequestMessage'] = _REQUESTMESSAGE
DESCRIPTOR.message_types_by_name['DataMessage'] = _DATAMESSAGE

RequestMessage = _reflection.GeneratedProtocolMessageType('RequestMessage', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTMESSAGE,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:demo.RequestMessage)
  ))
_sym_db.RegisterMessage(RequestMessage)

DataMessage = _reflection.GeneratedProtocolMessageType('DataMessage', (_message.Message,), dict(
  DESCRIPTOR = _DATAMESSAGE,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:demo.DataMessage)
  ))
_sym_db.RegisterMessage(DataMessage)


# @@protoc_insertion_point(module_scope)
