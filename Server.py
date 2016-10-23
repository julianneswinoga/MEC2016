import socket
import threading
import sys

class Server:
    def __init__(self, gsm):
        gsm = gsm
        HOST = ''
        PORT = 8888
        threading.Thread(target=self.listen, kwargs={'HOST': HOST, 'PORT': PORT, 'gsm': gsm}).start()

    def listen(self, **kwargs):
        # Datagram (udp) socket
        try :
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error, msg :
            print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit(1)
         
        # Bind socket to local host and port
        try:
            s.bind((kwargs['HOST'], kwargs['PORT']))
        except socket.error , msg:
            pass
             
        #now keep talking with the client
        while 1:
            # receive data from client (data, addr)
            d = s.recvfrom(1024)
            data = d[0]
            addr = d[1]
             
            kwargs['gsm'].addToBuffer(self.data)
