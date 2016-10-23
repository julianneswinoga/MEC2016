from battery import Battery #Battery
from solarpanel import SolarPanel #Solar Panel

import random, json #for simulation

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
								 } #Powered Components
		self.testData = None
		self.testTime = 0
		self.loadTestData()
		return None
	
	def loadTestData(self):
		f = open('testData.json', 'rb')
		self.testData = json.load(f)['data']
		f.close()
	
	def getStatus(self): #return the current status of the power manager
		self.testTime += 1
		return self.status
		
	def updateLoad(self): #update the component loads
		for i in self.poweredComponents: #For every running component, measure the load and add to the stored value. simulated to 1
			self.poweredComponents[i] = 0.9+0.2*random.random()

	def getLoad(self, component): #get the load of a specific component
		if (self.testData is None):
			self.updateLoad()
			return self.poweredComponents[component]
		else:
			print "THING:",self.testTime,self.testData[self.testTime]['load']
			return self.testData[self.testTime]['load']
		
	def getVoltage(self): #get the current system voltage
		if (self.testData is None):
			if self.battery.getStatus():
				return self.battery.getVoltage()
			else:
				return 0
		else:
			self.testTime += 1
			return self.testData[self.testTime]['battery']
			
	def getSolarVoltage(self): #get the voltage supplied by the solar panel
		if self.solarPanel.getStatus():
			return self.solarPanel.getVoltage()
		else:
			return 0