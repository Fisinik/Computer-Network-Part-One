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
                            #-----------
                            #|         |
                            #| 0     0 |
                            #|    <    |
                            #|         |
                            #| _______ |
                            #|         |
                            #----------- 
           
            elif mood==2:
                #sad
                client.send("\nYou are:\n-----------\n|         |\n| 0     0 |\n|    <    |\n|         |\n|    .    |\n|  .   .  |\n| .     . |\n-----------".encode('utf-8'))
                            #-----------
                            #|         |
                            #| 0     0 |
                            #|    <    |
                            #|         |
                            #|    .    |
                            #| .'   '. |
                            #-----------
                            
            elif mood==3:
                #happy
                client.send("\nYou are:\n-----------\n|         |\n| 0     0 |\n|    <    |\n|         |\n| .     . |\n|  .   .  |\n|   ...   |\n-----------".encode('utf-8'))
                            #-----------
                            #|         |
                            #| 0     0 |
                            #|    <    |
                            #|         |
                            #| .     . |
                            #|  '...'  |
                            #-----------                             
 
 #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       				
        # Metoda 1 - Fjolla Zatriqi

        def kthePrapa(var):
          reverse= var [::-1]
          client.send(reverse)

        #Metoda 2 - Fjolla Zatriqi
        def f(x):
          return math.pow(x,2)+3

        def g(x):
          return x+1

        def gCf(x):
          y=g(f(x))
         # print(y)
          client.sendto(str(y).encode("utf-8"))

 #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

        def recMovies(genre):
    
            if genre == "aksion":
                rand = random.randint(1,5)
                if rand == 1:
                    rand = "Taken (2008): Casting Liam Neeson (the badass) and his daughter (Maggie Grace) kidnapped by some drug dealing Albanians"
                    client.send(rand.encode('utf-8'))
                elif rand == 2:
                    rand = "The Avengers (2012): Casting Robert Downey Jr., Chris Evans, Natalie Portman, Tom Hiddleston. \n A fight between good and evil, deities and humans"
                    client.send(rand.encode('utf-8'))
                elif rand == 3:
                    rand = "Fast and Furious 7: The Fate of the Furious (2017): Casting Vin Diesel, R.I.P Paul Walker :( , Jason Statham, The Rock. \n Epic car stunts, cops and S.W.A.Ts on their tail."
                    client.send(rand.encode('utf-8'))
                elif rand == 4:
                    rand = "Spectre (2015): Casting Daniel Craig: \n The famous series of James Bond 007, the latest movie."
                    client.send(rand.encode('utf-8'))
                elif rand == 5:
                    rand = "John Wick (2014): Casting Keanu Reeves: \n Epic fights that make you question the capability of a single's man power."
                    client.send(rand.encode('utf-8'))
            elif genre == "komedi":
                rand = random.randint(1,5)
                if rand == 1:
                    rand = "Why Him? (2016): Casting James Franco: \n Hilarious."
                    client.send(rand.encode('utf-8'))
                elif rand == 2:
                    rand = "Fist Fight (2017): Casting Ice Cube, Charlie Day \n Teachers fighting over nothing."
                    client.send(rand.encode('utf-8'))
                elif rand == 3:
                    rand = "Bruce Almighty (2003): Casting Jim Carrey: \n Ever imagined being a god? well see if you can beat Morgan Freeman at that!"
                    client.send(rand.encode('utf-8'))
