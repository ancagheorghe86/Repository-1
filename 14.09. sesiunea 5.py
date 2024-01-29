# # # # # # ss = ["oaiealba", "oaiealba", "oaieneagra", "oaienagra"] #lista - afiseaza duplicatele
# # # # # # ff = {3, 4, 5, 5, 5} #set - nu afiseaza duplicatele
# # # # # # # print(ss, ff)
# # # # # #
# # # # # # # print(set(ss)) # am transormat lista in set si ne afiseaza elementele unice
# # # # # # # print(list(ff)) # am trasnformat setul in lista dar el ne afiseaza tot datele unice pentru ca era set
# # # # # #
# # # # # # count_negre = 0
# # # # # # count_albe = 0
# # # # # # count_oi = 0
# # # # # #
# # # # # # for element in ss:
# # # # # #     if element == "oaieneagra" or element == "oaiealba" :
# # # # # #         count_oi += 1
# # # # # #
# # # # # # print(f"oi albe: {count_oi}")
# # # # #
# # # # #
# # # # # ss = ("12", "24", "111111", "131")
# # # # # print(ss)
# # # # #
# # # # # count = 0
# # # # # for element in ss:
# # # # #     print(element)
# # # # #     if "11" in ss:
# # # # #         count = count + 1
# # # # #
# # # # # print (f'l-am gasit pe 1 de {count} ori')
# # # #
# # # # lista = ["3", "4", "5", "33", 4, 3, 3]
# # # # string = "123456"
# # # # s = "3"
# # # # if s in string:  # stringul "3" intr-un string "123456"
# # # #     # se ia primul string si se cauta in interiorul celui de-al doilea string
# # # #     print(f"l-am gasit pe {s} in {string}")
# # # #
# # # # if s in lista:
# # # #     # "3 in "3" "4" "5"
# # # #     # se cauta primul element(oricare tip de variabila ar fi) si se cauta in lista noastra
# # # #     print("l-am gasit in lista")
# # #
# # # l1 = [3,2, 0, 2]
# # # l2 = [6,5,4]
# # #
# # # l1.extend(l2)
# # # l3 = l1 + l2
# # #
# # # print(l3)
# # #                 # muta 0 la inceputul listei
# # #                 # se face cu for
# # # if len(l3) > 0:
# # #     print("lista nu este goala")
# # # else:
# # #     print("lista este goala")
# # #
# # # l3.clear() # sterge continutul
# # # # del l3 # sterge lista cu totul
# # #
# # #
# # dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' :5}
# #
# # # for element in dict1:
# # #     print(element)
# # #
# # # for key in dict1:
# # #     # print(key)
# # #     print(key, dict1[key])
# #
# # dict1['Dorel'] = 6
# # print(dict1)
# #
# # dict1.pop("Gigel")
# # print(dict1)
# #
#
zile_sapt = {'luni', 'marti', 'miercuri', "joi", "vineri", "sambata", "duminica"}
weekend = {"sambata", "duminica"}
#
# zile_sapt.add("luni")
# zile_sapt.add("luni")
# print(zile_sapt)
#
# # 14.Folosește un if și verifică dacă:
# # Weekend este un subset al zilelor din săptămânii.
# # Weekend nu este un subset al zilelor din săptămânii.
#
# if weekend.issubset(zile_sapt):
#     print("este subset")
# else:
#     print("nu este subset")
#
print(zile_sapt - weekend) #sau
print(zile_sapt.intersection(weekend))
