'''1.Clasa Cerc
    Atribute: rază, culoare
    Constructor pentru ambele atribute
    Metode:
descrie_cerc() - va PRINTA culoarea și raza
aria() - va RETURNA aria
diametru()
circumferinta()
'''

import math

class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f"Cercul are raza {self.raza} și culoarea {self.culoare}.")

    def aria(self):
        return math.pi * self.raza**2

    def diametru(self):
        return 2 * self.raza

    def circumferinta(self):
        return 2 * math.pi * self.raza

# Exemplu de utilizare:
cerc1 = Cerc(5, "rosu")
cerc1.descrie_cerc()
print(f"Aria cercului este: {cerc1.aria()}")
print(f"Diametrul cercului este: {cerc1.diametru()}")
print(f"Circumferinta cercului este: {cerc1.circumferinta()}")

'''Clasa Dreptunghi
     Atribute: lungime, lățime, culoare
     Constructor pentru toate atributele
     Metode:
descrie()
aria()
perimetrul()
schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare. Poți verifica schimbarea culorii prin apelarea metodei descrie().
'''
class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f"Dreptunghiul are lungimea {self.lungime}, lățimea {self.latime} și culoarea {self.culoare}.")

    def aria(self):
        return self.lungime * self.latime

    def perimetrul(self):
        return 2 * (self.lungime + self.latime)

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare
        print(f"Culoarea dreptunghiului a fost schimbată în {noua_culoare}.")

# Exemplu de utilizare:
dreptunghi1 = Dreptunghi(5, 3, "albastru")
dreptunghi1.descrie()
print(f"Aria dreptunghiului este: {dreptunghi1.aria()}")
print(f"Perimetrul dreptunghiului este: {dreptunghi1.perimetrul()}")
dreptunghi1.schimba_culoarea("verde")
dreptunghi1.descrie()