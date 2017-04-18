import socket

host = "192.168.0.37"
port = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def info():
            info="Metodat qe mund te implementohen nga serveri jane:\n1.IP - Tregon IP-n tuaj.\n2.PORT\n3.ZANORE - Kthen zanoret ne fjalin qe ju e jepni (ZANORE input_text)\n4.PRINTO - Printon fjalen qe ju e jepni (PRINTO input_text)\n5.HOST - Emri i Hostuesit.\n6.TIME\n7.KENO - 20 numra te rastesishem.\n8.FAKTORIEL\n9.KONVERTO - Konvertime te ndryshme, klikoni KONVERTO per me shume.\n10.MOOD\n11.PAGA\n12.FUNC\n13.KTHE\n14.CAESAR\nFIBO\nPITAGORA\nFUNFACT\n."     
            print(info)

sock.connect((host,port))

i=1
while True:
    
    data = input("Kerkesa: ")
    data = data.lstrip()
    data = data.rstrip()
    metoda = data.split(" ")
    if data == "": 
        if (i % 3 == 0):
            print("Shtypni help per ndihme")
        i = i + 1
        continue
    elif ( data == "keno" or data == "ip" ):
        print("Ju lutem shkruani funksionet me shkronja te medha!")
        continue
    #elif ( data == "KENO" or data == "FUNFACT" or data == "INFO" or data == "MOOD" or (metoda[0] == "KONVERTO" and len(metoda) > 1) or (metoda[0] == "RECMOVIE" and len(metoda) > 1) or (metoda[0]=="KTHE" and len(metoda)>1) or ( metoda[0]=="FIBO" and len(metoda) >1) or  (metoda[0]=="YJET" and len(metoda) > 1) or  data=="CAESAR" or data=="PITAGORA" or (metoda[0]=="PAGA" and len(metoda)>1) or (metoda[0]=="FAKTORIEL" and len(metoda)>1) or (metoda[0]== "ZANORE" and len(metoda)>1) ):
    elif ( (data == "KENO" or data == "FUNFACT" or data == "IP" or data == "INFO" or data == "TIME" or data == "HOST" or data == "MOOD" ) or (( metoda[0] =="ZANORE" or metoda[0] == "RECMOVIE" or metoda[0] == "KTHE" or metoda[0] == "CAESAR" or metoda[0] == "YJET" or metoda[0] == "FIBO" or metoda[0] == "PITAGORA" or metoda[0] == "KONVERTO" or metoda[0] == "PAGA" or metoda[0] == "FAKTORIEL" ) and (len(metoda)>1))):
        sock.send(data.encode("utf-8"))
        print("Pergjigja: ", sock.recv(1024).decode("utf-8"))
    elif ( data == "IP" or data == "PORT" or data == "ZANORE" or data == "HOST" or data == "TIME" ):
        sock.send(data.encode("utf-8"))
        print("Pergjigja: ", sock.recv(128).decode("utf-8"))
    elif ( data == "help" or data == "HELP"):
        info()
    elif ( data == "KONVERTO" and len(metoda) == 1):
        print("KONVERTO opsionet:\n===================\nKONVERTO     ")
    elif ( data == "FIBO" and len(metoda) == 1):
        print("FIBO <input_number>")
    else:    
        continue

