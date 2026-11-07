"""
this file is implementations of Activation functions
we first define the base class, then implement the specific activation functions
all the activation functions are implemented as subclasses of Activation
for each class, we implement the forward and backward methods
in the backward method, we use the cached output to compute the gradient
in the forward method, we cache the output for use in the backward method
activatoins implemented: Identity, ReLU, Sigmoid, Tanh, LeakyReLU
Identity is the identity function, i.e. f(x) = x we use this as a placeholder for the activation function
"""

class Activation:
    def forward(self, x):
        raise NotImplementedError

    def __call__(self, x):
        return self.forward(x)

    def backward(self, grad_output):
        raise NotImplementedError


class Identity(Activation):
    def forward(self, x):
        return x

    def backward(self, grad_output):
        return grad_output


class ReLU(Activation):
    def forward(self, x):
        self._cache = x
        return np.maximum(0, x)

    def backward(self, grad_output):
        x = self._cache
        return grad_output * (x > 0)


class Sigmoid(Activation):
    def forward(self, x):
        out = 1.0 / (1.0 + np.exp(-x))
        self._cache = out
        return out

    def backward(self, grad_output):
        s = self._cache
        return grad_output * s * (1.0 - s)


class Tanh(Activation):
    def forward(self, x):
        out = np.tanh(x)
        self._cache = out
        return out

    def backward(self, grad_output):
        t = self._cache
        return grad_output * (1.0 - t * t)


class LeakyReLU(Activation):
    def __init__(self, negative_slope=0.01):
        self.negative_slope = negative_slope

    def forward(self, x):
        self._cache = x
        return np.where(x > 0, x, self.negative_slope * x)

    def backward(self, grad_output):
        x = self._cache
        return grad_output * np.where(x > 0, 1.0, self.negative_slope)
