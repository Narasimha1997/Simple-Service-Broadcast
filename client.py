import socket
import time

'''Demo implementation of Service Discovery client '''

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

sock.bind(('', 4012))

while True:
    now = time.time()
    data = sock.recv(2048)
    delay = time.time() - now
    print(delay)
    print(data)