import numpy as np
import matplotlib.pyplot as plt
import accessory.FourierPlot
import DiffEq
import WorkWFiles


def gap_monitor(r):
    gap_p = []; gap_v = []
    critical_parameter = np.pi / 2
    for i in range(len(r) - 1):
        if abs(r[i + 1] - r[i]) > critical_parameter:
            gap_p.append(i+1)
            gap_v.append(r[i+1])
    return [gap_p, gap_v]


def diff_arr(r):
    diff_array = []
    for i in range(len(r) - 1):
        diff = r[i + 1] - r[i]
        diff_array.append(diff)
    return diff_array


# real time solution
# s = DiffEq.solve(); s0 = s[3]
# fi = DiffEq.phase_diff(s)

# relation params: 0, 0.112, 0.118, 0.2, 0.3
# variables: 'x', 'y', 'z', 'u', 'v', 'w'
eps_test_v = [0, 0.112, 0.118, 0.2]
param = ['x', 'y', 'z', 'u', 'v', 'w']
l = []

for i in eps_test_v:
    # recorded solution: s - solution of the equation; fi - phase difference
    s0 = WorkWFiles.write_to_list("solutions/u_eps=" + str(i) + ".dat")
    fi = WorkWFiles.write_to_list("solutions/phase_diff_eps=" + str(i) + ".dat")

    # r(t) building
    r = 2 * np.sin(np.array(fi) / 2)
    WorkWFiles.write_to_file(r, 'r_lambda/r_eps=' + str(i)+'.txt')
    r1 = gap_monitor(r)

    # diff arrays - разность между точками-разрывами
    # r(1 - 2) - ламинарная, r2(2n + 1) - ламинарные; r2(2n) - турбулентные
    r2 = diff_arr(r1[0])
    l.append(np.mean(r2[::2]))

    # fi plotting
    # plt.plot(fi[5000:6000]); plt.title("$f$(t) eps=" + str(i)); plt.ylim(0, 2)
    # plt.xlabel('t'); plt.ylabel('$f$'); plt.show()

    # r(t) plotting
    plt.plot(r); plt.xlabel('t'); plt.ylabel('r')
    plt.xlim(5000, 7000); plt.title("r(t) eps=" + str(i))
    # plt.plot(r1[0], r1[1])
    plt.show()

    # lyapunov exponent plotting
    for j in param:
        le = WorkWFiles.write_to_list('r_lambda/lapunov_' + j + '_eps=' + str(i) + '.txt')
        plt.plot(le); plt.title("lyapunov exponents eps=" + str(i))
    plt.show()

plt.plot(eps_test_v, l); plt.xlabel('eps'); plt.ylabel('lambda'); plt.show()
