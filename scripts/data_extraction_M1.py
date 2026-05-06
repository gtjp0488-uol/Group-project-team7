def extract_answers_sequence(file_path):
    """
    Reads a respondent quiz answer file and extracts the selected answers.

    The function scans the quiz file line by line, identifies answer options
    marked with '[x]', and converts them into numerical values:
        1 = Answer 1 selected
        2 = Answer 2 selected
        3 = Answer 3 selected
        4 = Answer 4 selected
        0 = No answer selected

    Parameters:
        file_path (str):
            The path to the respondent answer text file.

    Returns:
        list:
            A list of integers representing the respondent's answers.

    Example:
        Input file:
            [x] Answer 1
            [ ] Answer 2
            [ ] Answer 3
            [ ] Answer 4

        Output:
            [1]
    """
    answers = []
    current_question_answers = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()

        if line.startswith("["):
            current_question_answers.append(line)

            if len(current_question_answers) == 4:
                answer_value = 0

                for i, ans in enumerate(current_question_answers):
                    if "[x]" in ans:
                        answer_value = i + 1

                answers.append(answer_value)
                current_question_answers = []

    return answers


def write_answers_sequence(answers, n, destination_path):
    """
    Writes the extracted answer sequence to a text file.

    The function creates a text file named:
        answers_list_respondent_n.txt

    where 'n' is the respondent ID number.

    Each answer is written on a new line in the output file.

    Parameters:
        answers (list):
            A list of integers representing the extracted answers.

        n (int):
            The respondent identification number.

        destination_path (str):
            The folder path where the output file will be saved.

    Returns:
        None

    Example:
        answers = [1, 2, 4, 3]

        Output file:
            answers_list_respondent_1.txt
    """
    filename = f"{destination_path}/answers_list_respondent_{n}.txt"

    with open(filename, 'w') as file:
        for answer in answers:
            file.write(str(answer) + "\n")
