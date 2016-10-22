from battery import Battery as InternalBattery #Battery

class PowerManager: #Power Manager Class
    def __init__(self): #Initialization
        self.status = True
        self.battery = InternalBattery() #Initializing the battery component
        self.poweredComponents = {
                                    "controlBoard":1,
                                    "powerManager":1
                                 } #Powered Components
        return None
    
    def getStatus(self):
        return self.status
        
    def updateLoad(self):
        for i in self.poweredComponents: #For every running component, measure the load and add to the stored value. simulated to 1
            self.poweredComponents[i] = 1

    def getLoad(self):
        self.updateLoad()
        return self.poweredComponents
        
    def getVoltage(self):
        if self.battery.getStatus():
            return self.battery.getVoltage()
        else:
            return 0
        
A = PowerManager()