import numpy as np
import matplotlib.pyplot as plt
import FourierPlot
import WorkWFiles


# relation parameters
eps_test_v = [0, 0.112, 0.118, 0.2]

for i in eps_test_v:
    # s - solution of the equation; fi - phase difference
    s = WorkWFiles.write_to_list("solutions/u_eps=" + str(i) + ".dat")
    fi = WorkWFiles.write_to_list("solutions/phase_diff_eps=" + str(i) + ".dat")

    # fi plotting
    plt.plot(fi[5000:6000],'.'); plt.title("fi(t) eps=" + str(i)); plt.ylim(0, 2)
    plt.xlabel('t'); plt.ylabel('fi'); plt.show()

    # r(t) building
    r = 2 * np.sin(np.array(fi) / 2)
    plt.plot(r[5000:6000], '.'); plt.title("r(t) eps=" + str(i)); plt.ylim(0, 2)
    plt.xlabel('t'); plt.ylabel('r'); plt.show()

    # fourier analysis
    # FourierPlot.do_fourier_plot(s, i)
