import math
import numpy as np
import sympy as sp
import sys
import trHomogene
sys.path.insert(0,"../settings/")
import settings

class MGD:
  def __init__(self):
    self._0Tf = None
    pass
  
  def getPositionEffector(self):
    pass

  def getTransMatrix(self):
    return self._0Tf

class lampMGD(MGD):
  def __init__(self):
    modelSettings = settings.ModelSettings().get()

    theta1 = sp.symbols('theta1')
    theta2 = sp.symbols('theta2')
    theta3 = sp.symbols('theta3')
    theta4 = sp.symbols('theta4')
    theta5 = sp.symbols('theta5')

    d1     = modelSettings['d1']
    alpha1 = math.radians(-90)
    a2     = modelSettings['a2']
    a3     = modelSettings['a3']
    alpha4 = math.radians(-90)


    self._0T1 = trHomogene.dhMatrix(theta1 , 0  , d1 , alpha1) 
    self._1T2 = trHomogene.dhMatrix(theta2 , a2 , 0  , 0) 
    self._2T3 = trHomogene.dhMatrix(theta3 , a3 , 0  , 0) 
    self._3T4 = trHomogene.dhMatrix(theta4 , 0  , 0  , alpha4) 
    self._4Tf = trHomogene.dhMatrix(theta5 , 0  , 0  , 0) 

    self._0Tf = self._0T1 * self._1T2 * self._2T3 * self._3T4 * self._4Tf 

