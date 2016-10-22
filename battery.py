import random #for simulation

class Battery: #battery
    def __init__(self): #battey initialization
        self.batteryVoltage = 11.5+random.random()
        return None
        
    def getStatus(self): #return the status
        return True        
        
    def getVoltage(self): #return the battery voltage
        self.batteryVoltage = 11.5+random.random()
        return self.batteryVoltage