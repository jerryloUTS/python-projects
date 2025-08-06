import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()

client, addr = server.accept() #addr = address

file_name = client.recv(1024).decode()
print(file_name)
file_size = client.recv(1024).decode()
print(file_size)

file = open(file_name, "wb")

file_bytes = bytearray() #allows the application to detect <ENDPOINT> in full; having the endpoint in the quotations allows the file to be detected and receive the file properly

done = False

while not done:
    data = client.recv(1024)
    if file_bytes[-10:] == b"<ENDPOINT>": # 10 indicates the size of "file_bytes"; it checks for the text within the quotations
                                          # in the initial declaration if it is 10 bytes and compares to the text in sender.py
        done = True
    else:
        file_bytes += data

file.write(file_bytes)

file.close()
server.close()
client.close()
