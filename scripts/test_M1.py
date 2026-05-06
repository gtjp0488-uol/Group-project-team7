from data_extraction_M1 import extract_answers_sequence

# test with a sample file
answers = extract_answers_sequence("data/a1.txt")
# test with answers_respondent_1.txt (in moc_data)
answers = extract_answers_sequence("moc_data/answers_respondent_1.txt")
print(answers)
