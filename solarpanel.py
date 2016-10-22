import random

class SolarPanel:
    def __init__(self):
        self.status = True
        
        self.solarVoltage = 0
        
        return None
    
    def getStatus(self):
        return self.status
    
    def getVoltage(self):
        self.solarVoltage = 10+4*random.random()
        return self.solarVoltage