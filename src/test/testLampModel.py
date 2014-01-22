import sys
sys.path.insert(0,"../robotModel/")
import lampModel
import sympy as sp
sp.init_printing()

model = lampModel.lampMGD()

print ""
print "_0Tf :"
print model.getTransMatrix()


