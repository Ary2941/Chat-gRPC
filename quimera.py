import blueprint.client as client, blueprint.server as server, threading

serveraddress = input("my address: ")
clientaddress = input("their address: ")


x = threading.Thread(target=client.Client(clientaddress,serveraddress).run_client).start()
server.run_server(int(serveraddress))
