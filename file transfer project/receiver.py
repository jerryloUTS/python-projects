import socket # see sender.py comments
import tqdm # lets us see the progress of the transfer

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()

client, addr = server.accept() #addr = address

file_name = client.recv(1024).decode()
print(file_name)
file_size = client.recv(1024).decode()
print(file_size)

file = open(file_name, "wb")

file_bytes = b"" #allows the application to detect <ENDPOINT> in full; having the endpoint in the quotations allows the file to be detected and receive the file properly

done = False

progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=int(file_size)) #"B" refers to bytes, unit_scale refers to scaling the file size, unit_divisor = file size? idk lol

while not done: # continues to receive data in 1024 bytes bits until it's done (probably questionable practice)
    data = client.recv(1024)
    if file_bytes[-10:] == b"<ENDPOINT>": # 10 indicates the size of "file_bytes"; it checks for the text within the quotations
                                          # in the initial declaration if it is 10 bytes and compares to the text in sender.py
        done = True
    else:
        file_bytes += data
    progress.update(1024)

file.write(file_bytes)

file.close()
server.close()
client.close()