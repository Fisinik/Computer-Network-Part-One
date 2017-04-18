from socket import *
import sys
host='localhost'
port=9000

clientSocket=socket(AF_INET,SOCK_DGRAM)

whileTrue:
  tekst=raw_input('Kerkesa:').encode('utf-8')
  
  if tekst=="":
    print('Shtypni dicka')
    continue
    
  elif " " in tekst:
      if (tekst.endswith(" ") or tekst.startswith(" ")) and not tekst.isspace():
          tekst=tekst.rstrip()
          tekst=tekst.lstrip()
          clientSocket.sendto(tekst.encdoe('utf-8'),(host,port))
      else:
          clientSocket.sendto(tekst.encode('utf-8'),(host,port))
          
  elif sys.getsizeof(tekst)>128:
      print("Pergjigja:Kerkesa eshte me e gjate se 128 bytes. Kerkoni dicka tjeter")
      continue
  else:
      clientSocket.sendto(tekst.encdoe('utf-8'),(host,port))
  data, add=clientSocket.recvfrom(2048)
  print(data.decode('utf-8'))
           
clientSocket.close()
 
