
# chat_server.py
import grpc
from concurrent import futures
import chat_pb2
import chat_pb2_grpc
import google.protobuf.empty_pb2 as empty_pb2
import time

class ChatServicer(chat_pb2_grpc.ChatServiceServicer):
    def __init__(self):
        self.messages = []

    def SendMessage(self, request, context):
        response = chat_pb2.MessageResponse()
        response.sender = request.sender
        response.message = request.message
        self.messages.append(response)
        print(f"Message received on server: {response.sender}: {response.message}")
        return response

    def ReceiveMessage(self, request, context):
        for message in self.messages:
            yield message

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)  # Um dia em segundos
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
