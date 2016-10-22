class LightSensor:

	def __init__(self):
		self.lightsensor = 0
		self.updateLightData()

	def getLightData(self):
		self.updateLightData()
		return self.lightsensor

	def updateLightData(self):
		self.lightsensor = 35
	def getStatus(self):
        return true