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
