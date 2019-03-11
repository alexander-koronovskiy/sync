# single function in this darkness
# one direction coupled ressler
# be-coupled ressler oscillator
import numpy
from functools import reduce
import matplotlib.pyplot as plt
from copy import deepcopy
from functools import reduce

#------methods--------
# return remake of data


# Уравнение Ресслера
def bec_ressler(state, alienstate, params):
    x, y, z = state
    x2, y2, z2 = alienstate
    dxdt = -params["w"]*y - z + params["E"]*(x2 - x)
    dydt = params["w"]*x + params["a"]*y
    dzdt = params["p"] + z*(x - params["c"])
    newstate = [dxdt, dydt, dzdt]
    return newstate


def norm(vector):
    norm_value = (reduce(lambda a, x: a + x**2, vector, 0))**0.5
    return norm_value


# метод Эйлера
def euler_method(state, increment, dt):
    new_state = list(map(lambda x: x[0] + x[1] * dt, zip(state, increment)))
    return new_state


def e_error(state_d, params):
    e_value = sum(state_d["e_error_norm"]) / len(state_d["e_error_norm"]) / (
                state_d["savedtime"][-1] - state_d["savedtime"][params["startfrom"]])
    return e_value


def update_state(state_d, params):
    state_osc1 = state_d["osc1"][-1]
    state_osc2 = state_d["osc2"][-1]
    increment_osc1 = bec_ressler(state_osc1, state_osc2, params["osc1"])
    increment_osc2 = bec_ressler(state_osc2, state_osc1, params["osc2"])
    dt = params["dt"]

    new_state_osc1 = euler_method(state_osc1, increment_osc1, dt)
    new_state_osc2 = euler_method(state_osc2, increment_osc2, dt)

    if (len(state_d["savedtime"])>params["startfrom"]) and abs(increment_osc1[0]) < 2**33:
        vector_difference = list(map(lambda x: x[0] - x[1], zip(increment_osc1, increment_osc2)))
        e_error_integral = euler_method([state_d["e_error_norm"][-1]], [norm(vector_difference)], dt)[0]
        state_d["e_error_norm"].append(e_error_integral)
    state_d["osc1"].append(new_state_osc1)
    state_d["osc2"].append(new_state_osc2)
    state_d["savedtime"].append(state_d["time"].pop(0))


def make_timestep(state_d, params):
    while state_d["time"]:
        update_state(state_d, params)


if __name__ == '__main__':
    # art of state evolution
    params = {
        "osc1": {
            "a": 0.15,
            "p": 0.2,
            "c": 10,
            "w": 0.81,  # Изменять в пределах [0.89 - 1.01]
            "E": .1,
        },
        "osc2": {
            "a": 0.15,
            "p": 0.2,
            "c": 10,
            "w": 0.8,  # const
            "E": 0.1,
        },
        "dt": 0.1,
        "startfrom": 500,
        "e_error": 0,
    }

    state_d = {
        "time": [t for t in numpy.arange(0, 100.0001, params["dt"])],
        "savedtime": [],
        "osc1": [[0.1, 0.1, 0.1], ],
        "osc2": [[0.1, 0.1, 0.1], ],
        "e_error_norm": [0, ]
    }

    def part1_x1fromx2(state_d, params):
        make_timestep(state_d, params)

        x_osc1 = list(map(lambda x: x[0], state_d["osc1"][params["startfrom"]:]))
        x_osc2 = list(map(lambda x: x[0], state_d["osc2"][params["startfrom"]:]))
        plt.plot(x_osc1, x_osc2, "r.")
        plt.xlim(-15, 20)
        plt.ylim(-15, 20)
        plt.grid()
        plt.show()

        print("e_error: ", e_error(state_d, params))
    part1_x1fromx2(deepcopy(state_d), deepcopy(params))

    def part2_efromE(state_d, params):
        def pipeline_each(data, fns):
            result = reduce(lambda a, x: list(map(x, a)),
                            fns,
                            data)
            return result

        def make_elist(state_d, params):
            E_osc1 = [i for i in numpy.arange(0, 2.5, 0.005)]
            E_osc2 = [i for i in numpy.arange(0, 2.5, 0.005)]

            def make_timestep_local(data):
                state_d, params = data
                make_timestep(state_d, params)
                return state_d, params

            def e_list_append(data):
                state_d, params = data
                params["e_error"] = e_error(state_d, params)
                return state_d, params

            # TODO remake - data into list of params [params1, params2, params3]
            # TODO make for each params it's calculus

            paramlist = [deepcopy(params) for i in E_osc1]
            params_and_E = list(zip(paramlist, E_osc1, E_osc2))
            def updateEs(p_E_sample):
                params, E_osc1, E_osc2 = p_E_sample[0], p_E_sample[1], p_E_sample[2]
                params["osc1"]["E"] = E_osc1
                params["osc2"]["E"] = E_osc2
                return params
            paramlist = list(map(updateEs, params_and_E))
            state_d_list = [deepcopy(state_d) for i in E_osc1]

            data = list(zip(state_d_list, paramlist))
            new_data = pipeline_each(data, [make_timestep_local, e_list_append])
            e_list = list(map(lambda x: x[1]["e_error"], new_data))
            return E_osc1, E_osc2, e_list

        E_osc1, E_osc2, e_list = make_elist(state_d, params)
        plt.plot(E_osc1, e_list, "b-")
        plt.yscale("log")

        plt.grid()
        plt.show()
        # print(e_list)

    part2_efromE(deepcopy(state_d), deepcopy(params))
