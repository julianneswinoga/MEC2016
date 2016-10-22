import accelerometer.py
import temperature.py
import barometer.py

class Sensors:
    
    def __init__(self):
        self.accelerometer
        self.waterTemperature
        self.airTemperature
        self.barometer
    
    def readSensors(self):
        #Read values into local variables from individual sensor classes
        self.accelerometer = accelerometer.getAccelData()
        self.waterTemperature = temperature.getWaterTemp()
        self.airTemperature = temperature.getAirTemp()
        self.barometer = barometer.getPressure()
    
    def getAccelerometer(self):
        return accelerometer.getAccelData()
    
    def getWaterTemperature(self):
        return temperature.getWaterTemp()
    
    def getAirTemperature(self):
        return temperature.getAirTemp()
    
    def getBarometer(self):
        return barometer.getPressre()
    #end
