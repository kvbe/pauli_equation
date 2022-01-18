import numpy as np
import matplotlib.pyplot as plt

def phi(x, y, z, par, opt):
	xpts = len(x)
	ypts = len(y)
	zpts = len(z)
	
	if opt="rect":
		def pot(val)
	
	
	
	
	
	phi = np.zeros((xpts,ypts,zpts))
	
	for xi in range(xpts):
		for yi in range(ypts):
			for zi in range(zpts):
				phi[xi,yi,zi] = par.q*pot(x[xi])*pot(y[yi])*pot(z[zi])
	


Xmin = -1.0
Xmax = 1.0
Xpts = 50

X = np.linspace(Xmin,Xmax,Xpts,endpoint=True)

Ymin = -1.0
Ymax = 1.0
Ypts = 50

Y = np.linspace(Ymin,Ymax,Ypts,endpoint=True)

Zmin = -1.0
Zmax = 1.0
Zpts = 50

Z = np.linspace(Zmin,Zmax,Zpts,endpoint=True)

