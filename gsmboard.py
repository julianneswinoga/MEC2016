class GsmBoard: #gsm board module
    def __init__(self): #initialization
        self.status = True
        
        self.buffer = [] #internal command buffer
        
    def getStatus(self): #get the component status
        return self.status
        
    def isPending(self): #check if there is an element in the buffer
        return bool(len(self.buffer))        
        
    def latestMessage(self): #get the oldest element in the buffer
        return self.buffer.pop(0)
        
    def addToBuffer(self, element): #add to the buffer
        self.buffer.append(element)