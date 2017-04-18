import socket
import threading
import random
import time
import math
import sys
from socket import gethostname, gethostbyname

class ThreadedServer(object):
    

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()
            
def listenToClient(self, client, address):
        #funksionet
        def funfact():
            rand = random.randint(1,5)
            if rand == 1:
                rand = "hi1"
                elif rand == 2:
                rand = "hi2"
            elif rand == 3:
                rand = "hi3"
            elif rand == 4:
                rand = "hi4"
                elif rand == 5:
                rand = "hi5"
            else:
                rand = "not possible"
            return rand
