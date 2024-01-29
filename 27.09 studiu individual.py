# a = 40
# b = 30
# a, b = b, a
# print(f"a=", a)
# print(f"b=", b)

'''Carl Friedrich Gauss a fost un matematician german renumit
pentru realizările sale științifice. Printre acestea,
ne-a arătat faptul că suma primelor n numere naturale se poate
calcula folosind formula: n = (n * (n + 1))/2

'''
# n = int(input('introdu un numar: '))
# suma_n = (n*(n+1))/2
# print(suma_n)

'''2. Se citesc de la tastatură două cifre nenule și diferite. 
Afișați cele două numere care se pot realiza cu aceste cifre.'''

# nr1 = int(input('introdu un numar: '))
# nr2 = int(input('mai introdu un numar: '))
# a = (nr1*10)+nr2
# b = (nr2*10)+nr1
# print(a)
# print(b)

'''3. Realizați un program care citește de la tastatură două numere 
naturale nenule și afișează suma, diferența, produsul, câtul și restul 
împărțirii lor.
'''
# nr_1 = int(input('scrie un numar: '))
# nr_2 = int(input('mai scrie un numar: '))
# suma:
# if nr_1 >= 1 and nr_2>=1:
#     print(nr_1+nr_2)
# else:
#     print('nu ai introdus numere nenule, mai incearca: ')

# diferenta:
# if nr_1 >= 1 and nr_2>=1:
#     print(nr_1-nr_2)
# else:
#     print('nu ai introdus numere nenule, mai incearca: ')

# produsul:
# if nr_1 >= 1 and nr_2>=1:
#     print(nr_1*nr_2)
# else:
#     print('nu ai introdus numere nenule, mai incearca: ')

# catul:
# if nr_1 >= 1 and nr_2>=1:
#     print(nr_1//nr_2)
# else:
#     print('nu ai introdus numere nenule, mai incearca: ')

# restul impartirii:
# if nr_1 >= 1 and nr_2>=1:
#     print(nr_1%nr_2)
# else:
#     print('nu ai introdus numere nenule, mai incearca: ')

'''4. Un dog german a alergat n ture de teren de tenis care are dimensiunile 
standard: 23.77m x 8.23m. Ce distanță a parcurs el?

Indicație. Atenție la perimetru. Se citește de la tastatură doar numărul de ture, notat cu n.'''

# lungime = 23.77
# latime = 8.23
# perimetru = (lungime*2)+(latime*2)
# ture = int(input(f'Cate ture a alergat cainele? : '))
# print(perimetru*ture)

'''5. Se citește un număr natural format din exact trei cifre. 
Afișați numărul care conține toate cifrele micșorate cu 1.

Exemplu. Pentru numărul 359, se va afișa 248.'''

# n = 359
# c1 = (n//100)-1
# c2 = ((n//10)%10)-1
# c3 = ((n%10))-1
# n2 = c1*100 + c2*10 + c3
# print('n2 este:', n2)

'''6. Se citește un număr natural format din exact două cifre. 
Afișați suma cuburilor cifrelor sale.
Exemplu. Pentru numărul 49, se va afișa 4**3 + 9**3, adică 793.'''

# n = int(input('Scrie un nr de doua cifre: ' ))
# n1 = (n//10)**3
# n2 = (n%10)**3
# if n >= 0:
#     print(n1+n2)
# else:
#     print("Numarul introdus nu este >=0. Mai incearca!")

'''7. Se citesc două numere naturale în variabilele x și y. 
Afișați valoarea expresiei: x2 + y2 - 23.'''

# x = int(input(f'Scrie un nr: '))
# y = int(input(f'Mai scrie un nr: '))
# rezultat = x**2 + y**2 - 23
# if x>=0 and y>=0:
#     print(rezultat)
# else:
#     print('Nu ai introdus numere >=0. Mai incearca!')

import turtle #importăm modulul
t = turtle.Turtle() #reținem țestoasa în t
t.color("red") #culoarea de desenare
t.forward(75) #înainte 75 de pixeli
t.left(90) #rotim 90 de grade
#repetăm mișcarea de încă 3 ori
t.forward(75)
t.left(90)
t.forward(75)
t.left(90)
t.forward(75)
t.left(90)
print("Gata primul nostru pătrat roșu!")


