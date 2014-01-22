import sys
import readline
sys.path.insert(0, "../settings/")
import settings
sys.path.insert(0, "../control/")
import motorControl

class command :
  def __init__(self, cmd):
    s = cmd.split();
    self.cmdName = s[0]
    self.cmdArg = s[1:]

  def splitArg(self):
    argList = []
    for arg in self.cmdArg :
      pair = arg.split('=')
      argList += [[pair[0],int(pair[1])]]
    self.cmdArg = argList

class commandLineInterface :
  def __init__(self,settingPath=None,debug=False):
    if settingPath != None :
      motorSettings = settings.MotorSettings(settingPath)
    else :
      motorSettings = settings.MotorSettings()
    self.motorControl = motorControl.MotorControl(motorSettings.get())       

  def start(self):
    isRunning = True
    while isRunning :
      try:
        cmd = command(raw_input('$ '))
        if cmd.cmdName == "q":
          isRunning = False   
        elif cmd.cmdName == "setById" or cmd.cmdName == "sbi":
          cmd.splitArg()
          self.motorControl.setMotorsById(cmd.cmdArg)  
        elif cmd.cmdName == "setByName" or cmd.cmdName == "sbn":
          cmd.splitArg()
          self.motorControl.setMotorsByName(cmd.cmdArg)    
        elif cmd.cmdName == "setVelocity" or cmd.cmdName == "sv":
          self.motorControl.setAllSpeed(int(cmd.cmdArg[0]))
        elif cmd.cmdName == "read" or cmd.cmdName == "r":
          print self.motorControl.readAllMotors()

      except:
        # And EOF may have been sent, we exit cleanly
        print("")
        isRunning = False
            
