from accelerometer import Accelerometer
from temperature import Temperature
from barometer import Barometer
from gps import GPS
from lightsensor import LightSensor
import json

class Sensors:
	
	def __init__(self):
		self.accelerometer = Accelerometer()
		self.temperature = Temperature()
		self.barometer = Barometer()
		self.gps = GPS()
		self.light = LightSensor()
		
		self.testData = None
		self.testTime = 0
		self.loadTestData()
		
	def loadTestData(self):
		f = open('testData.json', 'rb')
		self.testData = json.load(f)['data']
		f.close()
	
	def getAccelerometer(self):
		if (self.testData is None):
			return self.accelerometer.getAccelData()
		else:
			self.testTime += 1
			return self.testData[self.testTime]['acc']
	
	def getWaterTemperature(self):
		if (self.testData is None):
			return self.temperature.getWaterTemp()
		else:
			return self.testData[self.testTime]['tmp']
	
	def getAirTemperature(self):
		if (self.testData is None):
			return self.temperature.getAirTemp()
		else:
			return self.testData[self.testTime]['tmp']
	
	def getBarometer(self):
		if (self.testData is None):
			return self.barometer.getPressure()
		else:
			return self.testData[self.testTime]['baro']

	def getGPS(self):
		if (self.testData is None):
			return self.gps.getGPSData()
		else:
			return [self.testData[self.testTime]['longitude'], self.testData[self.testTime]['latitude']]

	def getLightSensor(self):
		if (self.testData is None):
			return self.light.getLightData()
		else:
			return self.testData[self.testTime]['light']

	def getStatus(self):
		if (self.testData is None):
			return True
		else:
			return self.testData[self.testTime]['tmp']


