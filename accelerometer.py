class Accelerometer:
    
    def __init__(self):
        self.magnitude=0
        self.updateAccelData()
    
    def getAccelData(self):
        self.updateAccelData()
        return self.magnitude
    
    def updateAccelData(self):
        #Replace this value with sensor simulation
        self.magnitude = 0.25;