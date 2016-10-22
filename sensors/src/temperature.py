class Temperature:
    
    def __init__(self):
        self.currentAirTemp
        self.currentWaterTemp
    
    def getAirTemp(self):
        return self.currentAirTemp
    
    def getWaterTemp(self):
        return self.currentWaterTemp
    
    def updateTemperature(self):
        self.currentAirTemp = 25.0
        self.currentWaterTemp = 18.7