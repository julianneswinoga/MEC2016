# Control module

import time, sys
from powermanager import PowerManager
#from sensors import Sensors

class Unbuffered(object): # http://stackoverflow.com/questions/107705/disable-output-buffering
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)
	   
class Control:
	moduleNames = ['controlBoard', 'powerManager']

	def __init__(self):
		self.powermanager_module = PowerManager()
		#self.sensors_module = Sensors()
	
	def status(self, **kwargs):
		if ('module' not in kwargs or 'function' not in kwargs or 'args' not in kwargs):
			print 'Function status called wrong'
			return False
		if (not kwargs['module'].getStatus()):
			return {'err': False, 'msg': 'Status of ' + kwargs['module'].__name__ + ' has failed'}
		
		return getattr(kwargs['module'], kwargs['function'])(*kwargs['args'])
		
	def getModuleLoad(self, moduleName):
		return self.status(module = self.powermanager_module, function = 'getLoad', args = [moduleName])
		
	def powerOverload(self):
		overloaded = []
		for moduleName in moduleNames:
			modulePower = self.getModuleLoad(moduleName)
			if (modulePower >= 2):
				overloaded.append({ 'name': moduleName, 'power': modulePower })
				
		if (len(overloaded) == 0):
			return False
		else:
			return overloaded
			
	def writeLog(self):
		return True

if __name__ == '__main__':
	sys.stdout = Unbuffered(sys.stdout)
	control_module = Control()
	print 'Control module start'
	
	print 'Power manager status:', control_module.status(module = control_module.powermanager_module, function = 'getStatus', args = [])
	
	while (True):
		powerStatus = control_module.powerOverload()
		if (powerStatus == False):
			print 'Working fine'
		else:
			print 'Overload!'
		
		control_module.writeLog()
		
		time.sleep(1)
	