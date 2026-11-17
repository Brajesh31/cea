"""Small deterministic and synthetic-data tests for the CEA learning demos."""
from pathlib import Path
import importlib.util
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

def load_script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def test_candidate_elimination_returns_expected_container_shapes():
    mod = load_script("CEA")
    examples = [
        ["Sunny", "Hot", "High", "False", "No"],
        ["Overcast", "Mild", "High", "True", "Yes"],
    ]
    specific, general = mod.candidate_elimination(examples)
    assert len(specific) == 4
    assert len(general) == 4
    assert all(len(row) == 4 for row in general)

def test_neural_network_forward_output_shape_and_finiteness():
    import numpy as np
    mod = load_script("bpalgo")
    network = mod.NeuralNetwork()
    output = network.feedforward(np.array([[0.1], [0.2]]))
    assert output.shape == (2, 1)
    assert np.isfinite(output).all()

def test_neural_network_training_preserves_parameter_shapes():
    import numpy as np
    mod = load_script("bpalgo")
    network = mod.NeuralNetwork()
    network.train(
        np.array([[0.1], [0.2]]),
        np.array([[0.9], [0.1]]),
        learning_rate=0.1,
    )
    assert network.weights.shape == (2, 2)
    assert network.biases.shape == (2, 1)
    assert np.isfinite(network.weights).all()
    assert np.isfinite(network.biases).all()

def test_synthetic_dataset_is_repeatable_and_has_expected_schema():
    mod = load_script("id3")
    first = mod.generate_synthetic_data()
    second = mod.generate_synthetic_data()
    assert first.equals(second)
    assert first.shape == (100, 5)
    assert list(first.columns) == ["Feature_1", "Feature_2", "Feature_3", "Feature_4", "target"]

def test_majority_classifier_and_evaluation_baseline():
    import numpy as np
    import pandas as pd
    mod = load_script("id3")
    frame = pd.DataFrame({"Feature_1": [0, 1, 2, 3], "target": [2, 1, 2, 2]})
    majority = mod.train_model(frame)
    accuracy, predictions = mod.evaluate_model(frame, majority)
    assert majority == 2
    assert np.all(predictions == 2)
    assert accuracy == 0.75
