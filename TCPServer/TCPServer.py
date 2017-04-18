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
               elif rand == 4:
                    rand = "Scary Movies: Casting some wannabes (Emma Roberts): \n All the great movies made fun of."
                    client.send(rand.encode('utf-8'))
                elif rand == 5:
                    rand = "The Hangover (2009): Casting Bradley Cooper, Ed Helms, Zach Galifianakis: \n Crazy stories of three retarded friends. AAND A MONKEY!"
                    client.send(rand.encode('utf-8'))
            elif genre == "horror":
                rand = random.randint(1,5)
                if rand == 1:
                    rand = "The Ring (2002): \n Dul lulija te bunari."
                    client.send(rand.encode('utf-8'))
                elif rand == 2:
                    rand = "Texas Chainsaw (2013): \n A ruthless chainsaw murderer."
                    client.send(rand.encode('utf-8'))
                elif rand == 3:
                    rand = "se7en (): Casting Morgan Freeman, Brad Pitt : \n Two detectives facing a stone-cold serial killer."
                    client.send(rand.encode('utf-8'))
                elif rand == 4:
                    rand = "The Cabin in the Woods (2011): \n Guess what's going to happen?"
                    client.send(rand.encode('utf-8'))
                elif rand == 5:
                    rand = "The Crow (1994): \n Does he ever die?"
                    client.send(rand.encode('utf-8'))

            if genre == "drame":

                rand = random.randint(1,5)
                if rand == 1:
                    rand = "Forest Gump (1994): Casting Tom Hanks: \n Run Forest RUuuun."
                    client.send(rand.encode('utf-8'))

                elif rand == 2:
                    rand = "Casablanca (1942): Casting Humphrey Bogart, Madeleine LeBeau: \n A movie older that my grandma."
                    client.send(rand.encode('utf-8'))
                elif rand == 3:
                    rand = "Fight Club (1999): Casting Brad Pitt: \n Fight fight fight!"
                    client.send(rand.encode('utf-8'))
                elif rand == 4:
                    rand = "A Beautiful Mind (2001): Casting Russell Crowe \n A mathematician gone mad."
                    client.send(rand.encode('utf-8'))
                elif rand == 5:
                    rand = "The Imitation Game (2014): Casting Benedict Cumberbatch \n A russian spy mathematician."
                    client.send(rand.encode('utf-8'))
            elif genre == "sci-fi":
                rand = random.randint(1,5)
                if rand == 1:
                    rand = "The Matrix (1999): Casting Keanu Reeves \n A conspiration  "
                    client.send(rand.encode('utf-8'))

                elif rand == 2:
                    rand = "Star Wars-The Force Awakens (2017): Casting Harrison Ford, Mark Hamill \n The force needs five more minutes."
                    client.send(rand.encode('utf-8'))
                elif rand == 3:
                    rand = "Interstellar (2014): Casting Matthew McConaughey, Anne Hathaway \n What do you do when stuck in a 5th dimension in outer space? Travel back in time and scare your daughter."
                    client.send(rand.encode('utf-8'))
                elif rand == 4:
                    rand = "Planet of the Apes (2001): Casting Mark Wahlberg: \n Monkeys gone wild."
                    client.send(rand.encode('utf-8'))
                elif rand == 5:

                    rand = "Eternal Sunshine of the Spotless Mind (2004): Casting Jim Carrey (no it's not comedy) \n He finally meets the woman of his life and then loses his memory."
                    client.send(rand.encode('utf-8'))
            elif genre == "random":
                rand = random.randint(0,4)
                A= ["aksion", "horror", "sci-fi", "drame", "komedi" ]
                randomMovie = A[rand]
                recMovies(randomMovie)
 

        while True:
            try:
                data = client.recv(1024)
                data = data.decode("utf-8")
                metoda = data.split(" ")

                if len(metoda) == 1:
                    
                    if metoda[0] == "FUNFACT":
                        client.send(funfact().encode('utf-8'))
                    elif metoda[0] == "KENO":
                        client.send(keno().encode('utf-8'))
                    elif metoda[0] == "IP":
                        client.send(ip().encode('utf-8'))
                    elif metoda[0] == "INFO":
                        info()
                    elif metoda[0] == "PORT":
                        client.send(port().encode('utf-8'))
                    elif metoda[0] == "TIME":
                        client.send(koha().encode('utf-8'))
                    elif metoda[0] == "HOST":
                        client.send(host().encode('utf-8'))
                    elif metoda[0] == "MOOD":
                        mood()
