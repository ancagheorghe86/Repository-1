# import math
#
# r = float(input('Introdu raza cercului: '))
# culoare = str(input('Culoarea preferata: '))
# class Circle:
#     raza = None
#     culoare = None
#
#     def __init__(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#     def print_self(self):
#         print(self.raza, self.culoare)
#
#     def diametru(self):
#         d = 2 * self.raza
#         return d
#     def circumferinta(self):
#         c = 2 * math.pi * self.raza
#         return c
#
#     def aria(self):
#         a = math.pi * (self.raza * self.raza)
#         return a
#
# my_circle = Circle(raza=r, culoare=culoare)
# my_circle.print_self()
#
#
# print(my_circle.circumferinta())
# print(my_circle.diametru())
# print(my_circle.aria())

''' Clasa Dreptunghi
     Atribute: lungime, lățime, culoare
     Constructor pentru toate atributele
     Metode:
descrie()
aria()
perimetrul()
schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare.
Poți verifica schimbarea culorii prin apelarea metodei descrie().
'''

#exemplu de variabila constanta, ce nu se schimba pe parcursul programului (se scriu cu majuscule):
# DATABASE_URL = "https://mydb.com
class Dreptunghi:
    lungime = None
    latime = None
    culoare = None

    def __init__(self, lungime, latime, culoare):
        #self ne va ajuta sa assignam valori atributelor obiectului curent
        #(obiectivelor viitoare)

        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        ''' printeaza toate atributele din obiectul curent(self)'''
        print(f"Lungime: {self.lungime}"
              f"latime {self.latime}"
              f"culoare {self.culoare}")
        pass
    def aria(self):
        aria = self.latime * self.lungime
        return aria

    def perimetru(self):
        perimetru = 2 * self.lungime + 2 * self.latime
        return perimetru

    def schimba_culoarea(self, noua_culoare):
        # această metodă nu returneaza nimic.
        # Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare.
        # Poți verifica schimbarea culorii prin apelarea metodei descrie().
        self.culoare = noua_culoare

lungime = float(input(f"Scrie lungimea: "))
latime = float(input(f"Scrie latimea:"))
culoare = input(f"Scrie culoare:")
my_dreptunghi = Dreptunghi(lungime=lungime, latime=latime, culoare=culoare)
my_dreptunghi.descriere()
print(my_dreptunghi.aria())

noua_culoare = input("spune-mi noua culoare: ")

my_dreptunghi.schimba_culoarea(noua_culoare=noua_culoare)
my_dreptunghi.descriere()