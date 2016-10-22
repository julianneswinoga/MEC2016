from battery import Battery #Battery
from solarpanel import SolarPanel #Solar Panel

import random #for simulation

class PowerManager: #Power Manager Class
    def __init__(self): #Initialization
        self.status = True
        
        self.battery = Battery() #Initializing the battery component
        self.solarPanel = SolarPanel() #Initializing the solar power component        
        
        self.poweredComponents = {
                                    "controlBoard":1,
                                    "powerBoard":1,
                                    "light":1,
                                    "acc":1,
                                    "tmp":1,
                                    "baro":1,
                                    "sensorBoard":1,
                                    "logging":1,
                                    "radioBoard":1,
                                    "gsmBoard":0,
                                    "view":0
                                 } #Powered Components
        return None
    
    def getStatus(self): #return the current status of the power manager
        return self.status
        
    def updateLoad(self): #update the component loads
        for i in self.poweredComponents: #For every running component, measure the load and add to the stored value. simulated to 1
            self.poweredComponents[i] = 0.9+0.2*random.random()

    def getLoad(self, component): #get the load of a specific component
        self.updateLoad()
        return self.poweredComponents[component]
        
    def getVoltage(self): #get the current system voltage
        if self.battery.getStatus():
            return self.battery.getVoltage()
        else:
            return 0
            
    def getSolarVoltage(self): #get the voltage supplied by the solar panel
        if self.solarPanel.getStatus():
            return self.solarPanel.getVoltage()
        else:
            return 0