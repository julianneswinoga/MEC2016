class GPS:

	def __init__(self):
		self.coordN = 0.000
		self.coordW = 0.000
	
	def getGPSData(self):
		self.updateGPSData()
		g = []
		g.append(self.coordN)
		g.append(self.coordW)
		return g

	def updateGPSData(self):
		self.coordN = 40.446
		self.coordW = 79.982

	def getStatus(self):
        return true
