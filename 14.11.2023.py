#design patterns
# cand avem nevoie de o singura instanta pe toto parccusul proiectului
# cum ar fi o baza de date sau o clasa utiulitara ce lucreaza cu fisiere
# instanta ce se instantiaza o singura data

class SingletonClass:
    __instanta = None
    bec = False

    #putem sa punem cate atribute vrem

    def __init__(self, sector):
        self.sector = sector

    def __init__(self, bec=False):
        self.bec = bec

    def __new__(cls, *args):
        if cls.__instanta is None:
            #acest obiect se instantiaza o singura data in a life time
            cls.__instanta = object.__new__()
        #de vreme ce instanta noastra a fost creata la inceput
        #urmatoarele instante vor fi identice cu aceasta
        return cls.__instanta
    def aprinde_bec(self):
        self.bec = True

    def stinge_bec(self):
        self.bec = False

    def __str__(self):
        string = "aprins" if self.bec else "stins"
        return f"becul este {string}"


instance1 = SingletonClass("IT")
instance2 = SingletonClass("IT")
instance3 = SingletonClass

# is verifica eglitatea a doua obiecte in totalitate (valoare dar si adresa de memorie)
if instance1 is instance2 and instance2 is instance3:
    print("toate instantele sunt la fel")
