import sympy as sy
import sympy.utilities.lambdify  as lam

import numpy as np
import matplotlib.pyplot as plt


class par:
	def __init__(
		self,
		i_lx=1,
		i_hx=1,
		i_sx=1,
		i_ly=1,
		i_hy=1,
		i_sy=1,
		i_lz=1,
		i_hz=1,
		i_sz=1
		):
		self.lx = i_lx
		self.hx = i_hx
		self.sx = i_sx
		self.ly = i_ly
		self.hy = i_hy
		self.sy = i_sy
		self.lz = i_lz
		self.hz = i_hz
		self.sz = i_sz
		


p = par(1,1,10,1,1,10,1,1,10)


x,y,z,t = sy.symbols('x y z t',real=True)


phi = sy.Function('phi',real=True)(x,y,z) 


phi = (1+0.5*sy.tanh(p.sx*(x-p.lx/2))-0.5*sy.tanh(p.sx*(x+p.lx/2)))*p.hx
phi*= (1+0.5*sy.tanh(p.sy*(y-p.ly/2))-0.5*sy.tanh(p.sy*(y+p.ly/2)))*p.hy
#phi*= (1+0.5*sy.tanh(p.sz*(z-p.lz/2))-0.5*sy.tanh(p.sz*(z+p.lz/2)))*p.hz


e_x = phi.diff(x)
e_y = phi.diff(y)

Xmin = -5
Xmax = 5
Xpts = 100
X = np.linspace(Xmin,Xmax,Xpts,endpoint=True)

Ymin = -5
Ymax = 5
Ypts = 100
Y = np.linspace(Ymin,Ymax,Ypts,endpoint=True)



Phi = np.zeros((Xpts,Ypts))

E_x = np.zeros((Xpts,Ypts))
E_y = np.zeros((Xpts,Ypts))



sy.pprint(phi)


for ix in range(Xpts):
	for iy in range(Ypts):
		Phi[ix,iy] = (0.5*np.tanh(10*X[ix] - 5.0) - 0.5*np.tanh(10*X[ix] + 5.0) + 1)*(0.5*np.tanh(10*Y[iy] - 5.0) - 0.5*np.tanh(10*Y[iy] + 5.0) + 1)

	
#		E_x[ix,iy] = e_x.subs([(x, X[ix]), (y, Y[iy])])
#		E_y[ix,iy] = e_y.subs([(x, X[ix]), (y, Y[iy])])








print(Phi)


fig, ax = plt.subplots()
im = ax.imshow(Phi)

plt.show()


#plt.plot(X,Phi)


#sy.pprint(e_x)

#plt.plot(X,E_x)



#plt.show()
