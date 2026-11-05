import numpy as np

class Neuron:
    def __init__(self, weights, bias=0.0, activation_function= lambda x:x):
        self.weights = np.array(weights, dtype=float)
        self.bias = float(bias)
        self.activation_function = activation_function


    def forward(self, inputs):
        inputs = np.array(inputs, dtype=float)
        if inputs.shape[-1] != self.weights.shape[0]:
            raise ValueError(
                            f"Shape mismatch: inputs{inputs.shape} vs weights{self.weights.shape}"
                        )
        aggregation = np.dot(inputs, self.weights) + self.bias
        return self.activation_function(aggregation)
