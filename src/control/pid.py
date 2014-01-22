import time


class PIDcontroler:

  def __init__(self,proportionalCoeff,integralCoeff,derivateCoeff,maxIntegral=0,maxDerivate=0,length=1):

    self.proportionalCoeff = proportionalCoeff
    self.integralCoeff     = integralCoeff
    self.derivateCoeff     = derivateCoeff
    self.maxIntegral       = maxIntegral
    self.maxDerivate       = maxDerivate
    self.lastIn            = []
    self.integralValue     = []
    self.timeInit = time.time()

    for i in range(length):
      self.lastIn            += [0]
      self.integralValue     += [0]

  def update(self,reference,returnValue):

    derivate = []
    error    = []
    command  = []
    
    timeElapsed = time.time() - self.timeInit

    for i in range(len(reference)):
      derivate += [0]
      error    += [0]
      command  += [0]

      error[i] += reference[i] - returnValue[i]
      self.integralValue[i] += error[i] * timeElapsed
      if self.maxIntegral !=0:
        max(self.integralValue[i],self.maxIntegral)

      derivate[i] = error[i] - self.lastIn[i] / timeElapsed
      if self.maxDerivate != 0:
        max(derivate[i],self.maxDerivate)

      command[i] = error[i] * self.proportionalCoeff + self.integralValue[i] * self.integralCoeff + derivate[i] * self.derivateCoeff

      print "error " + str(error)
      print "intValue " +str(self.integralValue)

    self.lastIn = error

    return command


  time.sleep(2)
if (__name__)=='__main__':


  pid = PIDcontroler(2,0,0,maxIntegral= 500,length=1)
  positionMesured = [[10],[40],[70],[140],[149],[149],[149],[149],[149]]

  outPid = []
#  time.sleep(0.5)
  outPid = pid.update([150],[2])
  print outPid



  for i in range(len(positionMesured)):
      
      outPid = pid.update([150],positionMesured[i])
      time.sleep(0.5)
      print "outPid" + str(outPid) + "\n"



