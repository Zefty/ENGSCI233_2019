
# imports 
import numpy as np
from matplotlib import pyplot as plt
from ipywidgets import interact, interactive, Checkbox, Layout, HBox, Dropdown, IntSlider, fixed, FloatSlider
from IPython.display import display

class ImprovedEuler(object):
	''' This class is a hard coded Improved Euler method for a particular function and time step.
	
		It is hard coded because you will be implementing Improved Euler in the lab and I don't want
		the more enterprising students visiting the source code to copy the method.
	'''
	def __init__(self):
		self.x = [0, 0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6, 0.7, 0.7999999999999999, 0.8999999999999999]
		self.y = [1, 1.111605, 1.2510911476245623, 1.4303787320668615, 1.669257368774675, 2.0030917028294266, 2.501624425724359, 3.3228472650308203, 4.90801761586217, 9.010617182240603]
		self.dydx0s = [1.0, 1.23467765676025, 1.5630456214364068, 2.042365737783545, 2.781233121133108, 4.0061857953154485, 6.254874227126293, 11.062230004937321, 24.269555812652037,-1]
		self.dydx1s = [1.2321000000000002, 1.555045295730995, 2.0227060674095765, 2.735206996372725, 3.8954535599619247, 5.9644686625831955, 10.169582559002931, 20.641177011689674, 57.78243551491661,-1]
		self.yps = [1.1, 1.235072765676025, 1.407395709768203, 1.634615305845216, 1.9473806808879859, 2.4037102823609713, 3.1271118484369884, 4.429070265524553, 7.334973197127374,-1]

def dydx(x,y): return (1.+x*y)**2

def euler_step(step, h):
	f,(ax, ax2) = plt.subplots(1,2)
	f.set_size_inches([10,5])

	x = [0,]
	y = [1,]
	h0 = 0.1
	
	xlim = np.array([-0.05,1.15])
	ylim = [-0.9,10]
	ax.set_ylim(ylim)
	ax.set_xlim(xlim)
	
	for i in range(int(step)):
		y.append(y[-1]+h0*dydx(x[-1], y[-1]))
		x.append(x[-1]+h0)		
		
	if abs(step-int(step))>0.25:
		# plot derivative
		dydx0 = dydx(x[-1], y[-1])
		ys = dydx0*(xlim - x[-1])+y[-1]
		ax.plot(xlim, ys, 'r--')		
		ax.text(0.95*xlim[-1], np.min([1.05*ys[-1],9.]), 'compute derivative: $f^{'+'{:d}'.format(int(step))+'}=(x^{'+'{:d}'.format(int(step))+'},y^{'+'{:d}'.format(int(step))+'})$', ha = 'right', va = 'bottom', color = 'r')
	else:	
		dy = 0.4
		dx = 0.04
		ax.arrow(x[-2], y[-2]-dy, h0, 0, length_includes_head = True, head_width = 0.2, head_length = 0.02, color= 'r', linewidth = 0.5)
		ax.arrow(x[-1], y[-2]-dy, -h0, 0, length_includes_head = True, head_width = 0.2, head_length = 0.02, color= 'r', linewidth = 0.5)
		ax.text(0.5*(x[-1]+x[-2]), y[-2]-2*dy, '$x^{'+'{:d}'.format(int(step))+'}=x^{'+'{:d}'.format(int(step-1))+'}+h$', ha = 'center', va = 'top', color = 'r')
		
		ax.arrow(x[-1]+dx, y[-2], 0, y[-1]-y[-2], length_includes_head = True, head_width = 0.02, head_length = 0.2, color= 'r', linewidth = 0.5)
		ax.arrow(x[-1]+dx, y[-1], 0, -y[-1]+y[-2], length_includes_head = True, head_width = 0.02, head_length = 0.2, color= 'r', linewidth = 0.5)
		
		ax.text(x[-1]+2*dx, 0.5*(y[-1]+y[-2]), '$y^{'+'{:d}'.format(int(step))+'}=y^{'+'{:d}'.format(int(step-1))+'}+hf^{'+'{:d}'.format(int(step-1))+'}$', ha = 'left', va = 'center', color = 'r')
				
	ax.plot(x,y,'ko-', mfc = 'k')
	
	ax.plot(x[-1],y[-1],'ko', mfc = 'w')
	
	ax.set_xlabel('$x$', size = 14)
	ax.set_ylabel('$y(x)$', size = 14)
	
	# second plot, effect of step size
	x = [0,]
	y = [1,]
	x0 = [0,]
	y0 = [1,]
	
	while x[-1] < 1.:
		y.append(y[-1]+h*dydx(x[-1], y[-1]))
		x.append(x[-1]+h)	
	while x0[-1] < 1.:
		y0.append(y0[-1]+h0*dydx(x0[-1], y0[-1]))
		x0.append(x0[-1]+h0)	

	#y = y[:-1]
	#x = x[:-1]
	y0 = y0[:-1]
	x0 = x0[:-1]
	
	ax2.plot(x,y,'ko-', mfc = 'k', label = 'h={:3.2f}'.format(h))
	ax2.plot(x0,y0,'ko-', mfc = 'k', alpha = 0.5, label = 'h={:3.2f}'.format(h0))
	
	ax2.set_xlabel('$x$', size = 14)
	ax2.set_ylabel('$y(x)$', size = 14)
	ax2.set_ylim([0,20])
	ax2.set_xlim(xlim)
	
	ax2.legend(loc=2)
	
def euler_example():
	
	col_layout=Layout(display='flex', flex_flow='row-wrap', width="90%", justify_content='space-around', align_items='stretch')
	
	items = [FloatSlider(value = 0.5, description='steps', min=0.5, max = 10, step=0.5),
		FloatSlider(value = 0.1, description = '$h$', min= 0.02, max = 0.2, step=0.02)]
		
	hbox=HBox(items, layout=col_layout)
	
	w=interactive(euler_step, step = items[0], h = items[1])
	
	hbox.on_displayed(euler_step(step=0.5, h = 0.1))
	display(hbox)

def improved_euler_step(step, euler):
	f,ax = plt.subplots(1,1)
	f.set_size_inches([10,4])

	x = [0,]
	y = [1,]
	h0 = 0.1
	
	xlim = np.array([-0.05,1.15])
	ylim = [-0.9,10]
	ax.set_ylim(ylim)
	ax.set_xlim(xlim)	
	dydx0s = []
	dydx1s = []
	yps = []
	for i in range(int(np.ceil(step))):
		dydx0 = dydx(x[-1], y[-1])
		j = abs(step-i)
		if 0.2 < j < 0.4: break
		yp = y[-1]+h0*dydx0
		
		if 0.4 < j < 0.6: break
		dydx1 = dydx(x[-1]+h0, yp)
		dydxm = 0.5*(dydx0+dydx1)
		
		if 0.6 < j < 0.8: break	
		
		y.append(y[-1]+h0*dydxm)
		x.append(x[-1]+h0)		
		
	if not euler:
		j = abs(step-int(step))
		if 0.2 < j < 0.4:
			# plot derivative
			ys = dydx0*(xlim - x[-1])+y[-1]
			ax.plot(xlim, ys, 'r--')		
			ax.text(0.95*xlim[-1], np.min([1.05*ys[-1],9.]), 'predictor derivative: $f^{'+'{:d}'.format(int(step))+'}=(x^{'+'{:d}'.format(int(step))+'},y^{'+'{:d}'.format(int(step))+'})$', ha = 'right', va = 'bottom', color = 'r')
			
			ax.text(0.02, 0.95, 'PREDICTOR STEP', color = 'k', transform=ax.transAxes, ha = 'left', va = 'top')
		elif 0.4 < j < 0.6:
			ax.plot([x[-1],x[-1]+h0],[y[-1],yp],'k--o', mfc = 'w')
			dy = 0.4
			dx = 0.04
			ax.arrow(x[-1], y[-1]-dy, h0, 0, length_includes_head = True, head_width = 0.2, head_length = 0.01, color= 'r', linewidth = 0.5)
			ax.arrow(x[-1]+h0, y[-1]-dy, -h0, 0, length_includes_head = True, head_width = 0.2, head_length = 0.01, color= 'r', linewidth = 0.5)
			ax.text(0.5*(2*x[-1]+h0), y[-1]-2*dy, '$x^{'+'{:d}'.format(int(step+1))+'}=x^{'+'{:d}'.format(int(step))+'}+h$', ha = 'center', va = 'top', color = 'r')
			
			ax.arrow(x[-1]+h0+dx, yp, 0, y[-1]-yp, length_includes_head = True, head_width = 0.01, head_length = 0.2, color= 'r', linewidth = 0.5)
			ax.arrow(x[-1]+h0+dx, y[-1], 0, yp-y[-1], length_includes_head = True, head_width = 0.01, head_length = 0.2, color= 'r', linewidth = 0.5)		
			ax.text(x[-1]+h0+2*dx, 0.5*(y[-1]+yp), '$y_p^{'+'{:d}'.format(int(step+1))+'}=y^{'+'{:d}'.format(int(step))+'}+hf^{'+'{:d}'.format(int(step))+'}$', ha = 'left', va = 'center', color = 'r')
			
			ax.text(0.02, 0.95, 'PREDICTOR STEP', color = 'k', transform=ax.transAxes, ha = 'left', va = 'top')
			
		elif 0.6 < j < 0.8:
			ax.plot([x[-1],x[-1]+h0],[y[-1],yp],'k--o', mfc = 'w')
			# plot derivative
			ys = dydx0*(xlim - x[-1])+y[-1]
			ax.plot(xlim, ys, 'r--')	
			ys = dydx1*(xlim - x[-1]-h0)+yp
			ax.plot(xlim, ys, 'b--')	
			
			ax.text(0.95*xlim[-1], np.min([1.05*ys[-1],9.]), 'corrector derivative: $f_p^{'+'{:d}'.format(int(step+1))+'}=(x^{'+'{:d}'.format(int(step+1))+'},y_p^{'+'{:d}'.format(int(step+1))+'})$', ha = 'right', va = 'bottom', color = 'b')
			
			ax.text(0.02, 0.95, 'CORRECTOR STEP', color = 'k', transform=ax.transAxes, ha = 'left', va = 'top')
		else:	
			dy = 0.4
			dx = 0.04

			ys = dydxm*(xlim - x[-1])+y[-1]
			ax.plot(xlim, ys, 'g--')	
			
			
			ax.text(0.95*xlim[-1], np.min([1.05*ys[-1],9.]), 'average derivative: '+r'$\frac{h}{2}(f^{'+'{:d}'.format(int(step-1))+'}+f_p^{'+'{:d}'.format(int(step))+'})$', ha = 'right', va = 'bottom', color = 'g')
			
			ax.arrow(x[-2], y[-2]-dy, h0, 0, length_includes_head = True, head_width = 0.2, head_length = 0.01, color= 'g', linewidth = 0.5)
			ax.arrow(x[-1], y[-2]-dy, -h0, 0, length_includes_head = True, head_width = 0.2, head_length = 0.01, color= 'g', linewidth = 0.5)
			ax.text(0.5*(x[-1]+x[-2]), y[-2]-2*dy, '$x^{'+'{:d}'.format(int(step))+'}=x^{'+'{:d}'.format(int(step-1))+'}+h$', ha = 'center', va = 'top', color = 'g')
			
			ax.arrow(x[-1]+dx, y[-2], 0, y[-1]-y[-2], length_includes_head = True, head_width = 0.01, head_length = 0.2, color= 'g', linewidth = 0.5)
			ax.arrow(x[-1]+dx, y[-1], 0, -y[-1]+y[-2], length_includes_head = True, head_width = 0.01, head_length = 0.2, color= 'g', linewidth = 0.5)		
			ax.text(x[-1]+2*dx, 0.5*(y[-1]+y[-2]), '$y^{'+'{:d}'.format(int(step))+'}=y^{'+'{:d}'.format(int(step-1))+r'}+\frac{h}{2}(f^{'+'{:d}'.format(int(step-1))+'}+f_p^{'+'{:d}'.format(int(step))+'})$', ha = 'left', va = 'center', color = 'g')
					
			ax.text(0.02, 0.95, 'CORRECTOR STEP', color = 'k', transform=ax.transAxes, ha = 'left', va = 'top')
	
	ax.plot(x,y,'ko-', mfc = 'k', label='Improved Euler', zorder = 2)
	
	ax.plot(x[-1],y[-1],'ko', mfc = 'w', zorder = 3)
	
	ax.set_xlabel('$x$', size = 14)
	ax.set_ylabel('$y(x)$', size = 14)
	
	
	if euler:
		# plot euler for comparison
		x0 = [0,]
		y0 = [1,]
		for i in range(int(np.floor(step))):
			y0.append(y0[-1]+h0*dydx(x0[-1], y0[-1]))
			x0.append(x0[-1]+h0)		
			
		ax.plot(x0,y0,'ko-', color = [0.7,0.7,0.7], mec = [0.7,0.7,0.7], zorder = 1, label = 'Euler')
		
		ax.legend(loc=2)

def improved_euler_step_adhoc(step, euler):
	ie = ImprovedEuler()
	
	f,ax = plt.subplots(1,1)
	f.set_size_inches([10,4])

	x = [0,]
	y = [1,]
	h0 = 0.1
	
	xlim = np.array([-0.05,1.15])
	ylim = [-0.9,10]
	ax.set_ylim(ylim)
	ax.set_xlim(xlim)	
	
	i = int(np.floor(step))
	x = ie.x[:i+1]
	y = ie.y[:i+1]
	dydx0 = ie.dydx0s[i]
	dydx1 = ie.dydx1s[i]
	dydxm = 0.5*(ie.dydx0s[i-1] + ie.dydx1s[i-1])
	yp = ie.yps[i]
	
	if not euler:
		j = abs(step-int(step))
		if 0.2 < j < 0.4:
			# plot derivative
			ys = dydx0*(xlim - x[-1])+y[-1]
			ax.plot(xlim, ys, 'r--')		
			ax.text(0.95*xlim[-1], np.min([1.05*ys[-1],9.]), 'predictor derivative: $f^{'+'{:d}'.format(int(step))+'}=(x^{'+'{:d}'.format(int(step))+'},y^{'+'{:d}'.format(int(step))+'})$', ha = 'right', va = 'bottom', color = 'r')
			
			ax.text(0.02, 0.95, 'PREDICTOR STEP', color = 'k', transform=ax.transAxes, ha = 'left', va = 'top')
		elif 0.4 < j < 0.6:
			ax.plot([x[-1],x[-1]+h0],[y[-1],yp],'k--o', mfc = 'w')
			dy = 0.4
			dx = 0.04
			ax.arrow(x[-1], y[-1]-dy, h0, 0, length_includes_head = True, head_width = 0.2, head_length = 0.01, color= 'r', linewidth = 0.5)
			ax.arrow(x[-1]+h0, y[-1]-dy, -h0, 0, length_includes_head = True, head_width = 0.2, head_length = 0.01, color= 'r', linewidth = 0.5)
			ax.text(0.5*(2*x[-1]+h0), y[-1]-2*dy, '$x^{'+'{:d}'.format(int(step+1))+'}=x^{'+'{:d}'.format(int(step))+'}+h$', ha = 'center', va = 'top', color = 'r')
			
			ax.arrow(x[-1]+h0+dx, yp, 0, y[-1]-yp, length_includes_head = True, head_width = 0.01, head_length = 0.2, color= 'r', linewidth = 0.5)
			ax.arrow(x[-1]+h0+dx, y[-1], 0, yp-y[-1], length_includes_head = True, head_width = 0.01, head_length = 0.2, color= 'r', linewidth = 0.5)		
			ax.text(x[-1]+h0+2*dx, 0.5*(y[-1]+yp), '$y_p^{'+'{:d}'.format(int(step+1))+'}=y^{'+'{:d}'.format(int(step))+'}+hf^{'+'{:d}'.format(int(step))+'}$', ha = 'left', va = 'center', color = 'r')
			
			ax.text(0.02, 0.95, 'PREDICTOR STEP', color = 'k', transform=ax.transAxes, ha = 'left', va = 'top')
			
		elif 0.6 < j < 0.8:
			ax.plot([x[-1],x[-1]+h0],[y[-1],yp],'k--o', mfc = 'w')
			# plot derivative
			ys = dydx0*(xlim - x[-1])+y[-1]
			ax.plot(xlim, ys, 'r--')	
			ys = dydx1*(xlim - x[-1]-h0)+yp
			ax.plot(xlim, ys, 'b--')	
			
			ax.text(0.95*xlim[-1], np.min([1.05*ys[-1],9.]), 'corrector derivative: $f_p^{'+'{:d}'.format(int(step+1))+'}=(x^{'+'{:d}'.format(int(step+1))+'},y_p^{'+'{:d}'.format(int(step+1))+'})$', ha = 'right', va = 'bottom', color = 'b')
			
			ax.text(0.02, 0.95, 'CORRECTOR STEP', color = 'k', transform=ax.transAxes, ha = 'left', va = 'top')
		else:	
			dy = 0.4
			dx = 0.04

			ys = dydxm*(xlim - x[-1])+y[-1]
			ax.plot(xlim, ys, 'g--')	
			
			
			ax.text(0.95*xlim[-1], np.min([1.05*ys[-1],9.]), 'average derivative: '+r'$\frac{h}{2}(f^{'+'{:d}'.format(int(step-1))+'}+f_p^{'+'{:d}'.format(int(step))+'})$', ha = 'right', va = 'bottom', color = 'g')
			
			ax.arrow(x[-2], y[-2]-dy, h0, 0, length_includes_head = True, head_width = 0.2, head_length = 0.01, color= 'g', linewidth = 0.5)
			ax.arrow(x[-1], y[-2]-dy, -h0, 0, length_includes_head = True, head_width = 0.2, head_length = 0.01, color= 'g', linewidth = 0.5)
			ax.text(0.5*(x[-1]+x[-2]), y[-2]-2*dy, '$x^{'+'{:d}'.format(int(step))+'}=x^{'+'{:d}'.format(int(step-1))+'}+h$', ha = 'center', va = 'top', color = 'g')
			
			ax.arrow(x[-1]+dx, y[-2], 0, y[-1]-y[-2], length_includes_head = True, head_width = 0.01, head_length = 0.2, color= 'g', linewidth = 0.5)
			ax.arrow(x[-1]+dx, y[-1], 0, -y[-1]+y[-2], length_includes_head = True, head_width = 0.01, head_length = 0.2, color= 'g', linewidth = 0.5)		
			ax.text(x[-1]+2*dx, 0.5*(y[-1]+y[-2]), '$y^{'+'{:d}'.format(int(step))+'}=y^{'+'{:d}'.format(int(step-1))+r'}+\frac{h}{2}(f^{'+'{:d}'.format(int(step-1))+'}+f_p^{'+'{:d}'.format(int(step))+'})$', ha = 'left', va = 'center', color = 'g')
					
			ax.text(0.02, 0.95, 'CORRECTOR STEP', color = 'k', transform=ax.transAxes, ha = 'left', va = 'top')
		
	ax.plot(x,y,'ko-', mfc = 'k', label='Improved Euler', zorder = 2)
	
	ax.plot(x[-1],y[-1],'ko', mfc = 'w', zorder = 3)
	
	ax.set_xlabel('$x$', size = 14)
	ax.set_ylabel('$y(x)$', size = 14)
	
	
	if euler:
		# plot euler for comparison
		x0 = [0,]
		y0 = [1,]
		for i in range(int(np.floor(step))):
			y0.append(y0[-1]+h0*dydx(x0[-1], y0[-1]))
			x0.append(x0[-1]+h0)		
			
		ax.plot(x0,y0,'ko-', color = [0.7,0.7,0.7], mec = [0.7,0.7,0.7], zorder = 1, label = 'Euler')
		
		ax.legend(loc=2)
		
def improved_euler_example():
	
	col_layout=Layout(display='flex', flex_flow='row-wrap', width="90%", justify_content='center', align_items='stretch')
	
	items = [FloatSlider(value = 7.00, description='steps', min=0.25, max = 9, step=0.25), Checkbox(False, description='Euler')]
		
	hbox=HBox(items, layout=col_layout)
	
	improved_euler_step = improved_euler_step_adhoc
	
	w=interactive(improved_euler_step, step = items[0], euler = items[1])
	
	hbox.on_displayed(improved_euler_step(step=7.00, euler=False))
	display(hbox)
	