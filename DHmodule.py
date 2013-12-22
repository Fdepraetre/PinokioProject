#import rotation
from math import *
import numpy as np

# Class for denavit-hartenberg model
# This class calculate the transformation between two referentials
class dh_model:

  # Initialise the denavit-Hartenberg Model
  def __init__(self):
     self.theta = 0.0
     self.a = 0.0
     self.d = 0.0
     self.alpha = 0.0

  # Set the model's value
  def set(self,new_theta,new_a,new_d,new_alpha):
     self.theta = new_theta * pi/180.0
     self.a = new_a
     self.d = new_d
     self.alpha = new_alpha * pi/180.0

     self.rotx = np.zeros(4)
     self.rotz = np.zeros(4)
     self.trans = np.zeros(4)
     self._0Ti = np.zeros(4)

  # Calculate the transform matrix with this dh-model
  def applyDH(self):
    # Appli the model and calculate the change matrix
    self._0Ti = np.mat(self.rotz)*np.mat(self.trans)*np.mat(self.rotx)

  def getPi(self,_0OT):
    self.apply(tmp)
    tmp2 = [[tmp[0,3]],[tmp[1,3]],[tmp[2,3]]]
    _0OT = mat(tmp2)
    return _0OT
     
  def rotZ(self):
    tmp = [[cos(self.theta) , -sin(self.theta) , 0                , 0]  ,
           [sin(self.theta) , cos(self.theta)  , 0                , 0]  ,
           [0               , 0                , 1                , 0]  ,
           [0               , 0                , 0                , 0] ]
    self.rotz = np.mat(tmp)
  def rotX(self):
    tmp = [[1               , 0                , 0                , 0]  ,
           [0               , cos(self.alpha)  , -sin(self.alpha) , 0]  ,
           [0               , sin(self.alpha)  , cos(self.alpha)  , 0]  ,
           [0               , 0                , 0                , 0] ]
    self.rotx = np.mat(tmp)
  def Trans(self):
    tmp = [[1 , 0 , 0 , self.a ] ,
           [0 , 1 , 0 , 0      ] ,
           [0 , 0 , 1 , self.d ] ,
           [0 , 0 , 0 , 0      ]]
    self.trans = np.mat(tmp)
