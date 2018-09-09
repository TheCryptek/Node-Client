import socket

class Client():
    def __init__(self,Address=('198.37.231.220',25565)):
        self.s = socket.socket()
        self.s.connect(Address)

c = Client()

