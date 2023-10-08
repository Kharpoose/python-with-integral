import sympy as smp
import numpy as np
import matplotlib.pyplot as plt


x = smp.symbols('x')

print(smp.limit(smp.sin(x/2 + smp.sin(x)), x, smp.pi))

print(smp.diff(((1 + smp.sin(x)) / (1 - smp.cos(x)))*2, x))

#y = smp.sin(x)
#print(x)



#print(smp.sin(x))

#z =  x**2

#print(z.expand())