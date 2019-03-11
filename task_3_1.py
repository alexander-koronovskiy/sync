import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

# lorenz_f params
sigma = 10.0
r_d = 28.0
r_r = 8.0 / 3.0


def lorenz_f(state, t):
  x, y, z = state           # unpack the state vector
  return sigma * (y - x),   \
         x * (r_d - z) - y, \
         x * y - r_r * z    # derivatives


def plot_f(x, y, z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x, y, z)
    plt.show()


if __name__ == '__main__':
    state0 = [1.0, 1.0, 1.0]
    t = np.arange(0.0, 40.0, 0.01)
    states = odeint(lorenz_f, state0, t)
    plot_f(states[:, 0], states[:, 1], states[:, 2])
