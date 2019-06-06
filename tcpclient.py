import socket

HOST = socket.gethostname()
PORT = 9999

s= socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.connect((HOST , PORT))
print("Connected!")

while True:
    data = s.recv(1024)
    print(data.decode("UTF-8"))
    data = input('>>> ')
    s.send(data.encode("UTF-8"))
    if data == "q" :
        break
s.close()
