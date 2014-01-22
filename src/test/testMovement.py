import sys
sys.path.insert(0,"../control/")
import motorControl
sys.path.insert(0, "../settings/")
import settings
import time
import numpy as np

motorSettings = settings.MotorSettings()
motorControler = motorControl.MotorControl(motorSettings.get())
motorControler.setAllSpeed(10,False)

motorName = "head"
initValue = 100
finalValue = 200
step = 10
stepTime = 0.1

#Go to initial position
motorControler.setMotorsByName([[motorName,initValue]])
time.sleep(5)
print ""
print "Init ok"
print "position : " + str(initValue)

for i in np.arange(0,step,1):
  position = initValue + (finalValue - initValue) * i/step 
  motorControler.setMotorsByName([[motorName,position]])
  print ""
  print "go to position : " + str(position)
  time.sleep(stepTime)
