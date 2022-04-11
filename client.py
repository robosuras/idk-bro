import socket
from threading import Thread

def recieve(c):
    while True:
        print("anon: "+c.recv(1024).decode())
def send(c):
    while True:
        c.send(input("").encode())

def start_threads():
    r_thread.start()
    s_thread.start()

def end_threads():
    r_thread.join()
    s_thread.join()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("localhost", 9001))
    s.send(b"Hello")
    r_thread = Thread(target = recieve, args = (s,))
    s_thread = Thread(target = send, args = (s, ))
    start_threads()
    end_threads()
        