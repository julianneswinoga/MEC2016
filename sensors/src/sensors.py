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
        
        #Format output to control in string var temp
        temp = ("Accelerometer: "+self.accelerometer+"G's"
                +"\nWater Temperature: "+self.waterTemperature+"degC"
                +"\nAir Temperature: "+self.airTemperature+"degC"
                +"\nBarometric Pressure: "+self.barometer+"kPa")
        return temp;
    #end
