from socket import *
import threading
import random
from socket import gethostname, gethostbyname 
import time
import math


ip=''
port=9000

serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind((ip,port))


print("UDP Serveri eshte gati...")

def info(s,c):
    info="Metodat qe mund te implementohen nga serveri jane:\n1.IP\n2.PORT\n3.ZANORE\n4.PRINTO\n5.HOST\n6.TIME\n7.KENO\n8.FAKTORIEL\n9.KONVERTO\n10.MOOD\n11.PAGA\n12.FUNC\n13.KTHE\n14.CAESAR\nFIBO\nPITAGORA\nFUNFACT\n."     
    s.sendto(info.encode("utf-8"),c)

def zanore(fjalia,s,c):
    count=0
    for letter in fjalia:
        if(letter in ['A','E','I','O','U','Y','\u00CB','\u00EB','a','e','i','o','u','y']):
            count=count+1
    a="Pergjigja:Teksi i derguar permban "+str(count)+" zanore"
    if sys.getsizeof(a)<=128:
        s.sendto(a.encode('utf-8'),c)
    else:
        s.sendto("Error: Pergjigja shume e gjate!",c)

def keno(s,c):
    i=0
    A = []
    for i in range (0,19):            
        rand = random.randint(1,80)
        
        A.append(rand)
    s.sendto((str("Pergjigja:").encode("UTF-8")+str((A[0:19])).encode("UTF-8")),c)
    
def printo(fjaliaDerguar,s,c):
    s.sendto("Pergjigja:"+fjaliaDerguar.encode("utf-8"),c)

def celsiusToKelvin(celsius,s,c):
    kelvin=celsius+273.15
    s.sendto(("Pergjigja: "+str(kelvin).encode("UTF-8")+"K"),c)

def celsiusToFahrenheit(celsius,s,c):
    fahrenheit = celsius + 32
    s.sendto(("Pergjigja: "+str(fahrenheit).encode("UTF-8")+"F"),c)

def fahrenheitToCelsius(fahrenheit,s,c):
    celsius = fahrenheit - 32 
    s.sendto(("Pergjigja: "+str(celsius).encode("UTF-8")+"C"),c)

def kelvinToFahrenheit(kelvin,s,c):
    fahrenheit=kelvin*1.8-459.67
    s.sendto(("Pergjigja: "+str(fahrenheit).encode("UTF-8")+"F"),c)

def kelvinToCelsius(kelvin,s,c):
    celsius=kelvin-273.15
    s.sendto(("Pergjigja: "+str(celsius).encode("UTF-8")+"C"),c)

def fahrenheitToKelvin(fahrenheit,s,c):
    kelvin=((fahrenheit+459.67)*5)/9
    s.sendto(("Pergjigja: "+str(kelvin).encode("UTF-8")+"K"),c)

def poundToKilogram(pound,s,c):
    kilogram = pound - 0.546408
    if kilogram != 1:
        s.sendto(("Pergjigja: "+str(round(kilogram,4)).encode("UTF-8")+" kilograms"),c)    
    else:    
        s.sendto(("Pergjigja: "+str(kilogram).encode("UTF-8")+" kilogram"),c)   

def kilogramToPound(kilogram,s,c):
    pound = kilogram + 0.546408
    if pound != 1:
        s.sendto(("Pergjigja: "+str(round(pound,4)).encode("UTF-8")+" pounds"),c)   
    else:
        s.sendto(("Pergjigja: "+str(pound).encode("UTF-8")+" pound"),c)   

def faktorieli(numri,s,c):
    i=1
    f=1
    for i in range(1,numri+1):
        f=f*i
        i=i+1
    s.sendto(("Pergjigja: "+str(f).encode("UTF-8")),c)
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Metoda 1 - Fisnik Spahija

def funfact(s,c):
    rand = random.randint(1,12)
    try:
        if rand == 1:
            s.sendto(str("There are no pain receptors in the brain itself. But he meninges (coverings around the brain), periosteum (coverings on the bones), and the scalp all have pain receptors. Surgery can be done on the brain and technically the brain does not feel that pain. With that said, the brain is the tool we use to detect pain.").encode("UTF-8"),c)
        elif rand == 2:
            s.sendto((str("The pyramid of Khufu at Giza, Egypt, is the world's tallest. Also known as the Great Pyramid, it was 146.7 m (481.4 ft) high when completed around 4,500 years ago, but erosion and vandalism have reduced its height to 137.5 m (451.4 ft) high today. Khufu is also known as Cheops in Greek.").encode("UTF-8")),c)
        elif rand == 3:
            s.sendto(str("Profile America -- Thursday, May 12th. This week marks the anniversary of the first regularly scheduled television broadcasts -- and the date may surprise you.They were made in 1928 and originated from radio station WGY in Schenectady, New York.").encode("UTF-8"),c)
        elif rand == 4:
            s.sendto(str("A hat trick originally meant three goals in a row, with no intervening goals by either team. Hockey borrowed the term from Cricket. In 1858, a cricket player in England took three wickets with consecutive balls, an incredible trick. As a reward, his club gave the bowler a new hat, hence the term \"hat trick.\"").encode("UTF-8"),c)
        elif rand == 5:
            s.sendto(str("All communication between Mars and Earth goes through satellites. Because of the distance, there is a substantial delay. As communication signals travel at the speed of light, this means that it can take between 3 and 22 minutes for the information to reach the other end, so a phone call would not be practical.").encode("UTF-8"),c)
        elif rand == 6:
            s.sendto(str("For example, in 1971, Phil Knight paid Carolyn Davidson $35 to create the Nike \"Swoosh\" logo. Today, global brand consultancy Interbrand ranks Nike No. 25 on its list of the top 100 most valuable brands in the world, with an estimated value of more than $13 billion.").encode("UTF-8"),c) 
        elif rand == 7:
            s.sendto(str("The arrangement of the first six letters in the top alphabet row of a standard keyboard QWERTY goes way back. The layout was created in 1873 when Christopher Latham Sholes made improvements to his earlier typewriter models in order to design a quicker and more efficient typewriter for E. Remington and Sons.").encode("UTF-8"),c)
        elif rand == 8:
            s.sendto(str("A chin is a protrusion at the front of the mandible bone, which humans and elephants have while gorillas-and apparently every other animal-do not have. Skulls of animals in question.").encode("UTF-8"),c)
        elif rand == 9:
            s.sendto(str("Giant Jupiter is almost three times heavier than all the other eight planets put together. This sounds like a simple, .straightforward answer to the question, but there is more to it. Jupiter is 1,318 times . to an equal volume of water.Giant Jupiter is almost three times heavier than all the other eight planets put together. This sounds like a simple, .straightforward answer to the question, but there is more to it. Jupiter is 1,318 times . to an equal volume of water.").encode("UTF-8"),c)
        elif rand == 10:
            s.sendto(str("Mel Blanc ( the voice of Looney Tunes ) performed in 709 films, not including over 100 TV movies and video productions. He also had 81 uncredited voice parts in films. Right behind Mel Blanc on the IMDB's list of most prolific actors is Adoor Bhasi. Before his death in 1990, Bhasi was featured in 549 films.").encode("UTF-8"),c)
        elif rand == 11:
            s.sendto(str("The four kings, for example, are based on real rulers: the king of diamonds represents the wealthy Julius Caesar; the king of clubs is the brutal Alexander the Great; the king of spades represents the strong but kind David of Israel; and the king of Hearts represents the emotionally disturbed Charles VII of France.").encode("UTF-8"),c) 
        elif rand == 12:
            s.sendto(str("During World War II, copper was so badly needed for the war effort (to make shell casings) that the U.S. penny was made out of steel that year, which is why most 1943 pennies are silver colored. They are worth about 12 to 15 cents each in ciruclated condition, and as much as 50 cents or more if Uncirculated.").encode("UTF-8"),c)
    except:
        s.sendto("Something went wrong! Please try again :)".encode("UTF-8"),c)  

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Metoda 1 - Fjolla Beqiri
def mood(s,c):
    mood=random.randint(1,3)
    if mood==1:
        #neutral
        s.sendto("\nYou are:\n-----------\n|         |\n| 0     0 |\n|    <    |\n|         |\n| _______ |\n|         |\n|         |\n-----------",c)
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
        s.sendto("\nYou are:\n-----------\n|         |\n| 0     0 |\n|    <    |\n|         |\n|    .    |\n|  .   .  |\n| .     . |\n-----------",c)
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
        s.sendto("\nYou are:\n-----------\n|         |\n| 0     0 |\n|    <    |\n|         |\n| .     . |\n|  .   .  |\n|   ...   |\n-----------",c)
                    #-----------
                    #|         |
                    #| 0     0 |
                    #|    <    |
                    #|         |
                    #| .     . |
                    #|  '...'  |
                    #----------- 
                    
#Metoda 2 - Fjolla Beqiri
def paga(bruto,s,c):
    trusti=5 #(%)
    pagaBruto=bruto
    kontributiPunetorit=(pagaBruto*trusti)/100.0
    kontributiPunedhenesit=kontributiPunetorit
    gjithsejKontributet=kontributiPunetorit+kontributiPunedhenesit
    pagaPerTatim=pagaBruto-kontributiPunetorit
    
    if pagaPerTatim<=80:
                teArdhuratETatueshme=pagaPerTatim-0
                pagaPrej0ne80=(teArdhuratETatueshme*0)/100.0
                gjithsejTatimi=pagaPrej0ne80
    elif pagaPerTatim>80 and pagaPerTatim<=250:
                teArdhuratETatueshme=pagaPerTatim-80
                pagaPrej80ne250=(teArdhuratETatueshme*4)/100.0
                gjithsejTatimi=pagaPrej80ne250
    elif pagaPerTatim>250 and pagaPerTatim<=450:
                teArdhuratETatueshme=pagaPerTatim-250
                pagaPrej80ne250=6.8
                pagaPrej250ne450=(teArdhuratETatueshme*8)/100.0
                gjithsejTatimi=pagaPrej250ne450+pagaPrej250ne450
    else:
                teArdhuratETatueshme=pagaPerTatim-450
                pagaPrej80ne250=6.8
                pagaPrej250ne450=16
                pagaMbi450=(teArdhuratETatueshme*10)/100.0
                gjithsejTatimi=pagaPrej250ne450+pagaPrej250ne450+pagaMbi450
    pagaNeto=pagaBruto-kontributiPunetorit-gjithsejTatimi
    s.sendto("Pergjigja: Vlere neto e pages eshte "+str(pagaNeto)+" euro .",c)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       				
# Metoda 1 - Fjolla Zatriqi

def kthePrapa(var,s,c):
    reverse= var [::-1]
    s.sendto(str(reverse),c)

#Metoda 2 - Fjolla Zatriqi
def f(x):
    return math.pow(x,2)+3

def g(x):
    return x+1

def gCf(x,s,c):
    y=g(f(x))
    s.sendto(str(y).encode("utf-8"),c)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Elza Latifi -Metoda 1

def caesar(plaintext,s,c):
    ciphertext=''
    for char in plaintext:
        if char.isalpha():
            alfabeti=ord(char)+5
            if(alfabeti>ord('z')):
                alfabeti=alfabeti-26
        shkronjaFundit=chr(alfabeti)
        ciphertext+=shkronjaFundit
    s.sendto("Ciphertext: "+str(ciphertext),c)
    
#Elza Latifi-Metoda 2

def stars(nr,s,c):
    
    if nr=='5':
        s.sendto("Yjesia me e njohur me 5 yje eshte Kasiopea".encode('utf-8'),c)
    elif nr=='6':
        s.sendto("Yjesia me e njohur me 6 yje eshte Lyra".encode('utf-8'),c)
    elif nr=='7':
        s.sendto("Yjesia me e njohur me 7 yje eshte Kygus".encode('utf-8'),c)
    elif nr=='8':
        s.sendto("Yjesite me te njohur me 8 yje jane Andromeda,Luani dhe Peshorja".encode('utf-8'),c)
    elif nr=='9':
        s.sendto("Yjesia me e njohur me 9 yje eshte Bricjapi".encode('utf-8'),c)
    elif nr=='10':
        s.sendto("Yjesia me e njohur me 10 yje eshte Pegasusi".encode('utf-8'),c)
    elif nr=='11':
        s.sendto("Yjesia me e njohur me 11 yje eshte Hidra".encode('utf-8'),c)
    elif nr=='12':
        s.sendto("Yjesia me e njohur me 12 yje eshte Virgjeresha".encode('utf-8'),c)
    elif nr=='13':
        s.sendto("Yjesia me e njohur me 13 yje eshte Ofikusi".encode('utf-8'),c)
    elif nr=='14':
        s.sendto("Yjesia me e njohur me 14 yje eshte Drako".encode('utf-8'),c)
    elif nr<'5':
        s.sendto("Nuk ka yjesi me numer me te vogel te yjeve se 5".encode('utf-8'),c)
    elif nr>'14' and nr<'100':
        s.sendto("Jane gjithsej 88 yjesi te njohura ne dy hemisferat; 78 nga te cilat kane numer te yjeve me te madh se"+str(nr).encode('utf-8'),c)
    else :
        s.sendto("Jep nje numer me te vogel se 100".encode('utf-8'),c)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Blenda Gashi - Metoda 1

def fibonacci(numri,s,c):
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
    s.sendto(("Pergjigja:".encode("UTF-8")+str(a[0:]).encode("UTF-8")),c)

#Blenda Gashi - Metoda 2

def pitagora(k1,k2,s,c):
    katrori=math.pow(k1,2)+math.pow(k2,2)
    hipotenuza=math.sqrt((katrori))
    s.sendto("Pergjigja:Hipotenuza eshte ".encode('utf-8')+str(float(round(hipotenuza,3))).encode('utf-8'),c)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def handleClient(s,c,data):
    try:
        if (data.decode('utf-8')).isspace() :
                  s.sendto("Shtypni dicka",c)
        else:
            metoda=data.split(" ")
            if len(metoda)==1:       
                if metoda[0].decode("UTF-8") == "KENO":
                     keno(s,c)
                elif metoda[0].decode("UTF-8") == "INFO":   
                     info(s,c)
                elif metoda[0].decode("UTF-8") == "IP":
                    a="Pergjigja:IP adresa e klientit eshte ".encode("UTF-8")+str(c[0]).encode("UTF-8")
                    if(sys.getsizeof(a)<=128):
                          s.sendto(a,c)
                    else:
                          conn.send("Error:Pergjigja shume e gjate!")
                elif metoda[0].decode("UTF-8") =="PORT":
                    a="Pergjigja:Klienti eshte duke perdorur portin ".encode("UTF-8")+str(c[1]).encode("UTF-8")
                    if(sys.getsizeof(a)<=128):
                          s.sendto(a,c)
                    else:
                          conn.send("Error:Pergjigja shume e gjate!")
                elif metoda[0].decode("UTF-8") =="TIME":
                    currentTime = time.ctime(time.time()) + "\r"
                    if(sys.getsizeof(currentTime)<=128):
                          s.sendto(currentTime.encode('UTF-8'),c)
                    else:
                          s.sendto("Error:Pergjigja shume e gjate!",c)
                elif metoda[0].decode("UTF-8") =="HOST":
                    try:
                        a=gethostname().encode("UTF-8")
                        if(sys.getsizeof(a)<=128):
                            s.sendto(a,c)
                    else:
                          s.sendto("Error:Pergjigja shume e gjate!",c)
                    except errno:
                        s.sendto("Emri i klientit nuk dihet",c)
                elif metoda[0].decode("UTF-8")=="MOOD":
                      mood(s,c)
                elif metoda[0].decode("UTF-8")=="FUNFACT":
                      funfact(s,c)
                else:
                    s.sendto("Pergjigja:Kjo kerkese nuk mund te kryhet.Kerko dicka tjeter.".encode("UTF-8"),c)
            else: 
                if metoda[0]=="ZANORE":
                    gjatesia=len(metoda[1])
                    if str(data[7:]).startswith(" "):
                        s.sendto("Pergjigja:Formati i kerkeses eshte gabim.",c)
                    else:
                        teksti=data[7:]
                        zanore(teksti,s,c)
                elif metoda[0]=="KTHE":
                    teksti=data[4:]
                    kthePrapa(str(teksti),s,c)
                elif metoda[0]=="FUNC" and metoda[1].replace('.','',1).isdigit():
                    teksti=data[5:]
                    if " " in teksti:
                        s.sendto("Parametri hyres duhet te jete nje numer",c)
                    else:
                        gCf(float(teksti),s,c)
                elif metoda[0]=="PRINTO":
                    gjatesia=len(metoda[1])
                    if str(data[7:]).startswith(" "):
                        s.sendto("Pergjigja:Formati i kerkeses eshte gabim.",c)
                    else:
                        teksti=data[7:]                             
                        printo(teksti,s,c)
                elif metoda[0]=="CAESAR" :
                    plaintext=data[7:]
                    if plaintext.isdigit() :
                        s.sendto("Pergjigja:Keni dhene parameter te gabuar.",c)
                    else:
                        caesar(str(plaintext),s,c)
                elif metoda[0]=="YJET":
                    numri=int(metoda[1])
                    stars(str(numri),s,c)
                elif metoda[0]=="RECMOVIE":
                    teksti=data[9:]
                    recMovies(teksti,s,c)
                elif metoda[0]=="FIBO" and len(metoda)==2 and metoda[1].replace('.','',1).isdigit():
                    numri=int(data[4:])
                    fibonacci(numri,s,c)
                elif metoda[0]=="PITAGORA" and len(metoda)==3 and len(metoda[1])==1 and len(metoda[2])==1 and metoda[1].replace('.','',1).isdigit() and metoda[2].replace('.','',1).isdigit() :
                    k1=int(metoda[1])
                    k2=int(metoda[2])
                    pitagora(k1,k2,s,c)
                elif metoda[0]=="KONVERTO" and len(metoda)==3 and metoda[2].replace('.','',1).isdigit():    
                    vlera=metoda[2]              
                    if metoda[1]=="CelsiusToKelvin":
                        celsiusToKelvin(float(vlera),s,c)
                    elif metoda[1]=="CelsiusToFahrenheit":
                        celsiusToFahrenheit(float(vlera),s,c)
                    elif metoda[1]=="FahrenheitToCelsius":
                        fahrenheitToCelsius(float(vlera),s,c)
                    elif metoda[1]=="KelvinToFahrenheit":
                        kelvinToFahrenheit(float(vlera),s,c)
                    elif metoda[1]=="KelvinToCelsius":
                        kelvinToCelsius(float(vlera),s,c)
                    elif metoda[1]=="FahrenheitToKelvin":
                        fahrenheitToKelvin(float(vlera),s,c)
                    elif metoda[1]=="PoundToKilogram":
                        poundToKilogram(float(vlera),s,c)
                    elif metoda[1]=="KilogramToPound":
                        kilogramToPound(float(vlera),s,c)
                    else:
                        s.sendto("Pergjigja:Kjo kerkese nuk mund te shqyrohet.Kerko dicka tjeter.".encode("UTF-8"),c)
                elif metoda[0].decode("UTF-8")=="PAGA" and len(metoda)==2 and metoda[1].replace('.','',1).isdigit():
                    bruto=float(data[4:])
                    if bruto<0:
                        s.sendto("Vlere invalide e pages bruto.".encode("utf-8"),c)
                    else:
                        paga(bruto,s,c)
                elif metoda[0].decode("utf-8")=="FAKTORIEL" and len(metoda)==2 and metoda[1].replace('.','',1).isdigit():
                    numri=metoda[1]
                    if "." not in numri:
                        faktorieli(int(numri),s,c)
                    elif "." in numri:
                        numri=float(metoda[1])
                        s.sendto(str(round(math.gamma(numri+1),5)).encode("utf-8"),c)

                    else:
                        s.sendto("Pergjigja:Kjo kerkese nuk mund te shqyrohet.Kerko dicka tjeter.".encode("UTF-8"),c)
    except:
        pass

def main():
    while True:
        request, adresaDerguesit = serverSocket.recvfrom(2048)
        print("Kerkese e re nga: "+str(adresaDerguesit[0]))
        threading._start_new_thread(handleClient,(serverSocket,adresaDerguesit,request)) 
        
main()

serverSocket.close()


