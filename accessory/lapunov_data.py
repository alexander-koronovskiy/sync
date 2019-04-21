#! /bin/python3
import WorkWFiles
import sys
import numpy as np
from math import log, fabs as abs
from matplotlib import pyplot as pp
from tqdm import trange

if __name__ == '__main__':
    skip = 64
    count = 20480
    step = 0.01
    point = [1.0, 1.0, 1.0]

    def lorenc(p: ()) -> ():
        sig, bet, r = 10, 8 / 3, 28
        x, y, z = p[0], p[1], p[2]
        res = (
            p[0] + step * (sig * (y - x)),
            p[1] + step * (- x * z + r * x - y),
            p[2] + step * (x * y - bet * z)
        )
        return res

    with open("in.txt", "w") as f:
        for i in range(skip):
            point = lorenc(point)
        for i in range(count):
            point = lorenc(point)
            f.write(str(point[0]) + "\n")


if "-h" in sys.argv or "--help" in sys.argv or len(sys.argv) < 3:
    print("""
Usages:
    $ lapunov {input_file.name} {eps} {period_in_samples}

Script works with file like:
        0.01
        0.02
        0.04
        ...
        0.10
        
eps - deviation
    """)
    sys.exit(0)

# deviation
eps = float(sys.argv[2])

with open(sys.argv[1]) as f:
    data = np.asarray([float(i) for i in f.read().split()], dtype=np.float64)

N = len(data)-1
c_idx = 0

lapunov = [(0, 0.0)]
lap = 0.0

upd = trange(N, ncols=80)

while c_idx < N:
    s_idx = int(c_idx + int(sys.argv[3]) * (4./5.))
    if s_idx > N:
        break
    # find closer dots
    while s_idx < N:
        if (data[s_idx] - eps/20 <= data[c_idx]) and (data[s_idx] + eps/20 >= data[c_idx]):
            # print("{0}: {1}".format(c_idx, data[c_idx]))
            # print("{0}: {1}".format(s_idx, data[s_idx]))
            # print(abs(data[s_idx] - data[c_idx]))
            break
        s_idx += 1

    if s_idx == N:
        c_idx += 1
        upd.update(1)
        continue
        # break

    tn = 0
    eps_ = abs(data[s_idx] - data[c_idx])
    # evaluate
    while c_idx < N and (abs(data[s_idx] - data[c_idx]) <= eps):
        tn += 1
        c_idx += 1
        s_idx += 1
        upd.update(1)

    # print("{0}: {1}".format(c_idx, data[c_idx]))
    # print("{0}: {1}".format(s_idx, data[s_idx]))
    # print(abs(data[s_idx] - data[c_idx]))
    # print()

    # apply laponent
    # print(log(abs(data[s_idx] - data[c_idx]) / eps_))
    lap += log(abs(data[s_idx] - data[c_idx]) / eps_)
    lapunov.append(
        (
            len(lapunov),
            lap / c_idx
        )
    )

del lapunov[0]

num = [n[0] for n in lapunov]
val = [v[1] for v in lapunov]
pp.show()
pp.plot(num, val)
