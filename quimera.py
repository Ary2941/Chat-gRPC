import blueprint.client as client, blueprint.server as server, threading

serveraddress = input("minha porta: ")
clientaddress = input("porta do amigo: ")


x = threading.Thread(target=client.Client(clientaddress,serveraddress).run_client).start()
server.run_server(int(serveraddress))
