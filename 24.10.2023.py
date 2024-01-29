'''TodoList
    Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor

     Metode:
adauga_task(nume, descriere) - se va adauga in dict
finalizează_task(nume) - se va sterge din dict
afișează_todo_list() - doar cheile
afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului, printăm detalii suplimentare.
Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l adauge.
Dacă acesta răspunde nu - la revedere
Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict
'''

class Todolist:
    # todo este un dictionar cu chei si valori pentru aceste chei
    # cheile sunt unice
    todo = {}

    def afiseaza_todo(self):
        for item in self.todo:
            print(item)

    def adauga_task(selfself, nume_task, descriere):
        self.todo[nume_task] = descriere

    def finalizeaza_task(self, nume_task):
        self.todo.pop(nume_task)

    def detalii_suplimentare(self, nume_task):
        # verificam daca nume_task este in self.todo
        if nume_task not in self.todo:
            response = input("Taskul nu este in todo. Vrei sa il adaugi?")
            if response == "da":
                descriere = input("Spune-mi nume task")
                self.adauga_task(nume_task, descriere)
        else:
            print(self.todo[nume_task])

todo_list = Todolist()
todo_list.afiseaza_todo()
todo_list.adauga_task("learn python1", "doing python exercises")
todo_list.adauga_task("learn python2", "doing python exe")
todo_list.adauga_task("learn python3", "doing python ex")
todo_list.afiseaza_todo()
todo_list.detalii_suplimentare("learn python")

import json


class example_Json:
    file_path_txt = "C:\Users\vasile.mocanu\PycharmProjects\Intro\requirements.txt"

    def citeste_fisier_text(self):
        with open(file=self.file_path_txt, mode="r") as fisier:
            # pt. Json
            # Json.load(fisier)
            return json.load(fisier)

    def scriere_fisier(self):
        with open(self.file_path_txt, "a") as fisier:
            fisier.writelines("teste")


e = example_Json()
print(e.scriere_fisier())
#print(e.citeste_fisier_text())
[9:22 PM]
attrs==23.1.0
certifi==2023.7.22
cffi==1.16.0
decorator==5.1.1
h11==0.14.0
idna==3.4
outcome==1.3.0
pycparser==2.21
PySocks==1.7.1
selenium==4.14.0
self==2020.12.3
sniffio==1.3.0
sortedcontainers==2.4.0
trio==0.22.2
trio-websocket==0.11.1
urllib3==2.0.7
wsproto==1.2.0
整瑳瑥獥整