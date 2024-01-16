from concurrent import futures
import sys,os,time,threading
import grpc
import chat_pb2 as chat
import chat_pb2_grpc as rpc
import threading

def keyboard_interrupt_monitor():
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nEncerrando o servidor...")
        sys.exit()

class ChatServer(rpc.ChatServerServicer):
    def __init__(self):
        self.chats = []

    def ChatStream(self, request_iterator, context):
        lastindex = 0
        while True:
            while len(self.chats) > lastindex:
                n = self.chats[lastindex]
                lastindex += 1
                yield n

    def SendNote(self, request: chat.Note, context):
        print("[{}] {}".format(request.name, request.message))
        self.chats.append(request)
        return chat.Empty()

def run_server(port):
    monitor_thread = threading.Thread(target=keyboard_interrupt_monitor, daemon=True)
    monitor_thread.start()
    

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpc.add_ChatServerServicer_to_server(ChatServer(), server)
    print('Starting server. Listening...')
    
    try:
        sys.stderr = open('nul', 'w')  # No Windows
        server.add_insecure_port('[::]:' + str(port))
        server.start()
        keyboard_interrupt_monitor()
    except Exception as e:
        # Ignorar exceções específicas que você quer evitar
        print("OPS:", e)

run_server(int(sys.argv[1]))
