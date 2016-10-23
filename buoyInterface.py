import sys, webbrowser

try:
	import pygtk
	pygtk.require('2.0')
except:
	pass
try:
	import gtk
	import gtk.glade
except:
	print('GTK not available')
	sys.exit(1)
	
class BuoyWindow:
	def __init__(self):
		self.gladefile = "BuoyGUI.glade"
		self.builder = gtk.Builder()
		self.builder.add_from_file(self.gladefile)
		self.builder.connect_signals(self)
		self.window = self.builder.get_object("window1")
		self.window.show()
		settings = gtk.settings_get_default()
		
	def on_window_main_destroy(self, object, data=None):
		gtk.main_quit()
		
if __name__ == "__main__":
	#main = BuoyWindow()
	#gtk.main()

	print "Starting...\n"

	knownIPs = ["172.17.52.75"]

	while True:
		ip = knownIPs[int(raw_input("Enter ID: ")]
		command = raw_input("Enter command: ")
		value = 0    
		try:
			value = raw_input("Enter value: ")
		except:
			value = 0
		print ip, command, value,"\n"