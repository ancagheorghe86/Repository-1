'''Calculator pentru Indicele de Masă Corporală (IMC):

Solicită utilizatorului să introducă greutatea (în kilograme) și înălțimea (în metri).
Calculează IMC folosind formula: IMC = greutate / (înălțime * înălțime).
Afișează rezultatul.'''

# greutatea = int(input(f"Ce greutate ai ? __"))
# inaltimea = int(input(f"Ce inaltime ai ? __"))
# IMC = greutatea / (inaltimea * inaltimea)
# print(IMC)

'''Convertor Valutar Simplu:

Solicită utilizatorului să introducă o sumă de bani într-o anumită monedă.
Creează variabile pentru ratele de schimb (de exemplu, EUR la USD, USD la GBP).
Converteste suma în alte două monede și afișează rezultatele.'''

# suma = int(input(f'Ce suma de bani ai?'))
# moneda = input(f'Ce moneda vrei sa cumperi? ')
# euro = suma/4.5
# dolar = suma/4
# gbp = suma/6
# if moneda := euro:
#     print(f'Felicitari! ai cumparat {euro} euro')
# elif moneda := dolar:
#     print(f'Felicitari! ai cumparat {dolar} dolari')
# else:
#     print(f'Felicitari! ai cumparat {gbp} gbp')

'''Gestionați un Catalog de Cărți:

Creați variabile pentru titlu, autor și anul publicării unei cărți.
Afișați aceste informații sub forma unui șir de text bine format.'''

# titlu = 'Colt alb'
# autor = 'autor'
# anul_publicarii = 1950
# print(f'Recent am citit {titlu}, scrisa de {autor}, pulicata in anul {anul_publicarii}')

'''Calculul Cheltuielilor:

Solicită utilizatorului să introducă suma totală a cheltuielilor și numărul de persoane care împart aceste cheltuieli.
Calculează cât ar trebui să plătească fiecare persoană.'''

# suma = float(input(f"Ce suma ai cheltuit? "))
# nr_persoane = int(input(f'Cate persoane sunteti? '))
# suma_per_persoana = suma / nr_persoane
# print(suma_per_persoana)

'''Numere Pare și Impare:

Solicită utilizatorului să introducă un număr.
Verifică dacă numărul este par sau impar și afișează un mesaj corespunzător.'''

# numar = int(input(f'Spune-mi un numar'))
# if numar % 2 == 0:
#     print(f'Ai ales un numar par')
# else:
#     print(f"ai ales un numar impar")

'''Lista cu Bucle:

Creează o listă de cel puțin șapte numere.
Utilizează un buclu for pentru a afișa fiecare număr din listă.'''

# lista = [1, 2, 3, 4, 5, 6, 7]
# for i in lista:
#     print(i)

'''Contorizarea Caracterelor:

Solicită utilizatorului să introducă un șir de caractere.
Numără câte litere mici, litere mari și cifre sunt în șir.'''

# parola = input(f"scrie o parola")
#
# litere_mici = 0
# litere_mari = 0
# cifre = 0
#
# for i in parola:
#     if i.islower():
#         litere_mici +=1
#     elif i.isupper():
#         litere_mari += 1
#     elif i.isdigit():
#         cifre +=1
# print(f"Parola ta contine {litere_mici} litere mici, {litere_mari} litere mari si {cifre} cifre")

'''Construirea unei liste:

Creează o listă goală.
Solicită utilizatorului să introducă 5 numere și adaugă-le în listă.
Afișează lista rezultată.'''

# lista = []
# for _ in range(5):
#     continut_lista = int(input("Scrie un număr: "))
#     lista.append(continut_lista)
#
# print(lista)

'''Verificare Parolă:

Solicită utilizatorului să introducă o parolă.
Verifică dacă parola îndeplinește următoarele condiții: 
conține cel puțin 8 caractere, cel puțin o literă mare și cel puțin un număr.'''

parola = input(f'scrie o parola')
caractere = 0
litera_mare = 0
numar = 0
for i in parola:
   if i.islower():
       caractere +=1
   elif i.isupper():
       litera_mare += 1
   elif i.isdigit():
        numar += 1
print(f'parola e ok')

