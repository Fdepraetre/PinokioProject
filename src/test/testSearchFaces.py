import sys
sys.path.insert(0,"../behavior/")
import searchFaces
sys.path.insert(0,"../control/")
import motorControl
sys.path.insert(0,"../computerVision/")
import FaceDetection
sys.path.insert(0,"../settings/")
import settings


motorSettings = settings.MotorSettings()
motorControler = motorControl.MotorControl(motorSettings.get())
faceStream = FaceDetection.FaceStream(1)

faceSearchBehavior = searchFaces.FaceSearch(motorControler,faceStream,60)
faceSearchBehavior.start()

