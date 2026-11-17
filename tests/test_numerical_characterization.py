"""Deterministic characterization checks for the NumPy teaching network."""

import importlib.util
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def load_backprop():
    spec = importlib.util.spec_from_file_location("bpalgo", ROOT / "bpalgo.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_sigmoid_maps_finite_values_into_open_unit_interval():
    network = load_backprop().NeuralNetwork()
    values = network.sigmoid(np.array([-5.0, 0.0, 5.0]))
    assert values.shape == (3,)
    assert np.all(values > 0.0)
    assert np.all(values < 1.0)
    assert np.all(np.diff(values) > 0.0)


def test_forward_pass_matches_fixed_hand_calculated_dimensions():
    network = load_backprop().NeuralNetwork()
    network.weights = np.array([[0.5, -0.25], [0.1, 0.2]])
    network.biases = np.array([[0.0], [0.1]])
    inputs = np.array([[0.3], [0.4]])

    output = network.feedforward(inputs)
    expected_logits = np.array([[0.05], [0.21]])
    expected = 1.0 / (1.0 + np.exp(-expected_logits))

    assert output.shape == (2, 1)
    np.testing.assert_allclose(output, expected, rtol=1e-12, atol=1e-12)


def test_forward_pass_rejects_wrong_input_dimension():
    network = load_backprop().NeuralNetwork()
    with np.testing.assert_raises(ValueError):
        network.feedforward(np.array([[0.25]]))


def test_training_changes_parameters_for_nonzero_error():
    network = load_backprop().NeuralNetwork()
    network.weights = np.array([[0.2, 0.1], [0.3, 0.4]])
    network.biases = np.array([[0.0], [0.0]])
    before_weights = network.weights.copy()
    before_biases = network.biases.copy()

    network.train(
        np.array([[0.1], [0.2]]),
        np.array([[0.9], [0.1]]),
        learning_rate=0.1,
    )

    assert not np.array_equal(network.weights, before_weights)
    assert not np.array_equal(network.biases, before_biases)
