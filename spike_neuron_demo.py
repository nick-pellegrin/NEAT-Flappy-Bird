import matplotlib.pyplot as plt

import neat
import math
import random


def plot_spikes(spikes, jumps, title):
    """ Plots the trains for a single spiking neuron. """
    t_values = [t for t, I, v, u, f in spikes]
    v_values = [v for t, I, v, u, f in spikes]
    u_values = [u for t, I, v, u, f in spikes]
    I_values = [I for t, I, v, u, f in spikes]
    f_values = [f for t, I, v, u, f in spikes]

    fig = plt.figure()
    plt.subplot(4, 1, 1)
    plt.ylabel("Potential (mv)")
    plt.xlabel("Time (in ms)")
    plt.grid()
    plt.plot(t_values, v_values, "g-")

    plt.title("Izhikevich's spiking neuron model ({0!s})".format(title))

    plt.subplot(4, 1, 2)
    plt.ylabel("Fired")
    plt.xlabel("Time (in ms)")
    plt.grid()
    plt.plot(t_values, f_values, "r-")

    # plt.subplot(4, 1, 3)
    # plt.ylabel("Recovery (u)")
    # plt.xlabel("Time (in ms)")
    # plt.grid()
    # plt.plot(t_values, u_values, "r-")

    plt.subplot(4, 1, 3)
    plt.ylabel("Inputs")
    plt.xlabel("Time (in ms)")
    plt.grid()
    plt.plot(t_values, jumps, "r-")

    plt.subplot(4, 1, 4)
    plt.ylabel("Current (I)")
    plt.xlabel("Time (in ms)")
    plt.grid()
    plt.plot(t_values, I_values, "r-")

    # fig = plt.figure()
    # plt.title("Izhikevich's spiking neuron model u/v ({0!s})".format(title))
    # plt.xlabel("Recovery (u)")
    # plt.ylabel("Potential (mv)")
    # plt.grid()
    # plt.plot(u_values, v_values, 'r-')

    plt.show()
    plt.close()


# def show(title, a, b, c, d):
#     n = neat.iznn.IZNeuron(0.0, a, b, c, d, [])
#     net = neat.iznn.IZNN([n], [n], [])
#     spike_train = []
#     for i in range(1000):
#         if i < 100 or i > 800:
#             # n.current = 0.0
#             net.inputs[0].current = 0.0  
#         else:
#             #n.current = 10 * math.sin(6.28*i/700)
#             net.inputs[0].current = 10 * math.sin(6.28*i/700)
#         # spike_train.append((1.0 * i, n.current, n.v, n.u, n.fired))
#         spike_train.append((1.0 * i, n.current, n.v, n.u, n.fired))
#         print('{0:d}\t{1:f}\t{2:f}\t{3:f}'.format(i, n.current, n.v, n.u))
#         n.advance(0.25)

#     plot_spikes(spike_train, title)

def show(title, a, b, c, d):
    n = neat.iznn.IZNeuron(0.0, a, b, c, d, [])
    # o = neat.iznn.IZNeuron(0.0, a, b, c, d, [])
    net = neat.iznn.IZNN([n], [n], [])
    dt = net.get_time_step_msec()
    spike_train = []
    inputs = []
    for i in range(1000):
        net.set_inputs([10*math.sin(i)])
        # net.inputs[0].current = random.randint(0, 11)
        spike_train.append((1.0 * i, net.inputs[0].current, net.inputs[0].v, net.inputs[0].u, net.inputs[0].fired))
        inputs.append(10*math.sin(i))
        
        print('{0:d}\t{1:f}\t{2:f}\t{3:f}'.format(i, net.inputs[0].current, net.inputs[0].v, net.inputs[0].u))
        #neat.iznn.IZNN.advance = new_advance
        net.advance(0.25)

    plot_spikes(spike_train, inputs, title)


# def new_advance(self, dt_msec):
#         for n in self.neurons.values():
#             n.current = n.bias
#             for i, w in n.inputs:
#                 ineuron = self.neurons.get(i)
#                 ivalue = self.input_values[i]

#                 n.current += ivalue * w

#         for n in self.neurons.values():
#             n.advance(dt_msec)

#         return [self.neurons[i].fired for i in self.outputs]



show('regular spiking', **neat.iznn.REGULAR_SPIKING_PARAMS)

show('intrinsically bursting', **neat.iznn.INTRINSICALLY_BURSTING_PARAMS)

show('chattering', **neat.iznn.CHATTERING_PARAMS)

show('fast spiking', **neat.iznn.FAST_SPIKING_PARAMS)

show('low-threshold spiking', **neat.iznn.LOW_THRESHOLD_SPIKING_PARAMS)

show('thalamo-cortical', 0.02, 0.25, -65.0, 0.05)

show('resonator', 0.1, 0.26, -65.0, 2.0)

plt.show()