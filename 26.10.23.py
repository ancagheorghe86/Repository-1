import json
import csv
import pandas as pd

class WorkingWithFiles:
    file_path_txt = "C:\\Users\\WDG\\PycharmProjects\\pythonProject\\pythonProject5\\file.txt"
    file_path_csv = "C:\\Users\\WDG\\PycharmProjects\\pythonProject\\pythonProject5\\file.csv"
    file_path_json = "/home/ro-nbl-0130/PycharmProjects/pyta9/file.json"

    def citeste_fisier_text(self):
        with open(file=self.file_path_txt, mode="r") as fisier:
            for line in fisier.readlines():
                line = line.strip()  # elimina caractere nedorite ca /n(newline)
                print(line)

    def citeste_fisier_json(self):
        with open(file=self.file_path_json, mode='r') as file:
            content = json.load(file)
            return content

    def scrie_fisier_json(self, key, value):
        # getting the old file content
        with open(file=self.file_path_json, mode="r+") as file:
            content = json.load(file) # citim fisierul
            content[key] = value # adaugam key + value la content

            file.seek(0)# muta file pointer la inceputul fisierului
            file.truncate() # stergem continutul fisierului
            json.dump(content, file) # scriem contentul in fisier

    def citeste_fisier_csv(self):
        with open(file=self.file_path_csv, mode="r+", newline='\n') as file:
            content = pd.read_csv(file)
            # print(content)
            print(content.values)
            csvwriter = csv.writer(file)
            csvwriter.writerow([3, "234dfsdf", 235235])

    def scriere_fisier(self):
        with open(self.file_path_txt, "a") as fisier:
            fisier.writelines("teste")


e = WorkingWithFiles()
# e.citeste_fisier_text()
# e.citeste_fisier_json()
# e.scrie_fisier_json(key="keyd", value="val d")
e.citeste_fisier_csv()