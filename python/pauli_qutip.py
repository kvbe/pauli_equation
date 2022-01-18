from sympy.solvers.pde import pdsolve

from sympy import Function, Eq

from sympy.abc import x, y
import sympy as sy


f = Function('f')

u = f(x, y)

ux = u.diff(x)

uy = u.diff(y)

eq = Eq(1 + (2*(ux/u)) + (3*(uy/u)), 0)

sol = pdsolve(eq)

sy.pprint(sol)
