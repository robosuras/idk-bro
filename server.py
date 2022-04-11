import socket
from threading import Thread
from requests import get
def recieve(c):
    while True:
        print("anon: " + c.recv(1024).decode())
def send(c):
    while True:
        c.send(input("").encode())

def start_threads():
    r_thread.start()
    s_thread.start()

def end_threads():
    s_thread.join()
    r_thread.join()
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    ip, port = str(get('https://api.ipify.org').content.decode('utf8')), 9001
    s.bind(("localhost", port))
    print("The server's ip address is %s and the port %s is being used" %(ip, port))
    s.listen()
    c, a = s.accept()
    with c:
        r_thread = Thread(target = recieve, args = (c,))
        s_thread = Thread(target = send, args = (c, ))
        
        

            
