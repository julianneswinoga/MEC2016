from accelerometer import Accelerometer
from temperature import Temperature
from barometer import Barometer
from gps import GPS
from lightsensor import LightSensor

class Sensors:
    
    def __init__(self):
        self.accelerometer = Accelerometer()
        self.temperature = Temperature()
        self.barometer = Barometer()
        self.gps = GPS()
        self.light = LightSensor()
    
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

    def getLightSensor(self):
        return self.light.getLightData()

    def getStatus(self):
        return true


