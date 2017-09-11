import matplotlib.pyplot as plt
import numpy as np

vals = open('jitter_test', "r")

vals = [int(line) for line in vals]
print(vals)

histo_domain = range(374, 385)
histogram = [0]*11
for i in range(len(vals)):
	histogram[vals[i] - 374] += 1

mean = np.mean(vals)
std_dev = np.std(vals)
print(mean)
print(std_dev)
print(histogram)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(np.linspace(-5*8,6*8, 11), histogram, '.')
ax.set_title("Distribution of trigger jitter about mean")
ax.set_xlabel("Offset time in ns")
ax.set_ylabel("Number of samples")
ax.text(-5*8, max(histogram)*.95 , "Std. dev: " + str(std_dev*8)[0:4], bbox={'alpha':0.5, 'pad':10})
plt.show()
