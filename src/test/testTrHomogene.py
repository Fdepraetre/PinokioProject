import sys
sys.path.insert(0,"../robotModel/")
import trHomogene
import sympy as sp

sp.init_printing()

theta = sp.symbols('theta')
a     = sp.symbols('a')
d     = sp.symbols('d')
alpha = sp.symbols('alpha')

print ""
print "rotX :"
print trHomogene.rotX(theta)

print ""
print "rotY :"
print trHomogene.rotY(theta)

print ""
print "rotZ :"
print trHomogene.rotZ(theta)

print ""
print "dhMatrix :"
print trHomogene.dhMatrix(theta,a,d,alpha)

