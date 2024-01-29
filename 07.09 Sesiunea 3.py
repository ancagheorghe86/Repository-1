# x = input("enter number:")
# x = int(x)
#
# '''% - modulo
# este restul impartirii'''
#
# if x % 2 == 0:  # daca numarul se imparte exact la 2
#     print(f'rest: {x%2}')
#     print(f'numarul {x} este par')
# else:
#     print(f'rest: {x%2}')
#     print(f'numarul {x} este impar')

# if x % 3 == 0:  # daca numarul se imparte exact la 3
#     print(f"rest: {x%2}")
#     print(f"numarul {x} este divizibil cu 3")
# else:
#     print(f"rest: {x % 2}")
#     print(f"numarul {x} este par")
#

'''14.      x, y, z (int)
Afișează care este cel mai mare dintre ele?'''

# x = input("x = ")
# x = int(x)
#
# y = input("y =")
# y = int(y)
#
# z = input("z= ")
# z = int(z)
#
# # print(x, y, z)
#
# max = 90
# 35 1 4 6 9 6 89 90 86 11

if x >= y and x >= z:
    print('x=', x)
elif y >= x and y >= z:
    print('y=', y)
elif z >= x and z >= y:
    print('z=', z)
#
#
#
'''10.Transformă și printează notele din sistem românesc în  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F'''

# nota = float(input('nota: '))

# if nota < 0:
#     nota = nota * -1
#     print(nota)

# if nota >= 9:
#     print('A')
# elif nota >= 8:
#     print('B')
# elif nota >= 7:
#     print('C')
# elif nota >= 6:
#     print('D')
# elif nota > 4:
#     print('E')
# elif nota <= 4:
#     print('F')

'''14.Exercițiu:
citește un user de la tastatură;
citește o parolă;
afișează: 'Parola pt user x este ***** și are x caractere';
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.

eg: parola abc => ***
      parola abcd => ****'''

# user = input('user: ')
# parola = input("parola: ")
# lenght = len(parola)
#
# p = 5 * "%"
# print(p)
# print(f"userul {user} are parola {lenght * '*'}")    # varianta 1 - o sa puna cate o steluta pentru fiecare caracter al parolei
# print(f"userul {user} are parola {p}")               # varianta 2 -  o sa puna % de 5 ori, asa cum noi l-am definit pe "p"
#
#

# 1. introduceti un string de la tastatura. verificati daca acesta contine numere.


litera = input('introduce o litera: ')
vocale = 'aeiou'

if litera in vocale:
    print('este vocala')
else:
    print("este consoana")

# string - este o lista de caractere
# operatorul "in" face o verificare daca inputul din litera se afla in al doilea element "vocala"


