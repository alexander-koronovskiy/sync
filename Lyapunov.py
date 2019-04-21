from math import log
import numpy as np
import matplotlib.pyplot as plt
import WorkWFiles


def lyapunov_rw(f_r, f_w):
    with open(f_r, 'r') as f:
        data = [float(i) for i in f.read().split()]

    N = len(data)
    eps = 0.001
    lyapunovs = [[] for i in range(N)]

    for i in range(N):
        for j in range(i + 1, N):
            if np.abs(data[i] - data[j]) < eps:
                for k in range(min(N - i, N - j)):
                    lyapunovs[k].append(log(np.abs(data[i+k] - data[j+k])))

    with open(f_w, 'w') as f:
        for i in range(len(lyapunovs)):
            if len(lyapunovs[i]):
                string = str(sum(lyapunovs[i]) / len(lyapunovs[i]))
                f.write(string + '\n')


eps_test_v = [0]
for i in eps_test_v:
    lyapunov_rw('r_lambda/r_eps='+str(i) + '.txt', 'r_lambda/lyapunov_eps='+str(i) + '.txt')
    # data = WorkWFiles.write_to_list('r_lambda/lyapunov_eps='+str(i) + '.txt')
    # plt.plot(data); plt.show()
