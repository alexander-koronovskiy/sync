import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

# lorenz_f params
sigma = 10.0
r_d = 40
b = 8.0 / 3.0
r_r = 35.0
eps = 0.00001


def lorenz_f(state, t):
  x_d, y_d, z_d = state  # unpack the state vector
  return sigma * (y_d - x_d), \
         x_d * (r_d - z_d) - y_d, \
         x_d * y_d - b * z_d


def lorenz_f_r(state, t):
    x_r, y_r, z_r, x_d, y_d, z_d = state
    return sigma * (y_d - x_d), \
         x_d * (r_d - z_d) - y_d, \
         x_d * y_d - b * z_d, \
         sigma * (y_r - x_r) + eps * (x_d - x_r), \
         r_r * x_r - y_r - x_r * z_r, \
         x_r * y_r - b * z_r


def plot_f(x_d, y_d, z_d):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x_d, y_d, z_d)
    plt.show()


if __name__ == '__main__':
    state0 = [1.0, 1.0, 1.0]
    t = np.arange(0.0, 40.0, 0.01)
    states = odeint(lorenz_f, state0, t)
    print(states)
    plot_f(states[:, 0], states[:, 1], states[:, 2])
