import numpy as np
import matplotlib.pyplot as plt
import FourierPlot
import WorkWFiles


def gap_monitor(r):
    gap_p = []
    critical_parameter = np.pi
    for i in range(len(r) - 1):
        if r[i + 1] - r[i] > critical_parameter:
            gap_p.append(i+1)
    return gap_p


# relation parameters
eps_test_v = [0, 0.112, 0.118, 0.2]

for i in eps_test_v:
    # s - solution of the equation; fi - phase difference
    s = WorkWFiles.write_to_list("solutions/u_eps=" + str(i) + ".dat")
    fi = WorkWFiles.write_to_list("solutions/phase_diff_eps=" + str(i) + ".dat")

    # fi plotting
    # plt.plot(fi[5000:6000]); plt.title("$f$(t) eps=" + str(i)); plt.ylim(0, 2)
    # plt.xlabel('t'); plt.ylabel('$f$'); plt.show()

    # r(t) building
    r = 2 * np.sin(np.array(fi) / 2)
    print(gap_monitor(r))
    plt.plot(gap_monitor(r)); plt.show()
    # plt.plot(r, '.'); plt.title("r(t) eps=" + str(i));
    # plt.xlabel('t'); plt.ylabel('r'); plt.show()

    # fourier analysis
    # FourierPlot.do_fourier_plot(s, i)
