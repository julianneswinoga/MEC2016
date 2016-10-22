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
        self.accelerometer = accelerometer.getAccelData()
        self.waterTemperature = temperature.getWaterTemp()
        self.airTemperature = temperature.getAirTemp()
        self.barometer = barometer.getPressure()
    #end
