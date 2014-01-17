import arm
import readline
import settings

class command :
  def __init__(self, cmd):
    s = cmd.split();
    self.cmdName = s[0]
    self.cmdArg = []
    argList = s[1:]
    for arg in argList :
      pair = arg.split('=')
      self.cmdArg += [[pair[0],int(pair[1])]]

class userTerminal :
  def __init__(self,settingPath=None,debug=False):
    motorSettings = settings.motorSettings(settingPath)
    self.motorControl = arm.MotorControl(motorSettings.get())       

  def start(self):
    isRunning = True
    while isRunning :
      try:
        cmd = command(raw_input('$ '))
        if cmd.cmdName == "q":
          isRunning = False   
        elif cmd.cmdName == "setById" or cmd.cmdName == "sbi":
          self.motorControl.setAllMotors(cmd.cmdArg)  
        elif cmd.cmdName == "setByName" or cmd.cmdName == "sbn":
          self.motorControl.setAllMotorsByName(cmd.cmdArg)    

      except:
        # And EOF may have been sent, we exit cleanly
        print("")
        isRunning = False
            
if __name__ == "__main__":
  ui = userTerminal()
  ui.start()
