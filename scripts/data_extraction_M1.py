def extract_answers_sequence(file_path):
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
    filename = f"{destination_path}/answers_list_respondent_{n}.txt"

    with open(filename, 'w') as file:
        for answer in answers:
            file.write(str(answer) + "\n")
def write_answers_sequence(answers, n, destination_path):
    filename = f"{destination_path}/answers_list_respondent_{n}.txt"

    with open(filename, 'w') as file:
        for answer in answers:
            file.write(str(answer) + "\n")