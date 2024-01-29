# # # # # 5. Modernizează parcul de mașini:
# # # # #
# # # # # Crează o listă goală, masini_vechi.
# # # # # Iterează prin mașini.
# # # # # Când găsesti Lăstun sau Trabant:
# # # # # Salvează aceste mașini în masini_vechi.
# # # # # Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# # # # # Printează Modele vechi: x.
# # # # # Modele noi: x.
# # # # #
# # # masini = ['Audi','Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# # # #
# # # # wanted = ['Lastun', 'Trabant']
# # # # masini_vechi = []
# # # #
# # # # for index, masina in enumerate(masini):
# # # #     if masina == "Lastun" or masina == "Trabant":
# # # #     # if masina in wanted:
# # # #         masini_vechi.append(masini[index])
# # # #         masini[index] = "Tesla"
# # # #
# # # # print(masini)
# # # #
# # #
# # # # 6. Având dict:
# # # pret_masini = {
# # #     'Dacia': 6800,
# # #      'Lăstun': 500,
# # #      'Opel': 1100,
# # #      'Audi': 19000,
# # #      'BMW': 23000
# # # }
# # # #
# # # # Vine un client cu un buget de 15000 euro.
# # # #
# # # # Prezintă doar mașinile care se încadrează în acest buget.
# # # # Iterează prin dict.items() și accesează mașina și prețul.
# # # # Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
# # # # Iterează prin listă.
# # #
# # # for key, value in pret_masini.items():
# # #     # print(key, value) asa printam tot
# # #     if value <= 15000:
# # #         print (f"Puteti alege masina {key}")
# # #
# #
# # # 7. Având lista:
# # numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# # # Iterează prin ea.
# # # Afișează de câte ori apare 3 (nu ai voie să folosești count)
# #
# # # counter = 0
# # # for nr in numere:
# # #     if nr == 3:
# # #         counter += 1
# # # print(counter)
# #
# # #suma numerelor:
# # # suma = 0
# # # for nr in numere:
# # #     suma += nr
# # # print(suma)
# #
# # #cel mai mare numar:
# # max = -10000
# # for nr in numere:
# #     if nr > max:
# #         max = nr
# # print(max)
# #
# # #cel mai mic numar:
# # min = 10000
# # for nr in numere:
# #     if nr < min:
# #         min = nr
# # print(min)
# #
# # # Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# # for index, nr in enumerate(numere):
# #     if nr > 0:
# #         numere[index] = nr * -1
# # print(numere)
#
# '''11.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișează cele 4 liste la final
# '''
# # alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# # pare = []  # %2 == 0
# # impare = []  # %2 != 0
# # pozitive = [] # > 0
# # negative = [] # < 0
# # #
# # for nr in alte_numere:
# #     if nr % 2 == 0:
# #         pare.append(nr)
# #     if nr % 2 != 0:
# #         impare.append(nr)
# #     if nr > 0:
# #         pozitive.append(nr)
# #     if nr < 0:
# #         negative.append(nr)
# # print(pare)
# # print(impare)
# # print(pozitive)
# # print(negative)
#
# #alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
#
#
# # problema de SORTARE, cautare
#
# '''
# Bubble sort
# pas 1 - compar elementul cu indexul 0 cu tot ce urmeaza dupa el
# pana la finalul listei
# pas 2 - compar elementul cu indexul 1 cu tot ce urmaza dupa el,
# panala finalul listei
# pas 3 - compar elementul cu indexul 2 cu tot ce urmaza dupa el,
# panala finalul listei, pana la le(lista)
# .
# .
# .
# pana la len(lista)
# '''
# # a = 1
# # b = 2
# # aux = 0
# #
# # aux = a
# # a = b
# # b = aux
# # # sau mai eficient:
# # a, b = b, a
#
# def suma_lista(lista):
#     suma = 0
#     for nr in lista:
#         suma += nr
#     return suma
#
#
#
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# #sortarea numerelor dintr-o lista:
# #pasii 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# for i in range(len(alte_numere)):
#     for j in range(i+1, len(alte_numere)):
#         if alte_numere[i] > alte_numere[j]:
#             aux = alte_numere[i]
#             alte_numere[i] = alte_numere[j]
#             alte_numere[j] = aux
#
# print(alte_numere)
#
# s = suma_lista(alte_numere)
# print(s)
#

# 13. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
#    User alege un număr
#    Programul îi spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitări! Ai ghicit!

import random

numar_secret = random.randint(1,30)
numar_ghicit = None
while numar_secret != numar_ghicit:
    numar_ghicit = int(input("Alege numar: "))
    if numar_ghicit > numar_secret:
        print("Nr. introdus este prea mare")
    elif numar_ghicit < numar_secret:
        print(' Nr introdus este prea mic')
    else:
        print("Felicitari! Ai ghicit! ")

