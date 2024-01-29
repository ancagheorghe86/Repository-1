from datetime import date

# exemplu de variabila CONSTANTA(ce nu se schimba pe parcursul programului)
DATABASE_URL = "https://mydb.com"
USER = ""
PAROLA = ""


class Om:
    nume = None
    varsta = None
    greutate = None
    data_nastere = None

    def __init__(self, nume, varsta, greutate, data_nastere):
        print("sunt in constructorul om")
        self.nume = nume
        self.varsta = varsta
        self.greutate = greutate
        self.data_nastere = data_nastere

    def print_self(self):
        print("sunt in functia print self \n")
        print(self.nume, self.data_nastere, self.greutate, self.varsta)

    def __str__(self):
        return f"{self.nume}, {self.data_nastere}"


class Sofer:
    conduce_auto = None

    def __init__(self, conduce_auto):
        print("sunt in constructorul sofer")
        self.conduce_auto = conduce_auto


# intre cele doua paranteze din definirea clasei mentionam pe cine mostenim
# clasa Chef va mosteni atributele si metodele clasei Om
class Chef(Om, Sofer):
    """
    mostenirea ne permite sa avem acces la atributele si functiile clasei
    parinte(superioare)
    """
    def __init__(self, nume, greutate, varsta, data_nastere, conduce):
        print("sunt in constructorul chef")
        Om.__init__(self, nume=nume, varsta=varsta, greutate=greutate, data_nastere=data_nastere)
        Sofer.__init__(self, conduce_auto=conduce)

    def make_salad(self):
        print("Am facut salata!")

    def make_fries(self):
        print("Am facut cartofii")

    def make_dishes(self):
        print("Am spalat vasele!")


class JapaneseChef(Chef):
    sushi_level = None

    def __init__(self, nume, varsta, greutate, data_nastere, sushi_level, conduce):
        # apelam obligatoriu constructorul din clasa parinte(superioara)
        print("sunt in constructorul japanese chef")
        super(JapaneseChef, self).__init__(
            nume=nume,
            varsta=varsta,
            greutate=greutate,
            data_nastere=data_nastere,
            conduce=conduce
        )
        self.sushi_level = sushi_level

    def make_sushi(self):
        print("sushi")


class ItalianChef(Chef):
    def make_pizza(self):
        print("pizza")

#
# bucatar = Chef(nume="dan", varsta="24", greutate="75", data_nastere="03.03.03")
# bucatar.print_self()

japan_chef = JapaneseChef("andrei", 23, 234, "03.03.03", 100, conduce=True)
japan_chef.print_self()