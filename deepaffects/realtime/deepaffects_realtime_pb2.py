# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: deepaffects-realtime.proto
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
import sys
_b = sys.version_info[0] < 3 and (
    lambda x: x) or (lambda x: x.encode('latin1'))
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='deepaffects-realtime.proto',
    package='deepaffectsrealtime',
    syntax='proto3',
    serialized_pb=_b('\n\x1a\x64\x65\x65paffects-realtime.proto\x12\x13\x64\x65\x65paffectsrealtime\"\xb0\x01\n\x0cSegmentChunk\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x10\n\x08\x65ncoding\x18\x03 \x01(\t\x12\x14\n\x0clanguageCode\x18\x04 \x01(\t\x12\x12\n\nsampleRate\x18\x05 \x01(\x05\x12\x0f\n\x07userIds\x18\x06 \x03(\t\x12\x15\n\rsegmentOffset\x18\x07 \x01(\x02\x12\x10\n\x08\x64uration\x18\x08 \x01(\x02\x12\r\n\x05\x45rror\x18\t \x01(\t\"W\n\x0eSegmentSpeaker\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06userId\x18\x02 \x01(\t\x12\r\n\x05start\x18\x03 \x01(\x02\x12\x0b\n\x03\x65nd\x18\x04 \x01(\x02\x12\r\n\x05\x45rror\x18\x05 \x01(\t\"X\n\x0eSegmentEmotion\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05start\x18\x02 \x01(\x02\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x02\x12\x0f\n\x07\x65motion\x18\x04 \x01(\t\x12\r\n\x05\x45rror\x18\x05 \x01(\t2\xd7\x01\n\x13\x44\x65\x65pAffectsRealtime\x12_\n\x0fIdentifySpeaker\x12!.deepaffectsrealtime.SegmentChunk\x1a#.deepaffectsrealtime.SegmentSpeaker\"\x00(\x01\x30\x01\x12_\n\x0fIdentifyEmotion\x12!.deepaffectsrealtime.SegmentChunk\x1a#.deepaffectsrealtime.SegmentEmotion\"\x00(\x01\x30\x01\x42;\n\x1cio.grpc.examples.deepaffectsB\x13\x44\x65\x65paffectsRealtimeP\x01\xa2\x02\x03\x44RIb\x06proto3')
)


_SEGMENTCHUNK = _descriptor.Descriptor(
    name='SegmentChunk',
    full_name='deepaffectsrealtime.SegmentChunk',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='id', full_name='deepaffectsrealtime.SegmentChunk.id', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='content', full_name='deepaffectsrealtime.SegmentChunk.content', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='encoding', full_name='deepaffectsrealtime.SegmentChunk.encoding', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='languageCode', full_name='deepaffectsrealtime.SegmentChunk.languageCode', index=3,
            number=4, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='sampleRate', full_name='deepaffectsrealtime.SegmentChunk.sampleRate', index=4,
            number=5, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='userIds', full_name='deepaffectsrealtime.SegmentChunk.userIds', index=5,
            number=6, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='segmentOffset', full_name='deepaffectsrealtime.SegmentChunk.segmentOffset', index=6,
            number=7, type=2, cpp_type=6, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='duration', full_name='deepaffectsrealtime.SegmentChunk.duration', index=7,
            number=8, type=2, cpp_type=6, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='Error', full_name='deepaffectsrealtime.SegmentChunk.Error', index=8,
            number=9, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=52,
    serialized_end=228,
)


_SEGMENTSPEAKER = _descriptor.Descriptor(
    name='SegmentSpeaker',
    full_name='deepaffectsrealtime.SegmentSpeaker',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='id', full_name='deepaffectsrealtime.SegmentSpeaker.id', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='userId', full_name='deepaffectsrealtime.SegmentSpeaker.userId', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='start', full_name='deepaffectsrealtime.SegmentSpeaker.start', index=2,
            number=3, type=2, cpp_type=6, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='end', full_name='deepaffectsrealtime.SegmentSpeaker.end', index=3,
            number=4, type=2, cpp_type=6, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='Error', full_name='deepaffectsrealtime.SegmentSpeaker.Error', index=4,
            number=5, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=230,
    serialized_end=317,
)


_SEGMENTEMOTION = _descriptor.Descriptor(
    name='SegmentEmotion',
    full_name='deepaffectsrealtime.SegmentEmotion',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='id', full_name='deepaffectsrealtime.SegmentEmotion.id', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='start', full_name='deepaffectsrealtime.SegmentEmotion.start', index=1,
            number=2, type=2, cpp_type=6, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='end', full_name='deepaffectsrealtime.SegmentEmotion.end', index=2,
            number=3, type=2, cpp_type=6, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='emotion', full_name='deepaffectsrealtime.SegmentEmotion.emotion', index=3,
            number=4, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='Error', full_name='deepaffectsrealtime.SegmentEmotion.Error', index=4,
            number=5, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=319,
    serialized_end=407,
)

DESCRIPTOR.message_types_by_name['SegmentChunk'] = _SEGMENTCHUNK
DESCRIPTOR.message_types_by_name['SegmentSpeaker'] = _SEGMENTSPEAKER
DESCRIPTOR.message_types_by_name['SegmentEmotion'] = _SEGMENTEMOTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SegmentChunk = _reflection.GeneratedProtocolMessageType('SegmentChunk', (_message.Message,), dict(
    DESCRIPTOR=_SEGMENTCHUNK,
    __module__='deepaffects_realtime_pb2'
    # @@protoc_insertion_point(class_scope:deepaffectsrealtime.SegmentChunk)
))
_sym_db.RegisterMessage(SegmentChunk)

SegmentSpeaker = _reflection.GeneratedProtocolMessageType('SegmentSpeaker', (_message.Message,), dict(
    DESCRIPTOR=_SEGMENTSPEAKER,
    __module__='deepaffects_realtime_pb2'
    # @@protoc_insertion_point(class_scope:deepaffectsrealtime.SegmentSpeaker)
))
_sym_db.RegisterMessage(SegmentSpeaker)

SegmentEmotion = _reflection.GeneratedProtocolMessageType('SegmentEmotion', (_message.Message,), dict(
    DESCRIPTOR=_SEGMENTEMOTION,
    __module__='deepaffects_realtime_pb2'
    # @@protoc_insertion_point(class_scope:deepaffectsrealtime.SegmentEmotion)
))
_sym_db.RegisterMessage(SegmentEmotion)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b(
    '\n\034io.grpc.examples.deepaffectsB\023DeepaffectsRealtimeP\001\242\002\003DRI'))

_DEEPAFFECTSREALTIME = _descriptor.ServiceDescriptor(
    name='DeepAffectsRealtime',
    full_name='deepaffectsrealtime.DeepAffectsRealtime',
    file=DESCRIPTOR,
    index=0,
    options=None,
    serialized_start=410,
    serialized_end=625,
    methods=[
        _descriptor.MethodDescriptor(
            name='IdentifySpeaker',
            full_name='deepaffectsrealtime.DeepAffectsRealtime.IdentifySpeaker',
            index=0,
            containing_service=None,
            input_type=_SEGMENTCHUNK,
            output_type=_SEGMENTSPEAKER,
            options=None,
        ),
        _descriptor.MethodDescriptor(
            name='IdentifyEmotion',
            full_name='deepaffectsrealtime.DeepAffectsRealtime.IdentifyEmotion',
            index=1,
            containing_service=None,
            input_type=_SEGMENTCHUNK,
            output_type=_SEGMENTEMOTION,
            options=None,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_DEEPAFFECTSREALTIME)

DESCRIPTOR.services_by_name['DeepAffectsRealtime'] = _DEEPAFFECTSREALTIME

# @@protoc_insertion_point(module_scope)