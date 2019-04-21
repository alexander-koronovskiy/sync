import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

# Number of sample points
N = 7500
T = 1.0 / 500.0

# frequency example
x = np.linspace(0.0, N*T, N)
y = np.sin(800.0 * 2.0*np.pi*x) + 0.5*np.sin(500.0 * 2.0*np.pi*x)


# fourier analysis building
def do_fourier_plot(s, eps=0):
    yf = scipy.fftpack.fft(s)
    xf = np.linspace(0.0, 1.0 / (2.0 * T), N / 2)

    # fourier plots
    fig, ax = plt.subplots()
    ax.plot(xf, 2.0 / N * np.abs(yf[:N // 2]))
    plt.xlabel('Frequency[$f$]')
    plt.ylabel('x')
    plt.ylim(0, 20)
    plt.title("eps=" + str(eps))
    plt.show()
