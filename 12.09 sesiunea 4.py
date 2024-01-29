# # # # # lista = [1, 2, "sfsf", True]
# # # # # print(lista[3]) #printeaza al treilea element din lista "true" ; lista incepe de la 0 (numarul 1)
# # # # #
# # # # # lista = [1, 2, "sfsf", True]
# # # # # print(lista[-1]) #asa printam ultimul element din lista respectiva; -1 incepe numaratoarea de la coada
# # # #
# # # # # lista = [1, 2, "sfsf", True]
# # # # # print(lista[-3]) #asa printam ultimul element din lista respectiva; -1 incepe numaratoarea de la coada
# # # # #
# # # # # # daca incepem numaatoarea in lista incepem cu 0, daca vrem sa inceapa numaratoarea de la coada scriem -1(ultimul), -2 (penultimul, etc
# # # # #
# # # # # nn = None
# # # # # print(type(nn))
# # # #
# # # # # SLIICING :
# # # # lista = [1, 2, "sfsf", True, 5, 9]
# # # # print(lista[3:5]) # al cincilea element, 9, nu il ia in calcul
# # # # print(lista[0:5:2]) # din 2 in 2
# # # # print(lista[0:5:3]) # din 3 in 3
# # #
# # # # DICTIONAR :
# # # # mydict = {
# # # #     "qwe":34,
# # # #     "2324": "pdhjdded",
# # # #
# # # # }
# # # # print(mydict["2324"]) #ii specificam cheia, e atunci cand vrei sa ajungi la o valoare specificandu-i cheia
# # # #
# # # # mydict["a"] = "dedfedf" # i-am adaugat o cheie in dicionar
# # # # print(mydict)
# # #
# # # # ll = mydict.values() #printam valorile cheilor
# # # # print(list(ll))
# # # #
# # # #
# # # # mydict = {
# # # #     "masini": {
# # # #         "brand": [1, 2, 3]
# # # #     }
# # # # }
# # # # print
# # #
# # # # matrice = un tabel = o lista in lista
# # # matrice = [
# # #     [1, 2, 3],
# # #     [4, 5, 6],
# # #     {"1":2, "3":4},
# # #     "1231452"
# # # ]
# # # print(matrice[2]['3'])
# #
# # # SET
# # # ss = {1, 2, 3, 3, 3}
# # # ff = {3, 4, 5}
# # #print(ss, ff)
# # #print(ss.difference(ff)) # ne afiseaza diferentele dintre cele doua liste
# # #print(ss.intersection(ff)) # ne afiseaza elementele comuune dintre cele doua liste
# #
# # ss = [1, 2, 3, 3, 3]
# # ff = [3, 4, 5]
# # print(set(ss) - set(ff)) #diferenta dintre cele doua liste
# #
# #
# # TUPLE:
# # thistuple = ("apple", "banane", "cherry")
# # print(thistuple)
# # print(len(thistuple))
#
ss = [1, 2, 3, 3, 3] #lista - afiseaza duplicatele
ff = {3, 4, 5, 5, 5} #set - nu afiseaza duplicatele
# print(ss, ff)

# print(set(ss)) # am transormat lista in set si ne afiseaza elementele unice
# print(list(ff)) # am trasnformat setul in lista dar el ne afiseaza tot datele unice pentru ca era set

# count = 0
# for element in ss:
#  if element = 3:
#      print("l-am gasit pe 3")
#     count = count + 1  # count ++
# print(f"L-am gasit pe 3 de {count} ori")

