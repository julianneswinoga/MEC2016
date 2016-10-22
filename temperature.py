class Temperature:
    
    def __init__(self):
        self.currentAirTemp=0
        self.currentWaterTemp=0
        self.updateTemperature()
    
    def getAirTemp(self):
        self.updateTemperature
        return self.currentAirTemp
    
    def getWaterTemp(self):
        self.updateTemperature
        return self.currentWaterTemp
    
    def updateTemperature(self):
        #Replace these assignments with sensor simulation
        self.currentAirTemp = 25.0
        self.currentWaterTemp = 18.7