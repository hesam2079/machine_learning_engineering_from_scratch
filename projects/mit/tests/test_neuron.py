import numpy as np
import pytest
from nn import Neuron


def relu(x):
    return np.maximum(0, x)


def test_forward_single_sample():
    n = Neuron(weights=[1, 1], bias=-1.5, activation_function=relu)
    assert n.forward([1, 1]) == pytest.approx(0.5)


def test_forward_batch():
    n = Neuron(weights=[1, 1], bias=-1.5, activation_function=relu)
    batch = np.array([[1, 1], [1, 0], [0, 0]])
    result = n.forward(batch)
    np.testing.assert_allclose(result, [0.5, 0.0, 0.0])


def test_shape_mismatch_raises():
    n = Neuron(weights=[1, 1, 1])
    with pytest.raises(ValueError):
        n.forward([1, 1])   # ورودی ۲تایی به نورون ۳وزنی
