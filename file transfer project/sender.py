import os # portable way of using OS dependant functionality (os.path.getsize, for example)
import socket # lets us work with sockets. these sockets let us create network connections using TCP and UDP to send and receive data.

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

file = open("image.png", "rb") # loads image and gathers filesize
file_size = os.path.getsize("image.png")

client.send("received_image.png".encode()) # send image/filename
client.send(str(file_size).encode()) # send image size

data = file.read()
client.sendall(data) # send all data
client.send(b"<ENDPOINT>") # ending tag to indicate finish

file.close()
client.close()
