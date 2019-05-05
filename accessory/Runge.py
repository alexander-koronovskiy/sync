import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math


# Runge Kutta Method
def rKN(x, fx, n, hs):
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    xk = []
    for i in range(n):
        k1.append(fx[i](x)*hs)
    for i in range(n):
        xk.append(x[i] + k1[i]*0.5)
    for i in range(n):
        k2.append(fx[i](xk)*hs)
    for i in range(n):
        xk[i] = x[i] + k2[i]*0.5
    for i in range(n):
        k3.append(fx[i](xk)*hs)
    for i in range(n):
        xk[i] = x[i] + k3[i]
    for i in range(n):
        k4.append(fx[i](xk)*hs)
    for i in range(n):
        x[i] = x[i] + (k1[i] + 2*(k2[i] + k3[i]) + k4[i])/6
    return x


# Equation System
def f_x(x):
    return 10*x[1] - 10*x[0]
def f_y(x):
    return 40*x[0] - x[0]*x[2] - x[1]
def f_z(x):
    return x[0]*x[1] - 8/3*x[2]
def f_u(x):
    return 10*x[4] - 10*x[3] + 20*(x[0] - x[3])  # relation cases: strong(ε = 20) or weak(ε = 0.2)
def f_v(x):
    return 35*x[3] - x[3]*x[5] - x[4]
def f_w(x):
    return x[3]*x[4] - 8/3*x[5]


def solve():
    f = [f_x, f_y, f_z, f_u, f_v, f_w]
    x = [1, 1, 0, 0.1, 0.1, 0.1]
    hs = 0.02
    X =[]; Y=[]; Z=[]; U=[]; V=[]; W=[]
    for i in range(1000):
        x = rKN(x, f, 6, hs)
        X.append(x[0]); Y.append(x[1]); Z.append(x[2])
        U.append(x[3]); V.append(x[4]); W.append(x[5])
    return [X, Y, Z, U, V, W]


def plot_f(x, y, z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x, y, z)
    plt.show()


if __name__ == '__main__':
    # save or solve
    s = solve()
    plot_f(s[3], s[4], s[5])  # 3D Ressler system plot
