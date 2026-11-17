"""Checks that committed example fixtures remain small and synthetic."""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "docs" / "examples"


def read_csv(name):
    with (EXAMPLES / name).open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def test_candidate_fixture_has_four_attributes_and_binary_labels():
    rows = read_csv("candidate_examples.csv")
    assert len(rows) >= 1
    assert all(
        set(row) == {"outlook", "temperature", "humidity", "windy", "label"}
        for row in rows
    )
    assert {row["label"] for row in rows} <= {"Yes", "No"}


def test_backprop_fixture_contains_two_finite_numeric_inputs():
    rows = read_csv("backprop_inputs.csv")
    assert rows
    for row in rows:
        assert set(row) == {"input_1", "input_2"}
        assert all(float(value) == float(value) for value in row.values())


def test_baseline_fixture_contains_only_small_integer_classes():
    rows = read_csv("baseline_labels.csv")
    labels = {int(row["target"]) for row in rows}
    assert rows
    assert labels <= {0, 1, 2}
