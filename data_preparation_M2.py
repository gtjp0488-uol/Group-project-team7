import os
import requests
def download_answer_files(cloud_url:str, path_to_data_folder:str, total_respondents:int):
    os.makedirs(path_to_data_folder, exist_ok=True)
    for i in range(1,total_respondents+1):
         source_filename = f"a{i}.txt"
         source_url = f"{cloud_url}/{source_filename}"

         my_file = requests.get(source_url)
         if my_file.status_code == 200:
            target_filename = f"answers_respondent_{i}.txt"
            target_path = os.path.join(path_to_data_folder, target_filename)
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(my_file.text)
    
def collate_answer_files(data_folder_path:str):
    files = os.listdir(data_folder_path)
    files.sort(key=lambda x: int(x.split("_")[-1].split(".")[0]))

    output_folder=f"{data_folder_path}_collated"
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, "collated_answers.txt")

    with open(output_path, "w", encoding="utf-8") as f:
       for filename in files:
          full_path = os.path.join(data_folder_path, filename)
          with open(full_path, "r", encoding="utf-8") as g:
              text = g.read()
              f.write(text)
              f.write("\n*\n")

#