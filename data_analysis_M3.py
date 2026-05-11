from __future__ import annotations

import tempfile
from pathlib import Path
from typing import List

import matplotlib.pyplot as plt
import numpy as np

try:
    from data_extraction_M1 import extract_answers_sequence
except ModuleNotFoundError as error:
    raise ModuleNotFoundError(
        "Cannot import data_extraction_M1. Make sure data_extraction_M1.py or data_extraction_M1.pyc is in the same folder."
    ) from error


def _split_collated_answers(collated_answers_path: str) -> List[str]:
    path = Path(collated_answers_path)

    if not path.is_file():
        raise FileNotFoundError(
            f"Cannot find the collated answers file: {collated_answers_path}"
        )

    text = path.read_text(encoding="utf-8")

    if not text.strip():
        raise ValueError("The collated answers file is empty.")

    respondent_blocks = []
    current_block = []

    for line in text.splitlines():
        if line.strip() == "*":
            block = "\n".join(current_block).strip()
            if block:
                respondent_blocks.append(block)
            current_block = []
        else:
            current_block.append(line)

    final_block = "\n".join(current_block).strip()
    if final_block:
        respondent_blocks.append(final_block)

    if not respondent_blocks:
        raise ValueError("No respondent blocks were found in the collated file.")

    return respondent_blocks


def _extract_sequences_from_collated(collated_answers_path: str) -> List[List[int]]:
    blocks = _split_collated_answers(collated_answers_path)
    sequences = []

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)

        for respondent_id, block in enumerate(blocks, start=1):
            temp_file = tmp_path / f"temporary_respondent_{respondent_id}.txt"
            temp_file.write_text(block, encoding="utf-8")

            sequence = extract_answers_sequence(str(temp_file))

            if len(sequence) != 100:
                raise ValueError(
                    f"Respondent {respondent_id} produced {len(sequence)} answers. Expected 100."
                )

            invalid_values = sorted(
                set(value for value in sequence if value not in (0, 1, 2, 3, 4))
            )

            if invalid_values:
                raise ValueError(
                    f"Respondent {respondent_id} contains invalid values: {invalid_values}."
                )

            sequences.append(sequence)

    return sequences


def generate_means_sequence(collated_answers_path: str) -> List[float]:
    sequences = _extract_sequences_from_collated(collated_answers_path)
    data = np.array(sequences, dtype=float)

    means = []

    for question_index in range(100):
        question_answers = data[:, question_index]
        answered_answers = question_answers[question_answers != 0]

        if answered_answers.size == 0:
            means.append(float("nan"))
        else:
            means.append(float(np.mean(answered_answers)))

    return means


def visualize_data(collated_answers_path: str, n: int) -> None:
    question_numbers = np.arange(1, 101)

    if n == 1:
        means = generate_means_sequence(collated_answers_path)

        plt.figure(figsize=(12, 6))
        plt.scatter(question_numbers, means)
        plt.title("Mean Answer Value for Each Question")
        plt.xlabel("Question Number")
        plt.ylabel("Mean Answer Value, excluding unanswered responses")
        plt.xticks(np.arange(1, 101, 5))
        plt.yticks([1, 2, 3, 4])
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    elif n == 2:
        sequences = _extract_sequences_from_collated(collated_answers_path)

        plt.figure(figsize=(14, 7))

        for sequence in sequences:
            plotted_sequence = [np.nan if answer == 0 else answer for answer in sequence]
            plt.plot(question_numbers, plotted_sequence, linewidth=1, alpha=0.45)

        plt.title("Individual Respondent Answer Sequences")
        plt.xlabel("Question Number")
        plt.ylabel("Selected Answer Option")
        plt.xticks(np.arange(1, 101, 5))
        plt.yticks([1, 2, 3, 4])
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    else:
        print("Error: n must be 1 for a scatter plot or 2 for a line plot.")


if __name__ == "__main__":
    default_path = Path("output") / "collated_answers.txt"

    if default_path.exists():
        means_sequence = generate_means_sequence(str(default_path))
        print("First 10 mean answer values:")
        print(means_sequence[:10])

        visualize_data(str(default_path), 1)
        visualize_data(str(default_path), 2)
    else:
        print("No collated answers file found at output/collated_answers.txt.")
