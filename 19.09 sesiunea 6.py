# CICLURI REPETITIVE
# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ‘Mașina mea preferată este x’.
# Fă același lucru cu un for each.
# Fă același lucru cu un while.

# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# prefered_car = "Mercedes"

# for car in cars:
#     if car == prefered_car:
#         print(f'masina preferata este {car}')
#     print(car)

# i = 0 # indexul fiecareui element din lista cars
# while i <= len(cars):
#     print(i, cars[i])
#     i += 1  # sau i + 1

# i = 0
# while i < len(cars):
#     if cars[i] == prefered_car:
#         print(f'masina preferata este {cars[i]}')
#         # break
#         i += 1
#         continue
#     print(i, cars[i])
#     i += 1
#

# 2. Aceeași listă:
# Folosește un for else
# În for
# Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
# În else:
#   Printează lista.

# for car in cars:
#     if car == cars[0] or car == cars[-1]:  # daca masina noastra este prima[0] sau ultima [-1], atunci....
#         print(car)
#         continue
#     car = car.upper()
#     print(car)

# for car in cars:
#     if car == cars[0] or car == cars [-1]:
#         continue
#         car = car.upper
#         print(car)
# print(cars)

# i = 0
# print(list(enumerate(cars)))
# for i, car in enumerate(cars):\
#     #car = car.upper()
#     # cars [i] = car.upper()
#     if cars[0] == car or cars[-1] == car:
#         continue
#     cars[i] = car.upper()
#     print(i, car)
# else:
#
#     print(cars

'''3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Iterează prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
   Printează ‘am găsit mașina dorită de dvs’
   Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
   Printează ‘Am găsit mașina X. Mai căutam‘
'''

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# masina_de_vanzare = "Mercedes"
# for masina in masini:
#     if masina_de_vanzare == masina:
#         print(f'Am gasit masina dorita de dvs : {masina_de_vanzare}')
#         break
#     else:
#         print(f'Am gasit masina {masina}. Mai cautam')

'''4. Aceeași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun. 

Dacă mașina e Trabant sau Lăstun:
   Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
Printează S-ar putea să vă placă mașina x.

'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masina_de_vanzare = "Mercedes"

for masina in masini:
    if masina in ('Lastun', 'Trabant'):
    #     continue # atunci cand se gasesc elementele 'Lastun si Trabant, se trece la urmatoarele elemente din lista
    # print(f' S-ar putea sa va placa masina {masina}')
        masini.remove(masina)
print(masini)

