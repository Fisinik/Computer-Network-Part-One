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
        self.sock.listen(10)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()
            print(str(address[0])+" u lidh ne portin: "+str(address[1]) + ".")
            
def listenToClient(self, client, address):
        #funksionet
        def funfact():
            rand = random.randint(1,12)
            if rand == 1:
                 rand = "There are no pain receptors in the brain itself. But he meninges (coverings around the brain), periosteum (coverings on the bones), and the scalp all have pain receptors. Surgery can be done on the brain and technically the brain does not feel that pain. With that said, the brain is the tool we use to detect pain."
            elif rand == 2:
                 rand = "The pyramid of Khufu at Giza, Egypt, is the world's tallest. Also known as the Great Pyramid, it was 146.7 m (481.4 ft) high when completed around 4,500 years ago, but erosion and vandalism have reduced its height to 137.5 m (451.4 ft) high today. Khufu is also known as Cheops in Greek."
            elif rand == 3:
                 rand = "Profile America -- Thursday, May 12th. This week marks the anniversary of the first regularly scheduled television broadcasts -- and the date may surprise you.They were made in 1928 and originated from radio station WGY in Schenectady, New York."
            elif rand == 4:
                 rand = "A hat trick originally meant three goals in a row, with no intervening goals by either team. Hockey borrowed the term from Cricket. In 1858, a cricket player in England took three wickets with consecutive balls, an incredible trick. As a reward, his club gave the bowler a new hat, hence the term \"hat trick.\""
            elif rand == 5:
                 rand = "All communication between Mars and Earth goes through satellites. Because of the distance, there is a substantial delay. As communication signals travel at the speed of light, this means that it can take between 3 and 22 minutes for the information to reach the other end, so a phone call would not be practical."
            elif rand == 6:
                 rand = "For example, in 1971, Phil Knight paid Carolyn Davidson $35 to create the Nike \"Swoosh\" logo. Today, global brand consultancy Interbrand ranks Nike No. 25 on its list of the top 100 most valuable brands in the world, with an estimated value of more than $13 billion." 
            elif rand == 7:
                 rand = "The arrangement of the first six letters in the top alphabet row of a standard keyboard QWERTY goes way back. The layout was created in 1873 when Christopher Latham Sholes made improvements to his earlier typewriter models in order to design a quicker and more efficient typewriter for E. Remington and Sons."
            elif rand == 8:
                 rand = "A chin is a protrusion at the front of the mandible bone, which humans and elephants have while gorillas-and apparently every other animal-do not have. Skulls of animals in question."
            elif rand == 9:
                 rand = "Giant Jupiter is almost three times heavier than all the other eight planets put together. This sounds like a simple, .straightforward answer to the question, but there is more to it. Jupiter is 1,318 times . to an equal volume of water.Giant Jupiter is almost three times heavier than all the other eight planets put together. This sounds like a simple, .straightforward answer to the question, but there is more to it. Jupiter is 1,318 times . to an equal volume of water."
            elif rand == 10:
                 rand = "Mel Blanc ( the voice of Looney Tunes ) performed in 709 films, not including over 100 TV movies and video productions. He also had 81 uncredited voice parts in films. Right behind Mel Blanc on the IMDB's list of most prolific actors is Adoor Bhasi. Before his death in 1990, Bhasi was featured in 549 films."
            elif rand == 11:
                 rand = "The four kings, for example, are based on real rulers: the king of diamonds represents the wealthy Julius Caesar; the king of clubs is the brutal Alexander the Great; the king of spades represents the strong but kind David of Israel; and the king of Hearts represents the emotionally disturbed Charles VII of France."
            elif rand == 12:
                 rand = "During World War II, copper was so badly needed for the war effort (to make shell casings) that the U.S. penny was made out of steel that year, which is why most 1943 pennies are silver colored. They are worth about 12 to 15 cents each in ciruclated condition, and as much as 50 cents or more if Uncirculated."
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
                client.send("Error: Pergjigja shume e gjate!".encode('utf-8'))
 
        def printo(fjaliaDerguar):
            client.send(str(fjaliaDerguar).encode('utf-8'))

        def celsiusToKelvin(celsius):
            kelvin=celsius+273.15
            client.send(("Pergjigja: "+str(kelvin).encode("UTF-8")+"K"))
            
        def celsiusToFahrenheit(celsius):
            fahrenheit = celsius + 32
            client.send(("Pergjigja: "+str(fahrenheit).encode("UTF-8")+"F"))

        def fahrenheitToCelsius(fahrenheit):
            celsius = fahrenheit - 32 
            client.send(("Pergjigja: "+str(celsius).encode("UTF-8")+"C"))
            
        def kelvinToFahrenheit(kelvin):
            fahrenheit=kelvin*1.8-459.67
            client.send(("Pergjigja: "+str(fahrenheit).encode("UTF-8")+"F"))

        def kelvinToCelsius(kelvin):
            celsius=kelvin-273.15
            client.send(("Pergjigja: "+str(celsius).encode("UTF-8")+"C"))
            
        def fahrenheitToKelvin(fahrenheit):
            kelvin=((fahrenheit+459.67)*5)/9
            client.send(("Pergjigja: "+str(kelvin).encode("UTF-8")+"K"))

        def poundToKilogram(pound):
            kilogram = pound - 0.546408
            if kilogram != 1:
                client.send(("Pergjigja: "+str(round(kilogram,4)).encode("UTF-8")+" kilograms"))    
            else:    
                client.send(("Pergjigja: "+str(kilogram).encode("UTF-8")+" kilogram"))               

        def kilogramToPound(kilogram):
            pound = kilogram + 0.546408
            if pound != 1:
                client.send(("Pergjigja: "+str(round(pound,4)).encode("UTF-8")+" pounds"))   
            else:
                client.send(("Pergjigja: "+str(pound).encode("UTF-8")+" pound"))   
                
        def faktorieli(numri):
            i=1
            f=1
            for i in range(1,numri+1):
                f=f*i
                i=i+1
            client.send(("Pergjigja: "+str(f).encode("UTF-8")))
                
                
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
  
        # Metoda 2 - Fjolla Beqiri

        
        def paga(bruto):
            trusti=5 #(%)
            pagaBruto=bruto
            kontributiPunetorit=(pagaBruto*trusti)/100.0


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
        #Elza Latifi -Metoda 1

        def caesar(plaintext):
            ciphertext=''
            for char in plaintext:
                if char.isalpha():
                    alfabeti=ord(char)+5
                    if(alfabeti>ord('z')):
                        alfabeti=alfabeti-26
                shkronjaFundit=chr(alfabeti)
                ciphertext+=shkronjaFundit
            client.send(("Ciphertext: "+ciphertext).encode('utf-8'))

        def stars(nr):
    
            if nr==5:
                client.send("Yjesia me e njohur me 5 yje eshte Kasiopea".encode('utf-8'))
            elif nr==6:
                client.send("Yjesia me e njohur me 6 yje eshte Lyra".encode('utf-8'))
            elif nr==7:
                client.send("Yjesia me e njohur me 7 yje eshte Kygus".encode('utf-8'))
            elif nr==8:
                client.send("Yjesite me te njohur me 8 yje jane Andromeda,Luani dhe Peshorja".encode('utf-8'))
            elif nr==9:
                client.send("Yjesia me e njohur me 9 yje eshte Bricjapi".encode('utf-8'))
            elif nr==10:
                client.send("Yjesia me e njohur me 10 yje eshte Pegasusi".encode('utf-8'))
            elif nr==11:
                client.send("Yjesia me e njohur me 11 yje eshte Hidra".encode('utf-8'))
            elif nr==12:  
                client.send("Yjesia me e njohur me 12 yje eshte Virgjeresha".encode('utf-8'))
            elif nr==13:
                client.send("Yjesia me e njohur me 13 yje eshte Ofikusi".encode('utf-8'))
            elif nr==14:
                client.send("Yjesia me e njohur me 14 yje eshte Drako".encode('utf-8'))
            elif nr<5:
                client.send("Nuk ka yjesi me numer me te vogel te yjeve se 5".encode('utf-8'))
            elif nr>14 and nr<100:                
                client.send(("Jane gjithsej 88 yjesi te njohura ne dy hemisferat; 78 nga te cilat kane numer te yjeve me te madh se "+str(15)).encode('utf-8'))
            else :
                client.send("I'm asking for a Constellation not a Galaxy".encode('utf-8'))

        #----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #Blenda Gashi - Metoda 1

        def fibonacci(numri):
            i=0                
            vleraPare=0
            vleraDyte=1
            a=[]
            for i in range (0,numri):
                if(i<=1):
                    tjetri=i
                else:
                    tjetri=vleraPare+vleraDyte
                    vleraPare=vleraDyte
                    vleraDyte=tjetri  
                a.append(tjetri)
            client.send(("Pergjigja:".encode("UTF-8")+str(a[0:]).encode("UTF-8")))

        #Blenda Gashi - Metoda 2

        def pitagora(k1,k2):
            katrori=math.pow(k1,2)+math.pow(k2,2)                    
            hipotenuza=math.sqrt((katrori))
            client.send("Pergjigja:Hipotenuza eshte ".encode('utf-8')+str(float(round(hipotenuza,3))).encode('utf-8'))

        #---------------------------------------------------------------------------------------------------------------------------------------------------------------------                    
                    
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

                else:  
                    if metoda[0] == "ZANORE":
                        teksti = data[7:]
                        zanore(teksti) 
                    elif metoda[0] == "RECMOVIE":
                        teksti = data[9:]
                        recMovies(teksti)
                    elif metoda[0] == "KTHE":
                        teksti = data[4:]
                        kthePrapa(str(teksti).encode('utf-8'))
                        
                        except:
                client.close()
                False

if __name__ == "__main__":
    port_num = 9000
    ThreadedServer('',port_num).listen()
