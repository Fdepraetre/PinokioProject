import math
import numpy as np
import sympy as sp

def rotX(theta):
  return np.mat( [[1 , 0             , 0              , 0],
                  [0 , sp.cos(theta) , -sp.sin(theta) , 0],
                  [0 , sp.sin(theta) , sp.cos(theta)  , 0],
                  [0 , 0             , 0              , 1]])

def rotY(theta):
  return np.mat( [[sp.cos(theta)  , 0 , sp.sin(theta) , 0],
                  [0              , 1 , 0             , 0],
                  [-sp.sin(theta) , 0 , sp.cos(theta) , 0],
                  [0              , 0 , 0             , 1]])

def rotZ(theta):
  return np.mat( [[sp.cos(theta) , -sp.sin(theta) , 0 , 0],
                  [sp.sin(theta) , sp.cos(theta)  , 0 , 0],
                  [0             , 0              , 1 , 0],
                  [0             , 0              , 0 , 1]])

def trans(x, y, z):
  return  np.mat( [[1 , 0 , 0 , x ],
                   [0 , 1 , 0 , y ],
                   [0 , 0 , 1 , z ],
                   [0 , 0 , 0 , 1 ]])
 
def dhMatrix(theta, a, d, alpha):
  """ Calculate the transformation matrix with this dh-model """
  return rotZ(theta) * trans(a,0,d) * rotX(alpha)
     
 
