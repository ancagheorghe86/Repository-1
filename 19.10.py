# '''import mysql.connector
# mydb = mysql.connector.connect(host="aaa", user="bbb", password="ccc")
# mydb.execute("SHOW DATABASES")'''
# '''si uite asa folosesti mysql cu python'''
#

from abc import ABC, abstractmethod
# mostenire
# abstractizare
# incapsulare
# polimorfism
'''Cu cat copacul este mai stufos cu atat este mai frumos by Daniel Paun'''
# -> cu cat proiectul este mai stufos CONCEPTUALIZAT in 1. 2. 3. 4
# cu atat este mai FRUMOS (lizibil, usor de inteles, digerat de fiecare dev)
# NB: mai frumos sau stufos rezulta intr-o mai usoara adaugare de
# featureuri noi
class MInterface(ABC):
    @abstractmethod
    def descrie(self):
        raise NotImplementedError

    @abstractmethod
    def vopseste(self, culoare):
        raise NotImplementedError

    @abstractmethod
    def accelereaza(self, viteza):
        raise NotImplementedError


class Masina(MInterface):
    __culoare = "gri" #atribut privat -> modificam cu setter
    __viteza_actuala = 0 # atribut privat -> modificam cu setter
    culori_disponibile = ["gri", "albastru", "rosu"]
    marca = None # atribut public
    model = None # atribut public
    __viteza_maxima = None

    def __init__(self, model, viteza_maxima):
        self.__viteza_maxima = viteza_maxima
        self.model = model

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            self.__culoare = culoare
        else:
            raise Exception("culoarea introdusa nu exista")

    def descrie(self):
        # TODO: need to implement this method
        pass

    def accelereaza(self, viteza):
        if viteza >= 0 and viteza <= self.__viteza_maxima:
            self.__viteza_actuala = viteza
        else:
            raise NameError

    def get_viteza_actuala(self):
        return self.__viteza_actuala

    def get_culoare(self):
        return self.__culoare


m = Masina(model="toyota", viteza_maxima=220)
t = Masina(model="asda", viteza_maxima=300)
m.accelereaza(10)
print(m.get_viteza_actuala())
m.accelereaza(30)
print(m.get_viteza_actuala())
#m.vopseste("asd")
m.vopseste("albastru")
print(m.get_culoare())

# 1. mostenire
# 2. abstractizare
# 3. incapsulare
# 4. polimorfism

# "Cu cat copacul este mai stufos cu atat este mai frumos" by Daniel Paun
# -> cu cat proiectul este mai stufos CONCEPTUALIZAT in 1. 2. 3. 4
# cu atat este mai FRUMOS (lizibil, usor de inteles, digerat de fiecare dev)
# NB: mai frumos sau stufos rezulta intr-o mai usoara adaugare de
#   featureuri noi


class MInterface(ABC):
    @abstractmethod
    def descrie(self):
        raise NotImplementedError

    @abstractmethod
    def vopseste(self, culoare):
        raise NotImplementedError

    @abstractmethod
    def accelereaza(self, viteza):
        raise NotImplementedError


class Masina(MInterface):
    __culoare = "gri" #atribut privat -> modificam cu setter
    __viteza_actuala = 0 # atribut privat -> modificam cu setter
    __culori_disponibile = ["gri", "albastru", "rosu"]
    marca = None # atribut public
    model = None # atribut public
    __viteza_maxima = None

    def __init__(self, model, viteza_maxima):
        self.__viteza_maxima = viteza_maxima
        self.model = model

    def vopseste(self, culoare):
        if culoare in self.__culori_disponibile:
            self.__culoare = culoare
        else:
            raise Exception("culoarea introdusa nu exista")

    def descrie(self):
        # TODO: need to implement this method
        pass

    def accelereaza(self, viteza):
        if viteza >= 0 and viteza <= self.__viteza_maxima:
            self.__viteza_actuala = viteza
        else:
            raise NameError

    def get_viteza_actuala(self):
        return self.__viteza_actuala

    def get_culoare(self):
        return self.__culoare


m = Masina(model="toyota", viteza_maxima=220)
t = Masina(model="asda", viteza_maxima=300)
m.accelereaza(10)
print(m.get_viteza_actuala())
m.accelereaza(30)
print(m.get_viteza_actuala())
# m.vopseste("asd")
m.vopseste("albastru")
print(m.get_culoare())

from abc import ABC, abstractmethod


class Animal(ABC):
    """CLASA DE TIP INTERFATA, TIPAR pentru viitoarele clase
    ce mostenesc """
    @abstractmethod
    def sound(self):
        raise NotImplementedError

    @abstractmethod
    def sleep(self):
        raise NotImplementedError

    @abstractmethod
    def __get_all(self):
        raise NotImplementedError


class Dog(Animal):
    __name = "gigel"
    def sound(self):
        pass

    def sleep(self):
        raise NotImplementedError

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if self.__check_name(name):
            self.__name = name
        # raise NameNotRespectConditionsERROR

        # functie pentru a ma asigura
        # ca name respecta anumite reguli
    def __check_name(self, name):
        if name == "":
            return False
        if len(name) <= 5:
            return False
        return True


d = Dog()
d.set_name("Asdasdasd")

dog = Dog()
dog.get_all()
