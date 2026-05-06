# Review Notebook – Team Member 1

## Introduction

My role (Sima Sahranavard) in this project was Team Member 1. My task was to create the parsing module for the quiz response analysis project.

The purpose of the module was to read respondent quiz files and convert selected answers into numerical sequences that can later be analysed statistically.

---

# Function 1 – extract_answers_sequence()

This function reads a quiz answer file and extracts the selected answers.

The function searches for answer options marked with `[x]` and converts them into integers:

- 1 = Answer 1 selected
- 2 = Answer 2 selected
- 3 = Answer 3 selected
- 4 = Answer 4 selected
- 0 = No answer selected

Example:

Input:

[x] Answer 1

Output:

[1]

---

# Function 2 – write_answers_sequence()

This function saves the extracted answer sequence into a new text file.

The output file is named:

answers_list_respondent_n.txt

where `n` represents the respondent number.

---

# Testing

The module was tested using:

1. A custom test file (`a1.txt`)
2. Real respondent data provided by Team Member 2

The tests confirmed that the functions correctly extracted and saved answer sequences.

---

# Challenges

Some challenges encountered included:

- understanding file paths;
- handling automatically generated `__pycache__` files;
- case-sensitive filenames in GitHub Codespaces.

These issues were resolved through testing and debugging.

---

# Conclusion

The parsing module successfully converted raw quiz response files into structured numerical data suitable for further analysis.

The module integrates correctly with the wider project workflow and provides a reusable preprocessing component for the project.
