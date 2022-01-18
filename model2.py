import numpy as np
import matplotlib.pyplot as plt


class par:
	def __init__(
		self,
		i_l=[1,1,1],
		i_s=[1,1,1],
		i_h=1
		):
		self.lx = i_l[0]
		self.ly = i_l[1]
		self.lz = i_l[2]

		self.sx = i_s[0]
		self.sy = i_s[1]
		self.sz = i_s[2]

		self.h = i_h
		
def smooth_rect(c, p, mode):
	val=0

	if mode == "tanh":
#		for i in range(len(c)):

		#crx=p.sx*(c[0]-p.lx)
		#clx=p.sx*(c[0]+p.lx)

		#cry=p.sy*(c[1]-p.ly)
		#cly=p.sy*(c[1]+p.ly)

		cr=p.sx*(np.sqrt(c[0]**2+c[1]**2)-p.lx/2)
		cl=p.sx*(np.sqrt(c[0]**2+c[1]**2)+p.lx/2)

		right = 1/(1+np.exp(-cr))
		left  = 1/(1+np.exp( cl))
		
		val+= left+right
	
	val*= p.h
	return val



def radial_E(c, p, mode):
	val=0

	if mode == "tanh":

		cr=p.sx*(np.sqrt(c[0]**2+c[1]**2)-p.lx/2)
		cl=p.sx*(np.sqrt(c[0]**2+c[1]**2)+p.lx/2)

		right = np.exp(cr)/(1+np.exp(cr))**2
		left  = np.exp(cl)/(1+np.exp(cl))**2
		
		val+= left-right
	
	val*= p.h*p.sx
	return val






p = par([4,1,1],[10,1,1],1)









Xmin = -10
Xmax = 10
Xpts = 200
X = np.linspace(Xmin,Xmax,Xpts,endpoint=True)

Ymin = -10
Ymax = 10
Ypts = 200
Y = np.linspace(Ymin,Ymax,Ypts,endpoint=True)


rect_mode = "tanh"

Phi = np.zeros((Xpts,Ypts))
Efield = np.zeros((Xpts,Ypts))


h=1

for ix in range(Xpts):
	for iy in range(Ypts):
		Phi[ix,iy] = smooth_rect([X[ix],Y[iy]], p, rect_mode)
		Efield[ix,iy] = radial_E([X[ix],Y[iy]], p, rect_mode)



fig, axs = plt.subplots(1,4)

#ax.plot(X,Phi)

im = axs[0].imshow(
	Phi,
	extent=(Xmin,Xmax,Ymin,Ymax),
	origin='lower',
)

im = axs[1].imshow(
	Efield,
	extent=(Xmin,Xmax,Ymin,Ymax),
	origin='lower',
)






PhiY0 = np.asarray(list(zip(*Phi)))[int(Ypts/2)]

PhiX0 = Phi[int(Xpts/2)]

axs[2].plot(X,PhiY0)
axs[3].plot(Y,PhiX0)



plt.show()
