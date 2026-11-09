import numpy as np

from nn import Neuron
from nn import Layer
from nn import ReLU
from nn import LeakyReLU

n = Neuron(weights=[1, 1], bias=-1.5, activation_function=ReLU())
activation_function = ReLU()
l1 = Layer(input_dim=2, output_dim=5, activation=activation_function)
activation_function = LeakyReLU()
l2 = Layer(input_dim=5, output_dim=1, activation=activation_function)


input_data = np.array([1, 1])
output_data = l1.forward(input_data)
print(output_data)
output_data = l2.forward(output_data)
print(output_data)
