import pycwt as wavelet
import numpy as np
import matplotlib.pyplot as plt

num_steps = 512
x = np.arange(num_steps)
y = np.sin(2*np.pi*x/32) + np.cos(2*np.pi*x/128)

delta_t = x[1] - x[0]
scales = np.arange(1, num_steps+1)
freqs = 1/(wavelet.Morlet().flambda() * scales)
wavelet_type = 'morlet'

coefs, scales, freqs, coi, fft, fftfreqs = wavelet.cwt(y, delta_t, wavelet=wavelet_type, freqs=freqs)
plt.matshow(coefs.real)
plt.show()
