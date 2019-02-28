# Supplementary classes and functions for ENGSCI233 notebook performance.ipynb
# author: David Dempsey
import numpy as np
from matplotlib import pyplot as plt
	
def compare_scaling():
	''' plots two different algorithm scalings
	'''
	N = np.linspace(1,1e5, 101)
	k = 0.4e4
	heapN = k*N*np.log2(N)
	insertionN = N**2

	# plot the comparison
	f,ax = plt.subplots(1,1, figsize=(8,4))
	ax.plot(N, insertionN, 'b-', label='algorithm 1')
	ax.plot(N, heapN, 'r-', label = 'algorithm 2')
	ax.legend()
	ax.set_xlabel('size of problem, $N$')
	ax.set_ylabel('execution time, $\mathcal{O}(N)$')
	plt.show()
	
def scaling_loglog():
	''' plots two different algorithm scalings
	'''
	N = 2**np.arange(1,10)
	fN = N**2
	# plot the comparison
	f,(ax1,ax2,ax3) = plt.subplots(1,3, figsize=(16,4))
	ax1.plot(N, fN, 'bx',mew=1.5)
	ax2.plot(np.log10(N), np.log10(fN), 'bx',mew=1.5)
	ax3.plot(N, fN, 'bx',mew=1.5)
	for ax in [ax1,ax3]:
		ax.set_xlabel('size of problem, $N$')
		ax.set_ylabel('execution time, $\mathcal{O}(N)$')
	ax2.set_xlabel('logged size of problem, $log(N)$')
	ax2.set_ylabel('logged execution time, $log(\mathcal{O}(N))$')
	ax3.set_xscale('log')
	ax3.set_yscale('log')
	plt.show()