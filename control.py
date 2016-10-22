# Control module
#from powermanager import powermanager

class control:
	def __init__(self):
		pass#self.sensors_module = powermanager()
	
	def status(self, **kwargs): # module
		if ('module' not in kwargs or 'function' not in kwargs):
			print 'Function status called wrong'
			return False
		
			
			
if __name__ == "__main__":
	cntrl = control()
	print 'Control module'
	cntrl.status(module = cntrl, function = 'temp')
	