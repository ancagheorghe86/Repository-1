#
#
# def return_the_sixth(list):
#     try:
#         return list[6]
#     except IndexError as e:
#         # write error in logs here
#         print(e)
#         return list[-1]
#
# the_sixth = return_the_sixth([30, 20, 10])
# print(the_sixth)
#
# def divide(x, y):
#     try:
#         result = x // y
#     except ZeroDivisionError as e:
#         print(f'impartirea la zero nu este posibila' )
#         return -1
#     else:
#         print(f"divide done")
#         return result
#     finally:
#         print(f"acest cod se executa oricum")
#
# nr1 = int(input("nr1: "))
# nr2 = int(input("nr2: "))
#
# print(divide(nr1, nr2))

# def divide(x, y):
#     try:
#         result = x// y
#     except (ZeroDivisionError, ConnectionError):
#         print('asdjdk')
#         return -1
#     else:
#         print("divide done")
#         return result
# x = int(input("nr1: "))
# y = int(input("nr2: "))
#
# print(divide(x,y))

'''8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.'''
def pozitiv_only(lista):
    nr_pozitive = []
    for nr in lista:
        if nr > 0:
            nr_pozitive.append(nr)
    return nr_pozitive
listapozitive = pozitiv_only([1, 3, 5, -5, -7, 8])
print(listapozitive)


'''9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ
Primul număr x este mai mare decat al doilea număr y
Al doilea număr y este mai mare decat primul număr x
Numerele sunt egale. 
'''
def compare(x, y):
    if x > y:
        print(f'{x} este mai mare ca {y}')
    elif y > x:
        print(f'{y} e mai mare ca {x}')
    else:
        print("numerele sunt egale")

compare(5, 5)

'''10. Funcție care primește un număr și un set de numere.
Printează ‘am adaugat numărul nou în set’ + returnează True
Printează ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
'''

# def add_number(number, set_numere: set):
#     if number not in set_numere:
#         set(set_numere).add(number)
#         print('Am adaugat numarul in set')
#         print(set_numere)
#         return True
#     else:
#         print('Nu am agaugat. Exista deja')
#         return False
#
# set1 = {4, 5, 7}
# print(add_number(8, set1))

def add_number(number, set_numere):
    try:
        if number not in set_numere:
            set_numere.add(number)
            print('Am adaugat numarul in set')
            return True
        else:
            print('Nu am agaugat. Exista deja')
            return False
    except Exception:
        print(Exception("Error"))

try:
    print(add_number(8, 3, 8, 8))
except TypeError:
    print("Error")