# imports
import sympy
from scipy.integrate import odeint
import re as regex
import numpy as np
import matplotlib.pyplot as plt
import math
import WorkWFiles
from mpl_toolkits.mplot3d import Axes3D

# define relation type for analysis: strong or weak
relation_type = 'strong'

# define all symbols I am going to use
x = sympy.Symbol('x')
y = sympy.Symbol('y')
z = sympy.Symbol('z')
t = sympy.Symbol('t')
u = sympy.Symbol('u')
v = sympy.Symbol('v')
w = sympy.Symbol('w')

# read the file
systemOfEquations = []
with open("systems/systems_all.txt", "r") as fp:
   for line in fp:
        pattern = regex.compile(r'.+?\s+=\s+(.+?)$')
        expressionString = regex.search(pattern, line)
        # first match ends in group(1)
        systemOfEquations.append(sympy.sympify(expressionString.group(1)))


def dX_dt(X, t):
    vals = dict(x=X[0], y=X[1], z=X[2],
                u=X[3], v=X[4], w=X[5], t=t)
    return [eq.evalf(subs=vals) for eq in systemOfEquations]


def do_s_result(arg_num):
    solver_result = []
    solver_array = odeint(dX_dt, [1, 1, 0, 1, 1, 0], np.linspace(0, 10, 500))
    for i in range(len(solver_array)):
        solver_result.append(solver_array[i][arg_num])
    return solver_result


def plot_f(x, y, z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x, y, z)
    plt.show()


def do_phase_shift(X, Y):
    n = min(len(X), len(Y))
    phase_array = []
    for i in range(n):
        phase_array.append(math.atan(Y[i] / X[i]))
    return phase_array


def save_s_result():
    var_names = [x, y, z, u, v, w]
    for i in range(6):
        WorkWFiles.write_to_file(do_s_result(i), 'solutions_' + relation_type + '/' + str(var_names[i]) + '.txt')


if __name__ == '__main__':
    # solution data rewriting
    # save_s_result()

    # d - drive system
    x_sol = WorkWFiles.write_to_list('solutions_' + relation_type + '/x.txt')
    y_sol = WorkWFiles.write_to_list('solutions_' + relation_type + '/y.txt')
    z_sol = WorkWFiles.write_to_list('solutions_' + relation_type + '/z.txt')
    # r - driven system
    u_sol = WorkWFiles.write_to_list('solutions_' + relation_type + '/u.txt')
    v_sol = WorkWFiles.write_to_list('solutions_' + relation_type + '/v.txt')
    w_sol = WorkWFiles.write_to_list('solutions_' + relation_type + '/w.txt')
    # 3D dyn sys plots
    plot_f(x_sol, y_sol, z_sol)
    plot_f(u_sol, v_sol, w_sol)
    # dependence between phase and time
    a = do_phase_shift(x_sol, u_sol)
    plt.title(relation_type + ' relation type')  # weak: ε = 0.01; strong: ε = 10
    plt.xlabel('Time[t]')
    plt.ylabel('Phase[$f$]')
    plt.plot(a)
    plt.show()
