from accelerometer import Accelerometer
from temperature import Temperature
from barometer import Barometer

class Sensors:
    
    def __init__(self):
        self.accelerometer = Accelerometer()
        self.temperature = Temperature()
        self.barometer = Barometer()
    
    def getAccelerometer(self):
        return self.accelerometer.getAccelData()
    
    def getWaterTemperature(self):
        return self.temperature.getWaterTemp()
    
    def getAirTemperature(self):
        return self.temperature.getAirTemp()
    
    def getBarometer(self):
        return self.barometer.getPressure()
    #end


