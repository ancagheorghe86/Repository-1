class Om:
    nume = None
    varsta = None
    greutate = None
    data_nastere = None

    # apoi ni se asigneaza niste valori :

def __init__(self, nume, varsta, greutate, data_nastere):
    # print("sunt in constructor")
    self.nume = str(input(f"Spune numele"))
    self.varsta = int(input(f' Scrie varsta omului'))
    self.greutate = int(input(f' Trece greutatea: '))
    self.data_nastere = data_nastere
    print(f"am atribuit {nume} {varsta} {greutate} {data_nastere}")

def print_self(self):
   # print("sunt in functia print self \n")
   print(self.nume, self.data_nastere, self.greutate, self.varsta)

def __str__(self):
    self.nume = nume
    self.varsta = varsta
    self.greutate = greutate

    return f"{self.nume}, {self.data_nastere}"

# intre cele doua paranteze din definirea clasei, mentionam pe cine mostenim
# clasa chef va mosteni atributele si metodele clasei Om
class Chef(Om):

    def make_salad(self):
        print("Am facut salata!")

    def make_fries(self):
        print("Am facut cartofi")

    def make_dishes(self):
        print("Am spalat vasele")

class JapaneseChef(Chef):
    sushi_level = 18
    def make_pizza(self):
        print("sushi")

class ItalianChef(Chef):
    def make_pizza(self):
        print("pizza")

bucatar = Chef(nume="dan", varsta="24", greutate="75", data_nastere="03.03.2023")
bucatar.print_self()

japan_chef = JapaneseChef("andrei", 23, 234, "03.03.2003")
japan_chef.print_self()
