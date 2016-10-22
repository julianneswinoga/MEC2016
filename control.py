# Control module
import sys
from powermanager import powermanager

class Control:
	def __init__(self):
		self.sensors_module = powermanager()
	
	def status(self, **kwargs): # module
		if ('module' not in kwargs or 'function' not in kwargs or 'args' not in kwargs):
			print 'Function status called wrong'
			return False
		if (not kwargs['module'].getStatus()):
			return {'err': False, 'msg': 'Status of ' + kwargs['module'].__name__ + ' has failed'}
		
		return getattr(kwargs['module'], kwargs['function'])(*kwargs['args'])
			
			
if __name__ == "__main__":
	cntrl = Control()
	print 'Control module start'
	print cntrl.status(module = cntrl.sensors_module, function = 'getStatus', args = [])
	