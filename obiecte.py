# # lista1 = [1,2,3]
# # lista2 = [4,5,6]
# # lista3 = list
# #
# # print(type(lista1), type(lista2), type(lista3))
#
# class Car:
#     make = 'Dacia'
#     model = None
#     year = 2022
#     color = None
#     viteza = 0
#
#     def accelerate(self):
#         print("vrum, vrum", self.viteza)
#         self.viteza = self.viteza + 10
#
#     def print_self(self):
#         print(self.make, self.year, self.viteza)
#
#
#     def stop(self):
#         print("Stop!")
#         self.viteza = 0
#
# car1 = Car()
# car2 = Car()
# # print(car1.make, car1.year)
# # print(car2.make, car2.year)
# # print(car1.make, car1.year, car1.viteza)
# car1.print_self()
# car1.accelerate()
# car1.accelerate()
# car1.accelerate()
# car1.accelerate()
# car1.accelerate()
# car1.print_self()
#
#
#
#
# # car1.stop()
#
# class Client:
#     user = "daniel"
#     parola = "sdfferf"
#
#     def ascunde_parola(self):
#         self.parola = len(self.parola) * "*"
#
# print(Client.user)
# print(Client.parola)
# client1 = Client()
# client1.ascunde_parola()
# client1.afiseaza_parola()

from datetime import date
class Om:
    nume = None
    varsta = None
    greutate = None
    data_nastere = None

    #apoi ni se asigneaza niste valori :

    def __init__(self, nume, varsta, greutate, data_nastere):
        #print("sunt in constructor")
        self.nume = str(input(f"Spune numele"))
        self.varsta = int(input(f' Scrie varsta omului'))
        self.greutate = int(input(f' Trece greutatea: '))
        self.data_nastere = data_nastere
        print(f"am atribuit {nume} {varsta} {greutate} {data_nastere}")

    def print_self(self):
        #print("sunt in functia print self \n")
        print(self.nume, self.data_nastere, self.greutate, self. varsta)

    def __str__(self):
        return f"{self.nume}, {self.data_nastere}"

om1 = Om("Daniel", 0, 3.200, date.today())
om2 = Om("Rares", 32, 86, date.today())
om1.print_self()
om2.print_self()


#print("\n") # se va lasa un rand liber intre randuri
