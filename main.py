import socket
import sys
import wave

from thread import start_new_thread

host = "0.0.0.0"
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((host, port))
except:
    print("Failed to bind socket")
    sys.exit()

server.listen(10)

print("Server is listening")

number = 0

def handleConnection(connection):
    global number

    myNumber = number

    number += 1

    print("Write some %ds" % myNumber)

    file = wave.open("%ds.wav" % myNumber, "w")
    file.setnchannels(1)
    file.setsampwidth(2)
    file.setframerate(44100)

    while True:
        data = connection.recv(1024)

        if not data:
            break

        file.writeframes(data)

    connection.close()

    print("No more %ds" % myNumber)

while True:
    connection, address = server.accept()

    start_new_thread(handleConnection, (connection,))

server.close()