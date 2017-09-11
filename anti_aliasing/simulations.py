import numpy as np
import matplotlib.pyplot as plt




# plot a sine wave of frequency "freq" over time interval "time_interval"
# plot same wave sampled at sampling_rate

def plot_signals(time_interval, freq, sampling_rate):
	# set time_res to 1 / (10 * freq) so my plot will have a resolution of 10 samples per waveform
	time_res = 1 / (10 * freq) 
	# time_res times number of points is time_interval...
	num_points = time_interval / time_res
	domain, signal = signal_gen(time_res, freq, num_points)
	sample_space = 1 / sampling_rate
	num_points = time_interval / sample_space
	sample_domain, sampled_signal = signal_gen(sample_space, freq, num_points, phase=(np.pi/4))
	plt.plot(domain, signal, color = 'r')
	plt.plot(sample_domain, sampled_signal, color = 'b')
	plt.savefig('phase_output.png')
	return 

# time res is in seconds, freq in hertz
def signal_gen(time_res, freq, num_points, phase=0):
	total_time = time_res * num_points
	domain = np.arange(0, total_time, time_res);
	f = lambda x : np.sin(2*np.pi*freq*x - phase)
	return domain, f(domain)




if __name__ == "__main__":
		time_res = .001 # 1 ms
		freq = 16000
		sampling_rate = 15258
		num_points = 10
		plot_signals(.01, freq, sampling_rate)	
'''
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax.plot(domain, signal);
		pltV.show()
'''
