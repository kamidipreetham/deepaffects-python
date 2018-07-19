# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import deepaffects.realtime.deepaffects_realtime_pb2 as deepaffects__realtime__pb2


class DeepAffectsRealtimeStub(object):
    """Interface exported by the server.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.IdentifySpeaker = channel.stream_stream(
            '/deepaffectsrealtime.DeepAffectsRealtime/IdentifySpeaker',
            request_serializer=deepaffects__realtime__pb2.SegmentChunk.SerializeToString,
            response_deserializer=deepaffects__realtime__pb2.SegmentSpeaker.FromString,
        )
        self.IdentifyEmotion = channel.stream_stream(
            '/deepaffectsrealtime.DeepAffectsRealtime/IdentifyEmotion',
            request_serializer=deepaffects__realtime__pb2.SegmentChunk.SerializeToString,
            response_deserializer=deepaffects__realtime__pb2.SegmentEmotion.FromString,
        )


class DeepAffectsRealtimeServicer(object):
    """Interface exported by the server.
    """

    def IdentifySpeaker(self, request_iterator, context):
        """A Bidirectional streaming RPC.

        Accepts a stream of SegmentChunk sent while a route is being traversed,
        while receiving other SegmentSpeaker (e.g. from other users).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IdentifyEmotion(self, request_iterator, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DeepAffectsRealtimeServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'IdentifySpeaker': grpc.stream_stream_rpc_method_handler(
            servicer.IdentifySpeaker,
            request_deserializer=deepaffects__realtime__pb2.SegmentChunk.FromString,
            response_serializer=deepaffects__realtime__pb2.SegmentSpeaker.SerializeToString,
        ),
        'IdentifyEmotion': grpc.stream_stream_rpc_method_handler(
            servicer.IdentifyEmotion,
            request_deserializer=deepaffects__realtime__pb2.SegmentChunk.FromString,
            response_serializer=deepaffects__realtime__pb2.SegmentEmotion.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'deepaffectsrealtime.DeepAffectsRealtime', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))