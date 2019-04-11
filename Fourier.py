import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import WorkWFiles

# Number of sample points
N = 7500
T = 1.0 / 500.0

# frequency example
x = np.linspace(0.0, N*T, N)
y = np.sin(800.0 * 2.0*np.pi*x) + 0.5*np.sin(500.0 * 2.0*np.pi*x)

# relation parameters
eps_test_v = [0, 0.112, 0.118, 0.2]

for i in eps_test_v:
    # s - solution of the equation; fi - phase difference
    s = WorkWFiles.write_to_list("solutions/u_eps=" + str(i) + ".dat")
    fi = WorkWFiles.write_to_list("solutions/phase_diff_eps=" + str(i) + ".dat")

    # s, fi plotting
    # DiffEq.plot_f(s[0], s[1], s[2])
    plt.plot(fi[5000:6000]); plt.title("fi eps=" + str(i)); plt.ylim(-3, 3)

    # r(t) building
    r = 2 * np.sin(np.array(fi) / 2)[5000:6000]
    # plt.plot(r); plt.title("r eps=" + str(i))

    # fourier analysis building
    yf = scipy.fftpack.fft(s)
    xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

    # fourier plots
    fig, ax = plt.subplots(); ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
    plt.xlabel('Frequency[$f$]'); plt.ylabel('x'); plt.ylim(0, 20)
    plt.title("eps=" + str(i))
    plt.show()
