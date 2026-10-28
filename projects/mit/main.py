import numpy as np

from nn import Neuron

def relu(x):
    return np.maximum(0, x)

n = Neuron(weights=[1, 1], bias=-1.5, activation_function=relu)

print(n.forward([1, 1]))   # → 0.5
print(n.forward([1, 0]))   # → 0.0
print(n.forward([0, 0]))   # → 0.0

batch = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
print(n.forward(batch))    # → [0.5 0.  0.  0. ]
