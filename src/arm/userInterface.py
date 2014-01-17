import arm
import readline

class command :
	def __init__(self, cmd):
		s = cmd.split();
		self.cmdName = s[0]
		self.cmdArg = s[1:]

class userTerminal :
	def __init__(self):
		pass

	def start(self):
		isRunning = True
		while isRunning :
			try:
				cmd = command(raw_input('$ '))
			except:
				 # And EOF may have been sent, we exit cleanly
				print("")
				isRunning = False
			
			print cmd.cmdName 
			print cmd.cmdArg
 
			if cmd.cmdName == "q":
				isRunning = False	
			elif cmd.cmdName == "setById":
				pass
			elif cmd.cmdName == "setByName":
				pass

ui = userTerminal()
ui.start()
