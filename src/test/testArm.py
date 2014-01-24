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

  moveAndPlot(motorControler, plotter, [["bottom",150],["mid",220],["head",125],["top",75],["bowl",45]])
  time.sleep(1)
  moveAndPlot(motorControler, plotter, [["bottom",150],["mid",180],["head",175],["top",75],["bowl",135]])
  time.sleep(1)
  moveAndPlot(motorControler, plotter, [["bottom",150],["mid",180],["head",125],["top",190],["bowl",45]])
  time.sleep(1)
