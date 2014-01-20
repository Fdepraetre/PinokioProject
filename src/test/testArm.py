import sys
sys.path.insert(0,"../motorControl/")
import motorControl
import plot
sys.path.insert(0, "../settings/")
import settings

motorSettings = settings.motorSettings()

motorControler = motorControl.MotorControl(motorSettings.get())
motorControler.setAllSpeed(100)
plotter = plot.Ploting()
initTime = time.time()
i = 0

while True: 
#   key = raw_input("Do you want to move or plot?" + "\n\r" + "\t - (p) plot \r\n \t - (m) move \r\n")
#      if key == 'm':
  if i < 10:
    # First tests
    motorControler.setAllMotorsByName([["bottom",140],["middle",230],["head",250],["top",150],["bowl",200]])
    out = motorControler.readAllMotors()
    plotter.addNewVal(out,time.time()-initTime)
    # Second tests
    motorControler.setAllMotorsByName([["bottom",160],["middle",160],["head",150],["top",100],["bowl",300]])
    out = motorControler.readAllMotors()
    plotter.addNewVal(out,time.time() - initTime)
    # Third tests
    motorControler.setAllMotorsByName([["bottom",140],["middle",160],["head",150],["top",200],["bowl",300]])
    out = motorControler.readAllMotors()
    plotter.addNewVal(out,time.time() - initTime)
    i += 1
  # elif key == 'p':
  else:
    plotter.plot()
  break

