class Om:

    nume = None
    prenume = None
    inaltime = None

    def __init__(self, nume, prenume, inaltime):
        self.nume = nume
        self.prenume = prenume
        self.inaltime = inaltime

class Sofer:

    conduce = None

    def __init__(self, conduce):
        self.conduce = conduce

class Chef(Om, Sofer):

    face_cartofi = None

    def __init__(self, nume, prenume, inaltime, conduce, face_cartofi):
        Om.__init__(self, nume, prenume, inaltime)
        Sofer.__init__(self, conduce)
        self.face_cartofi = face_cartofi

class Super_chef(Chef):

    make_retete = None

    def __init__(self, nume, prenume, inaltime, conduce, face_cartofi, make_retete):
        super().__init__(nume, prenume, inaltime, conduce, face_cartofi)
        self.make_retete = make_retete

    def print_self(self):
        print(self.nume, self.prenume, self.inaltime, self.conduce, self.face_cartofi, self.make_retete)


super_chef1 = Super_chef ("Ion", "Ionel" , 180, "da1", "da2", "da3")

super_chef1.print_self()

class Animal:

    papuci = None

    def P(self, *args):
        for x in args:
            print(x)


    def urla(self):
        pass

class Caine(Animal):

    def urla(self):
        print("ham ham")

class Pisica(Animal):

    def urla(self):
        print("miau miau")

pisica1 = Pisica()
#
pisica1.urla()
#
caine1 = Caine()
#
caine1.urla()
animal1 = Animal()
animal1.P("asd", "123", "dsa")

