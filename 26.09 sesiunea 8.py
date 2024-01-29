# # # # # BUBLE SORT
# # # cars = ['Audi', 'Volvo', 'Bmw', 'Mercedes', 'Aston Martin']
# # # #
# # #
# # #
# # # # def suma2nr(a, b):
# # # #     # print(a + b)
# # # #     suma = a + b
# # # #     return suma
# # # # gigel = suma2nr(2, 5)
# # # # dorel = suma2nr(3, 9)
# # # # print(gigel)
# # # # print(dorel)
# # # #
# # # # # suma2nr(2,5)
# # #
# # # def print_cars(cars=["a", "b"]):
# # #     print(cars)
# # #
# # # # def print_cars_reversed(cars):
# # # #     print("lista masini: ", cars[::-1])
# # #
# # # lista = ['Audi', 'Volvo', 'Bmw', 'Mercedes', 'Aston Martin']
# # #
# # # print_cars(cars=lista)
# #
# #
# Exercitii:

# 1.Funcție care să calculeze și să returneze suma a două numere

# def sum_2_nr(nr1, nr2):
#     suma = nr1 + nr2
#     return suma
# print(sum_2_nr(1,2))

# sau:
# a = int(input("introdu nr. 1: "))
# b = int(input("introdu nr. 2: "))
# print(sum_2_nr(a, b))
# print((sum_2_nr(1,8)))
# print(sum_2_nr(5, 37))
# print(sum_2_nr(123123, 3462345))
# print(sum_2_nr(2365425, 365489))
#
#
# def is par(nr):
#     if nr % 2 == 0:
#     return True
#     else:                     # gresit
#     return False
#     print(is_par(56))


# def total_chars(nume, prenume, nume_mijlociu):
#     total = len(nume) + len(prenume) + len(nume_mijlociu)
#     return total                                                      # OK
#
# print(total_chars(nume="anca", prenume='andreea', nume_mijlociu='gheorghe'))

#
# def aria_dreptunghiului(lungimea, latimea):
#     aria = lungimea * latimea
#     return aria
# print(aria_dreptunghiului(50,100))
#
# def aria_cercului(raza):
#     pi = 3.14
#     aria = pi * raza * raza
#     return aria
# print(aria_cercului(50))

# https://www.w3schools.com/python/ref_math_pi.asp

'''6. Funcție care returnează True dacă un caracter x se găsește
 într-un string dat și False dacă nu găsește'''

# def cauta(str1, str2):
#     if str1 in str2:
#         return True
#     else:
#         return False
# print(cauta("1","21")) # adica caracterul 1 se gaseste in adunatura 21

'''7. Funcție fără return, primește un string și printează pe ecran:
Numărul de caractere lower case este x
Numărul de caractere upper case exte y 
'''

# def num_upp_low(string):
#     up_count = 0
#     low_count = 0
#     for char in string:
#         if str(char).isalpha():
#             if str(char).isupper():
#                 up_count += 1
#
#             else:
#                 low_count += 1
#
#     print(f'Lower characters found: {low_count}')
#     print(f'Upper characters found: {up_count}')

def numar_mare_mic(x):
    numar_mare = 0
    numar_mic = 0
    for char in x:
        if str(char).islower():
            numar_mic = numar_mic + 1
        elif str(char).isupper():
            numar_mare = numar_mare+1
        else:
            continue
    print(f'Am gasit atatte litere scrise cu majuscule: {numar_mare}')
    print(f'Am gasit atatte litere scrise cu minuscule: {numar_mic}')
numar_mare_mic("HeLLo WorLD 77")
