'''Exercise 1: Accept numbers from a user
Write a program to accept two numbers from the user and calculate multiplication'''

# a = int(input("Alege un numar: "))
# b = int(input("Mai alege un numar"))
# multiplication = a * b
#
# print("Multiplication of this numbers is: ", multiplication)

'''Display three string “Name”, “Is”, “James” as “Name**Is**James”
Use the print() function to format the given words in the mentioned format. Display the ** separator between each string.'''
# print("Name", "is", "Jones", sep='**')

'''1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă. 
'''
# o variabila este un loc in memorie ce pastreaza valori, ca o cutiuta

'''2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă:
string
int 
float
bool
Observație: Valorile vor fi alese de tine după preferințe.
'''

name = 'Anca'
age = 37
age_2 = 37,5
blonda = False

'''3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
'''
# print(type(name))
# print(type(age))
# print(type(age_2))
# print(type(blonda))
# print(f'My name is {name} and I have {age} years old.')

'''Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
Verifică tipul acesteia.
'''

# age_2 = round(37.5)
# print(age_2)

'''5. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile. 
Rezolvă nepotrivirile de tip prin ce modalitate dorești.
'''
# print(f'Numele meu este {name}.')
# print(f'Am varsta de {age} ani.')

'''Citește de la tastatură:
numele;
prenumele.
    Afișează: 'Numele complet are x caractere'.
'''
# nume = (input("Scrie-ti numele : "))
# prenume = (input("Si prenumele: "))
# lungimea = len(nume)+ len(prenume)
# print('Numele complet are', lungimea, 'caractere')

'''Operatori, condiționale

Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe. 
X este un int.

1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
'''
# if else : daca o conditie este indeplinita se intampla ceva, in caz contrar se intampla altceva

'''2. Verifică și afișează dacă x este număr natural sau nu.
'''
'''Numerele naturale sunt numerele întregi strict pozitive'''

# x = input("Scrie un numar: ")
# if x > '0':
#     print(f'{x} este numar natural')
# else:
#     print('X nu este numar natural')

'''3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
'''
# if x > "0":
#     print('X este un numar pozitiv')
# elif x < "0":
#     print('x este un numar negativ')
# else:
#     print('x este un numar neutru')

'''4. Verifică și afișează dacă x este între -2 și 13.
'''
x = int(input('Alege un numar: '))
if x >= -2 and x < 13:
    print('x este intre -2 si 13')
else:
    print('x este in afara intervalului')