import random #for simulation

class SolarPanel: #solar panel component/module
    def __init__(self):
        self.status = True #set the status
        
        self.solarVoltage = 18*random.random() #set the voltage 
        
        return None
    
    def getStatus(self): #get status function for returning operational status
        return self.status
    
    def getVoltage(self): #get the current supplied voltage
        self.solarVoltage = 18*random.random()
        return self.solarVoltage