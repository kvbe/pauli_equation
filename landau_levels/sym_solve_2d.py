import sympy as sy
import numpy as np
import matplotlib.pyplot as plt


E = sy.symbols('E', real=True)


x,y = sy.symbols('x y', real=True)

f = sy.Function('f')(x,y)


X = sy.Function('X')(x)
Y = sy.Function('Y')(y)

eq = sy.Eq(
	E*f,
	-1/2*sy.Derivative(f,y,2)
	+y**2
	-1/2*sy.Derivative(f,x,2)
	-x*sy.Derivative(f,y)
	+1/2*x**2
)

clas = sy.classify_pde(eq)

#sol = sy.pdsolve(eq,func=f,hint='all')

#sep = sy.pde_separate(eq, f, [X, Y], strategy='mul')

#sy.pprint(f)
#sy.pprint(eq)
#sy.pprint(sep)
#sy.pprint(sol)
sy.pprint(clas)
