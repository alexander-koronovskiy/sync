import matplotlib.pyplot as plt
import numpy as np


def cauchy(f1, f2, x10, x20, T, h):
    x1 = [x10]
    x2 = [x20]
    for i in range(1, h):
        k11 = f1((i-1)*T/h, x1[-1], x2[-1])
        k12 = f2((i-1)*T/h, x1[-1], x2[-1])
        k21 = f1((i-1)*T/h + T/h/2, x1[-1] + T/h/2*k11, x2[-1] + T/h/2*k12)
        k22 = f2((i-1)*T/h + T/h/2, x1[-1] + T/h/2*k11, x2[-1] + T/h/2*k12)
        k31 = f1((i-1)*T/h + T/h/2, x1[-1] + T/h/2*k21, x2[-1] + T/h/2*k22)
        k32 = f2((i-1)*T/h + T/h/2, x1[-1] + T/h/2*k21, x2[-1] + T/h/2*k22)
        k41 = f1((i-1)*T/h + T/h, x1[-1] + T/h*k31, x2[-1] + T/h*k32)
        k42 = f2((i-1)*T/h + T/h, x1[-1] + T/h*k31, x2[-1] + T/h*k32)
        x1.append(x1[-1] + T/h/6*(k11 + 2*k21 + 2*k31 + k41))
        x2.append(x2[-1] + T/h/6*(k12 + 2*k22 + 2*k32 + k42))
    return x1, x2


def f1(t, x1, x2):
    return x2


def f2(t, x1, x2):
    return -x1


def true_x1(t):
    return np.cos(t) + np.sin(t)


def true_x2(t):
    return np.cos(t) - np.sin(t)


x10 = 1
x20 = 1
T = 10
h = 100

x1, x2 = cauchy(f1, f2, x10, x20, T, h)
t = np.linspace(0, T, h)
plt.xlabel('t')
plt.ylabel('x1')
plt.plot(x1, "red", label="approximation_x1")
plt.plot(true_x1(t), "blue", label="true_x1")
plt.legend(bbox_to_anchor=(0.97, 0.27))
plt.show()
