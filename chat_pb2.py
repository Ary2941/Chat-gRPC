# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nchat.proto\x1a\x1bgoogle/protobuf/empty.proto\"1\n\x0eMessageRequest\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"2\n\x0fMessageResponse\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t2\x81\x01\n\x0b\x43hatService\x12\x32\n\x0bSendMessage\x12\x0f.MessageRequest\x1a\x10.MessageResponse\"\x00\x12>\n\x0eReceiveMessage\x12\x16.google.protobuf.Empty\x1a\x10.MessageResponse\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chat_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MESSAGEREQUEST']._serialized_start=43
  _globals['_MESSAGEREQUEST']._serialized_end=92
  _globals['_MESSAGERESPONSE']._serialized_start=94
  _globals['_MESSAGERESPONSE']._serialized_end=144
  _globals['_CHATSERVICE']._serialized_start=147
  _globals['_CHATSERVICE']._serialized_end=276
# @@protoc_insertion_point(module_scope)