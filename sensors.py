from accelerometer import Accelerometer
from temperature import Temperature
from barometer import Barometer
from gps import GPS

class Sensors:
    
    def __init__(self):
        self.accelerometer = Accelerometer()
        self.temperature = Temperature()
        self.barometer = Barometer()
        self.gps = GPS()
    
    def getAccelerometer(self):
        return self.accelerometer.getAccelData()
    
    def getWaterTemperature(self):
        return self.temperature.getWaterTemp()
    
    def getAirTemperature(self):
        return self.temperature.getAirTemp()
    
    def getBarometer(self):
        return self.barometer.getPressure()

    def getGPS(self):
        return self.gps.getGPSData()

a=Sensors()


