# computes lyapunov exponents for Lorenz attractor
# original in MatLab: https://www.mathworks.com/matlabcentral/fileexchange/4628-calculation-lyapunov-exponents-for-ode
import numpy
from scipy.integrate import ode
from matplotlib import pyplot as pp
from tqdm import trange


def nonlin_generator(t, X, m=1.45, g=0.15):
    x, y, z = X[0], X[1], X[2]
    res = numpy.empty(shape=(12,), dtype=numpy.float)
    h = 0.0 if x <= 0.0 else 1.0

    res[0] = m*x + y -x*z
    res[1] = -x
    res[2] = -g*x + h*x**2

    Y = numpy.mat((
        (X[3], X[6], X[9]),
        (X[4], X[7], X[10]),
        (X[5], X[8], X[11])
    ))
    J = numpy.mat((
        (m-z, 1, -x),
        (-1, 0, 0),
        (2*x*h-g, 0, 0)
    ))

    res[3:] = (J * Y).reshape((9,), order="F")

    return res


def Lorenz(t, X, sig=10, bet=8/3, r=28):
    x, y, z = X[0], X[1], X[2]
    res = numpy.empty(shape=(12,), dtype=numpy.float)

    res[0] = sig*(y - x)
    res[1] = -x*z + r*x - y
    res[2] = x*y - bet*z

    Y = numpy.mat((
        (X[3], X[6], X[9]),
        (X[4], X[7], X[10]),
        (X[5], X[8], X[11])
    ))
    J = numpy.mat((
        (-sig, sig, 0),
        (r - z, -1, -x),
        (y, x, -bet)
    ))

    res[3:] = (J*Y).reshape((9,), order="F")

    return res


def lyapunov(n, fn, tStart, tStep, tEnd, y0):
    totalIter = int((tEnd - tStart) / tStep)

    y = numpy.zeros((n + 1, n), numpy.float)
    S = numpy.zeros((n,), numpy.float)

    gsc = numpy.empty((n,), numpy.float)
    norms = numpy.empty((n,), numpy.float)
    series = numpy.empty((totalIter, n + 1), dtype=numpy.float)

    y[0] = y0
    y[1:] = numpy.eye(n)

    t = tStart
    integrator = ode(fn)\
        .set_integrator("dopri5")\
        .set_initial_value(y.flat, t)

    upd = trange(totalIter, ncols=80)

    for i in range(totalIter):
        y = integrator.integrate(t + tStep).reshape((n + 1, n))
        t += tStep

        w = y[1:]
        for j in range(n):
            for k in range(j):
                gsc[k] = numpy.dot(w[j], w[k])

            for k in range(j):
                w[j] -= numpy.dot(gsc[k], w[k])

            norms[j] = numpy.linalg.norm(w[j])
            w[j] /= norms[j]
        y[1:] = w

        S += numpy.log(norms)
        series[i] = (t, *(S / (t - tStart)))

        upd.update(1)

    return series


if __name__ == '__main__':
    res = lyapunov(3, Lorenz, 0.64, 0.1, 1024, [-3.16, -5.31, 13.31])
    # res = lyapunov(3, nonlin_generator, 0.64, 0.1, 1024, [1.0, -1.0, 1.0])

    time = numpy.asarray([p[0] for p in res])
    first = numpy.asarray([p[1] for p in res])
    second = numpy.asarray([p[2] for p in res])
    third = numpy.asarray([p[3] for p in res])

    pp.plot(time, first, label="1")
    pp.plot(time, second, label="2")
    pp.plot(time, third, label="3")
    pp.legend()
    pp.show()
