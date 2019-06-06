import socket

HOST = socket.gethostname()
PORT = 9999

serversocket= socket.socket(socket.AF_INET , socket.SOCK_STREAM)
serversocket.bind((HOST,PORT))
serversocket.listen(1)
clientsocket,addr = serversocket.accept()
print("Connected!")
welcommsg = "Type number 0-2 if you want to know about vulnerability."
clientsocket.send(welcommsg.encode("UTF-8"))

while True:
    data = clientsocket.recv(1024).decode("UTF-8")
    
    if data in ["0","1","2"] :
        print(str(addr) + " wants to know the name of vulnerability " + data)
    
    if data == "0":
        msg = "Heartbleed"
    elif data == "1":
        msg = "POODLE"
    elif data == "2":
        msg = "GHOST"
    elif data == "q":
        break
    else:
        msg = "Type number 0-2"
        
    clientsocket.send(msg.encode("UTF-8"))
    
clientsocket.close()
