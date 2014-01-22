import sys
sys.path.insert(0,"../control/")
import motorControl
import plot
sys.path.insert(0, "../settings/")
import settings
import time
import cv2
import select

def moveAndPlot(motorControler, plotter, values):
  motorControler.setMotorsByName(values)
  out = motorControler.readAllMotors()
  plotter.addNewVal(out,time.time()-initTime)


motorSettings = settings.MotorSettings()

motorControler = motorControl.MotorControl(motorSettings.get())
motorControler.setAllSpeed(100)
plotter = plot.Ploting()
initTime = time.time()

exit = False
while not exit: 
  if select.select([sys.stdin],[],[],0) == ([sys.stdin], [], []):
    cmd = sys.stdin.read(1)
    if cmd == 'q': 
      exit = True
    elif cmd == 'p':
      plotter.plot()

  moveAndPlot(motorControler, plotter, [["bottom",100],["middle",230],["head",250],["top",150],["bowl",200]])
  time.sleep(1)
  moveAndPlot(motorControler, plotter, [["bottom",160],["middle",160],["head",150],["top",100],["bowl",300]])
  time.sleep(1)
  moveAndPlot(motorControler, plotter, [["bottom",100],["middle",160],["head",150],["top",200],["bowl",300]])
  time.sleep(1)
