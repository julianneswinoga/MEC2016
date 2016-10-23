# Control module

import time, sys
from powermanager import PowerManager
from sensors import Sensors
from gsmboard import GsmBoard
from database import Database

class Unbuffered(object): # http://stackoverflow.com/questions/107705/disable-output-buffering
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)
	   
class ControlBoard:
	def __init__(self):
		self.powerBoard = PowerManager()
		self.sensorBoard = Sensors()
		self.gsmBoard = GsmBoard()
		self.logging = Database()
		
		self.moduleNames = ['controlBoard', 'powerBoard', 'sensorBoard', 'logging', 'gsmBoard', 'radioBoard']
		self.logTime = 5
		self.lastLogTime = 0
		self.sensorData = {'longitude': None,'latitude': None,'light': None, 'acc': None, 'tmp': None, 'baro': None}
	
	def status(self, **kwargs):
		if ('module' not in kwargs or 'function' not in kwargs or 'args' not in kwargs):
			print 'Function status called wrong'
			return False
		if (False and not kwargs['module'].getStatus()):
			return {'err': False, 'msg': 'Status of ' + kwargs['module'].__name__ + ' has failed'}
		
		return getattr(kwargs['module'], kwargs['function'])(*kwargs['args'])
	
	def isPendingGSMMessage(self):
		return self.status(module = self.gsmBoard, function = 'isPending', args = [])
	
	def GSMPendingMessage(self):
		return self.status(module = self.gsmBoard, function = 'latestMessage', args = [])
	
	def handleGSMCommand(self, command):
		if (command['cmdName'] == 'setLogTime'):
			self.logTime = command['value']
		elif (command['cmdName'] == 'getStatus'):
			self.sendGSMMsg(command['id'], {'cmdName': STATUS, 'value': 'ME 2 THANKS' })
			
		return True
	
	def updateSensors(self):
		self.sensorData['longitude'] = self.status(module = self.sensorBoard, function = 'getGPS', args = [])[0]
		self.sensorData['latitude'] = self.status(module = self.sensorBoard, function = 'getGPS', args = [])[1]
		self.sensorData['light'] = self.status(module = self.sensorBoard, function = 'getLightSensor', args = [])
		self.sensorData['acc'] = self.status(module = self.sensorBoard, function = 'getAccelerometer', args = [])
		self.sensorData['tmp'] = self.status(module = self.sensorBoard, function = 'getAirTemperature', args = [])
		self.sensorData['baro'] = self.status(module = self.sensorBoard, function = 'getBarometer', args = [])
		
	def sendGSMMsg(self, id, msg):
		return self.gsmBoard.sendMessage(id, msg)
	
	def getModuleLoad(self, moduleName):
		return self.status(module = self.powerBoard, function = 'getLoad', args = [moduleName])
		
	def powerOverload(self):
		overloaded = []
		for moduleName in self.moduleNames:
			modulePower = self.getModuleLoad(moduleName)
			if (modulePower >= 2):
				overloaded.append({ 'name': moduleName, 'power': modulePower })
				
		if (len(overloaded) == 0):
			return False
		else:
			return overloaded
	
	def writeDB(self, data):
		return self.status(module = self.logging, function = 'insert', args = [data])
	
	def writeLog(self, data):
		currTime = time.time()
		self.writeDB(data)
		self.lastLogTime = currTime
		return True

if __name__ == '__main__':
	sys.stdout = Unbuffered(sys.stdout)
	control = ControlBoard()
	print 'Control module start'
	
	print 'Power manager status:', control.status(module = control.powerBoard, function = 'getStatus', args = [])
	
	while (True):
		control.updateSensors()
		if (control.isPendingGSMMessage() is not False):
			control.handleMessage(control.GSMPendingMessage())
	
		powerStatus = control.powerOverload()
		if (powerStatus == False):
			print 'Working fine'
		else:
			print 'Overload!'
		
		if (time.time() - control.lastLogTime > control.logTime):
			control.writeLog(control.sensorData)
		
		time.sleep(1)
	