import socket
from threading import Thread
import time
import os

path = os.environ['HOME']+'/.services/service.txt'

if not os.path.exists(path):
    print(path, ' not found, creating an empty file')
    with open(path, 'a') as pre_writer:
        pre_writer.write('ServiceDiscovery;;192.168.0.255;;A simple service broadcast;;4012\n')
        pre_writer.close()

def init_parameters(broadcast_address, port):

    broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = (broadcast_address, port)

    broadcast_socket.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_BROADCAST,
        1
    )
    #return broadcast_address:
    print('Initialized socket parameters at: ', addr)
    return (broadcast_socket, addr)


def callback_function(*args):

    #do your work here
    print('Emitted broadcast')
    pass


class EventLoop(Thread):

    def __init__(self, callback, b_socket,addr, broadcast_data = None, timeinterval = 5):
        Thread.__init__(self)
        self.callback = callback
        self.broadcast_data = broadcast_data
        self.timeinterval = timeinterval
        self.b_socket = b_socket
        self.addr = addr
       
    def process_broadcast_data(self):
        with open(path, 'r') as reader:
                self.broadcast_data = reader.readlines()
                self.broadcast_data = set(self.broadcast_data)
            data = ""
            for line in self.broadcast_data:
                data+=line
            return data
    
    def run(self):
        while True:
            data = self.process_broadcast_data()
            self.b_socket.sendto(bytes(data.encode('utf-8')), self.addr)
        
            #callback demo, implement any funcition here
            self.callback('success')

            time.sleep(self.timeinterval)


#usage:
sock, addr = init_parameters('192.168.0.255', 4012)

EventLoop(callback_function, sock, addr).start()

        
