import numpy as np
import matplotlib.pyplot as plt
import FourierPlot
import WorkWFiles


def gap_monitor(r):
    gap_p = []; gap_v = []
    critical_parameter = np.pi
    for i in range(len(r) - 1):
        if r[i + 1] - r[i] > critical_parameter:
            gap_p.append(i+1)
            gap_v.append(r[i+1])
    return [gap_p, gap_v]


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
    print(gap_monitor(r)[1])
    plt.plot(gap_monitor(r)[0], gap_monitor(r)[1]); plt.show()
    # plt.plot(r, '.'); plt.title("r(t) eps=" + str(i));
    # plt.xlabel('t'); plt.ylabel('r'); plt.show()

    # fourier analysis
    # FourierPlot.do_fourier_plot(s, i)
