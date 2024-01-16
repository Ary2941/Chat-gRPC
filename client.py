import grpc
import threading, sys
import PySimpleGUI as sg
import chat_pb2 as chat
import chat_pb2_grpc as rpc

address = 'localhost'
port = sys.argv[1]

class Client:

    def __init__(self, u: str):
        self.username = u
        self.connected = True
        self.layout = self.__setup_ui()
        self.window = sg.Window('Chat - {}'.format(self.username), self.layout, finalize=True)
        self.connect_to_server()

    def connect_to_server(self):
        try:
            channel = grpc.insecure_channel(address + ':' + str(port))
            self.conn = rpc.ChatServerStub(channel)
            threading.Thread(target=self.__listen_for_messages, daemon=True).start()
        except grpc.RpcError as e:
            print("Erro ao conectar ao servidor:", e)
            self.connected = False
            self.window.close()

    def __listen_for_messages(self):
        while self.connected:
            try:
                for note in self.conn.ChatStream(chat.Empty()):
                    print("R[{}] {}".format(note.name, note.message))
                    self.window.write_event_value('RECEIVE_MESSAGE', note)
            except grpc.RpcError as e:
                print("Erro de comunicação com o servidor:", e)
                self.connected = False
                self.window.close()

    def send_message(self, message):
        if message != '' and self.connected:
            n = chat.Note()
            n.name = self.username
            n.message = message
            print("S[{}] {}".format(n.name, n.message))
            self.conn.SendNote(n)

    def __setup_ui(self):
        sg.theme('SystemDefault1')
        layout = [
            [sg.Multiline('', size=(40, 15), key='-OUTPUT-', disabled=True)],
            [sg.InputText('', size=(35, 1), key='-INPUT-', enable_events=True),
             sg.Button('Send', bind_return_key=True)]
        ]
        return layout

    def run_client(self):
        while True:
            event, values = self.window.read()

            if event in (sg.WIN_CLOSED, 'Exit'):
                self.connected = False
                break

            if event == 'Send':
                message = values['-INPUT-']
                self.send_message(message)
                self.window['-INPUT-'].update('')

            if event == 'RECEIVE_MESSAGE':
                note = values['RECEIVE_MESSAGE']
                self.window['-OUTPUT-'].print('[{}] {}'.format(note.name, note.message))

        self.window.close()

client = Client(sys.argv[2]).run_client()
