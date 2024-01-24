import grpc
import threading, sys
import PySimpleGUI as sg
import chat_pb2 as chat
import chat_pb2_grpc as rpc

address = 'localhost'

class Client:

    def __init__(self,port, u: str,):
        self.username = u
        self.connected = False
        self.connect_to_server(port)

    def connect_to_server(self,port):
        '''
        try:
            channel = grpc.insecure_channel(address + ':' + str(port))
            self.conn = rpc.ChatServerStub(channel)
            print("conectado!")
            self.connected = True

        except grpc.RpcError as e:
            print("Erro ao conectar ao servidor:", e)
            self.connected = False
            self.window.close()
        '''
        while not self.connected:
            try:
                channel = grpc.insecure_channel(address + ':' + str(port))
                self.conn = rpc.ChatServerStub(channel)
                self.connected = True
                print("lock and loaded!")

            except grpc.RpcError as e:
                print("Error connecting to the server:", e)
                self.connected = False
                self.window.close()

    def send_message(self, message):
        if message != '' and self.connected:
            n = chat.Note()
            n.name = self.username
            n.message = message
            self.conn.SendNote(n)

    def message_sender(self):
        while 1:
            if self.connected:
                message = input("") 
                self.send_message(message)


    def run_client(self):
        threading.Thread(target=self.message_sender).start()

#Client(input("porta: ")).run_client()