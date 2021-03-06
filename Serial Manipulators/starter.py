from sympy import symbols, cos, sin, pi, simplify, sqrt, atan2
from sympy.matrices import Matrix

###############################################################
# Problem Statement:
  # Let P be a vector expressed in frame {B} with (x,y,z)
  # coordinates = (15.0, 0.0, 42.0)
  # Rotate P about the Y-axis by angle = 110 degrees. 
  # Then translate the vector 1 unit
  # in the X-axis and 30 units in the Z-axis. 
  # Print the new (x, y, z) coordinates of P after the transformation.  
###############################################################


# Create symbols for joint variable

q1 = symbols('q1')
gamma  = symbols('gamma')

# Conversion Factors

rtd = 180./pi # radians to degrees
dtr = pi/180. # degrees to radians

# coordinates of point P

P = Matrix([[15.0],[0.0],[42.0],[1]] )

# The homogenous transform of 

T = Matrix([[ cos(q1),        0,  sin(q1),  0],
            [       0,        1,        0,   0],
            [-sin(q1),        0,  cos(q1),  30]]) 

# The coordniate of P after the transformation 
P_new = T* P

P_new = simplify(T * P)
print("P_new is :", P_new)

# Evaluate numerically
print("The new coordinates of P_A are :", P_new.evalf(subs={q1: 110*dtr}))
