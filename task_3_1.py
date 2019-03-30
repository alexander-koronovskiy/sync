# imports
import sympy
from scipy.integrate import odeint
import re as regex
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# define all symbols I am going to use
x = sympy.Symbol('x')
y = sympy.Symbol('y')
z = sympy.Symbol('z')
t = sympy.Symbol('t')

# read the file
systemOfEquations = []
with open("systems.txt", "r") as fp:
   for line in fp:
            pattern = regex.compile(r'.+?\s+=\s+(.+?)$')
            expressionString = regex.search(pattern, line)
            # first match ends in group(1)
            systemOfEquations.append(sympy.sympify(expressionString.group(1)))


def dX_dt(X, t):
    vals = dict(x=X[0], y=X[1], z=X[2], t=t)
    return [eq.evalf(subs=vals) for eq in systemOfEquations]


def do_s_result(arg_num):
    solver_result = []
    solver_array = odeint(dX_dt, [0.1, 0.1, 0.1], np.linspace(0, 10, 500))
    for i in range(len(solver_array)):
        solver_result.append(solver_array[i][arg_num])
    return solver_result


def plot_f(x, y, z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x, y, z)
    plt.show()


if __name__ == '__main__':
    plot_f(do_s_result(0), do_s_result(1), do_s_result(2))
