import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math
import WorkWFiles


# Equation System func, ε - relation parameter
eps = 0.2
def f_x(x):
    return - x[1] - x[2]
def f_y(x):
    return x[0] + 0.15*x[1]
def f_z(x):
    return 0.2 + x[0]*x[2] - 10*x[2]
def f_u(x):
    return - 0.95*x[4] - x[5] + eps*(x[0] - x[3])
def f_v(x):
    return 0.95*x[3] + 0.15*x[4]
def f_w(x):
    return 0.2 + x[3]*x[4] - 10*x[5]


# Runge Kutta solution
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
def solve():
    f = [f_x, f_y, f_z, f_u, f_v, f_w]
    x = [1, 1, 0, 0.1, 0.1, 0.1]
    hs = 0.1
    X =[]; Y=[]; Z=[]; U=[]; V=[]; W=[]
    for i in range(15000):
        x = rKN(x, f, 6, hs)
        X.append(x[0]); Y.append(x[1]); Z.append(x[2])
        U.append(x[3]); V.append(x[4]); W.append(x[5])
    return [X, Y, Z, U, V, W]


# work with arrays of phases
def do_phase_shift_np(X, Y):
    X = np.array(X); Y = np.array(Y)
    return np.arctan2(Y, X)
def do_diff_arrays(x, y):
    a = [x]
    b = [y]
    c = [list(map(lambda a, b: a - b, a[i], b[i])) for i in range(len(a))]
    return c[0]
def do_phase_shift(X, Y):
    n = min(len(X), len(Y))
    phase_array = []
    for i in range(n):
        phase_array.append(math.atan2(Y[i], X[i]))
    return phase_array

# save solution results in text files
def save(s):
    WorkWFiles.write_to_file(s[0], 'solutions/x_eps=' + str(eps) + '.dat')
    WorkWFiles.write_to_file(s[1], 'solutions/y_eps=' + str(eps) + '.dat')
    WorkWFiles.write_to_file(s[2], 'solutions/z_eps=' + str(eps) + '.dat')
    WorkWFiles.write_to_file(s[3], 'solutions/u_eps=' + str(eps) + '.dat')
    WorkWFiles.write_to_file(s[4], 'solutions/v_eps=' + str(eps) + '.dat')
    WorkWFiles.write_to_file(s[5], 'solutions/w_eps=' + str(eps) + '.dat')
def phase_diff(s):
    phase = do_diff_arrays(do_phase_shift(s[0], s[1]), do_phase_shift(s[3], s[4]))  # task 3.1
    # WorkWFiles.write_to_file(phase, 'solutions/phase_diff_eps=' + str(eps) + '.dat')
    return phase


# plotting
def plot_f(x, y, z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x, y, z)
    plt.show()
def do_plot(*args):
    for i in args:
        plt.plot(i)
    plt.show()


if __name__ == '__main__':
    s = solve()
    # save(s)
    fi = phase_diff(s); fi_part = fi[5000:6000]
    # plot_f(s[0], s[1], s[2])  # 3D Ressler system plot
    do_plot(fi_part)
