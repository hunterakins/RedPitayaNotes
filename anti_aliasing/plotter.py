import numpy as np
import matplotlib.pyplot as plt
import sys

if __name__ == '__main__':
	curr_file = sys.argv[1]
	output = sys.argv[2]
	vals = np.loadtxt(curr_file)
	domain = np.arange(0, .01, .01 / 153)
	plt.plot(domain, vals[:153])
	plt.savefig(output)
 
