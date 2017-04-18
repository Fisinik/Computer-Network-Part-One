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
        
        def info():
            info="Metodat qe mund te implementohen nga serveri jane:\n1.IP\n2.PORT\n3.ZANORE\n4.PRINTO\n5.HOST\n6.TIME\n7.KENO\n8.FAKTORIEL\n9.KONVERTO\n10.MOOD\n11.PAGA\n12.FUNC\n13.KTHE\n14.CAESAR\nFIBO\nPITAGORA\nFUNFACT\n."     
            client.send(info.encode("utf-8"))
         
        def keno():
            i=0
            A = []
            for i in range (0,19):            
                rand = random.randint(1,80)
                
                A.append(rand)
            return(str(A[0:19]))   

        def ip():
            return (str(address[0]))

        def port():
            return (str(address[1]))

        def koha():
            currentTime = time.ctime(time.time())
            return str(currentTime)
        
        def host():
            return gethostname()
        
        def zanore(fjalia):
            count=0
            for letter in fjalia:
                if(letter in ['A','E','I','O','U','Y','\u00CB','\u00EB','a','e','i','o','u','y']):
                    count+=1
                    
            a="Pergjigja:Teksi i derguar permban "+str(count)+" zanore"
            if sys.getsizeof(a)<=128:
                client.send(a.encode('utf-8'))
            else:
                client.send("Error: Pergjigja shume e gjate!")
        
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
      
    #Metoda 1 - Fjolla Beqiri
        def mood():
            mood=random.randint(1,3)
            if mood==1:
                #neutral        
                client.send("\nYou are:\n-----------\n|         |\n| 0     0 |\n|    <    |\n|         |\n| _______ |\n|         |\n|         |\n-----------".encode('utf-8'))
