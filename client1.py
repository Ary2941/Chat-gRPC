import grpc
import chat_pb2
import chat_pb2_grpc
import google.protobuf.empty_pb2 as empty_pb2

def send_message(stub, sender, message):
    request = chat_pb2.MessageRequest(sender=sender, message=message)
    response = stub.SendMessage(request)
    #print(f"Message sent: {response.sender}: {response.message}")

def receive_messages(stub):
    for response in stub.ReceiveMessage(empty_pb2.Empty()):
        print(f"Received message: {response.sender}: {response.message}")

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = chat_pb2_grpc.ChatServiceStub(channel)

    sender = input("Enter your name: ")

    send_message(stub, sender, "Hello, I've joined the chat!")

    try:
        while True:
            message = input("Type a message (or type 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            send_message(stub, sender, message)
            #receive_messages(stub)
    except KeyboardInterrupt:
        pass
    finally:
        channel.close()

if __name__ == '__main__':
    run()
