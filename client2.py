# client2.py

import grpc
import chat_pb2
import chat_pb2_grpc
import threading
from google.protobuf import empty_pb2

class ChatClient:
    def __init__(self, name):
        self.name = name
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = chat_pb2_grpc.ChatStub(self.channel)

    def send_message(self, content):
        request = chat_pb2.Message(sender=self.name, content=content)
        response = self.stub.SendMessage(request)
        print(f"{response.sender}: {response.content}")

    def receive_messages(self):
        for message in self.stub.ReceiveMessage(empty_pb2.Empty()):
            print(f"{message.sender}: {message.content}")

def run_client2():
    client = ChatClient("Client 2")
    threading.Thread(target=client.receive_messages, daemon=True).start()
    while True:
        message = input("Client 2, type a message: ")
        client.send_message(message)

if __name__ == "__main__":
    run_client2()
