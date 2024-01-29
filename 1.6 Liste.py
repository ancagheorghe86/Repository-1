# ARRAY
# listele in python pot sa cuprinda elemente de tipuri diferite
# au dimensiune dinamica; deci nu sunt imutabile

fructe = ['mar', 'banana', 'portocala', 3, True, 3]

# afisam o lista
print(fructe)

# accesam un element in functie de index
print(fructe[0]) # o sa primim rezultatul mar; marul reprezinta index 0 in lista noastra
print(fructe[1]) # o sa primim rezultatul banana; banana reprezinta index 1 in lista noastra
                 # numaratoarea incepe de la 0, nu de la 1
                 # pentru numaratoarea in sens invers se incepe de la -1

# adaugam un nou element
fructe.append('rosie')
print(fructe)

# suprascriem un element - ex: in loc de mar sa scriem para :
fructe[0] = 'para'
print(fructe)

# aflam dimensiunea listei
print(len(fructe))

# scoate si ne returneaza ultimul element:
# metoda pop
last = fructe.pop()
print(last)
print(fructe)

# de cate ori apare un element
print(fructe.count(3))

# functia EXTEND (extindere de lista cu o alta lista)
# mai facem o lista:

fructe_exotice = ['ananas', 'kiwi']
fructe.extend(fructe_exotice)  #adaugam "fructe_exotice" la lista noastra initiala "fructe"
print(fructe)

