from Server import Server
import socket

class GsmBoard: #gsm board module
    def __init__(self): #initialization
        self.status = True
        
        self.buffer = [] #internal command buffer

        self.server = Server(self)

        self.PORT = 8888;
        
    def getStatus(self): #get the component status
        return self.status
        
    def send(self, host, msg):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error:
            print 'Failed to create socket'
            sys.exit(1)
         
        try :
            #Set the whole string
            s.sendto(msg, (host, self.PORT))
        except socket.error, msg:
            print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit(1)

    def isPending(self): #check if there is an element in the buffer
        return bool(len(self.buffer))        
        
    def latestMessage(self): #get the oldest element in the buffer
        return self.buffer.pop(0)
        
    def func(self):
        print('hello')

    def addToBuffer(self, element): #add to the buffer
        print 'adding to buffer:'
        self.buffer.append(element)
