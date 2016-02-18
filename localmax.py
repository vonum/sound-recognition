import numpy as np

def localmax(data, freqs):

	amps = []

	for val in freqs:
		amps.append(np.amax(data[val - 1:val + 1]))

	return np.array(amps)

def adaptivelocalmax(data, freqs):

	amps = []

	for i in range(0, 80):
		amps.append(np.amax(data[freqs[i] - 0.5:freqs[i] + 0.5]))
	for i in range(80, 100):
		amps.append(np.amax(data[freqs[i] - 0.7:freqs[i] + 0.7]))
	for i in range(100, 120):
		amps.append(np.amax(data[freqs[i] - 0.9:freqs[i] + 0.9]))
	for i in range(120, 150):
		amps.append(np.amax(data[freqs[i] - 1.3:freqs[i] + 1.3]))

	return np.array(amps)



