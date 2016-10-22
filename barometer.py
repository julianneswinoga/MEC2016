class Barometer:
    
    def __init__(self):
        self.currentPressure=0
        self.updatePressure()
        
    def getPressure(self):
        self.updatePressure()
        return self.currentPressure
    
    def updatePressure(self):
        #Replace this assignment with sensor simulation
        self.currentPressure = 101.4