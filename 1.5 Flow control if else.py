# flow control = controlam pana unde sa ruleze programul
# flow control = conditionarea codului in functie de o conditie

#if
piesa_faina = True

print('pornim radio')
if piesa_faina == True:
    print('dam mai tare')
    print('fredonam')
print('oprim radio')

# if else
# daca numarul este par printam acest lucru
# altfel printam impar

nr = 4
# ce insemana par? se imparte exact la 2
# ce insemana ca se imparte la 2? ne da restul 0
if nr % 2 == 0:  # daca restul impartirii numarului ( % = modulo) la 2 este egal cu zero, atunci nr este par si se va afisa mesajul:
    print('nr par')
else:           # daca restul impartirii numarului la 2 nu este egal cu zero, atunci nr este impar si se va afisa mesajul:
    print('nr impar')

# este un numar pozitiv?
if (nr > 0):
    print('nr pozitiv')
else:
    print('nr nu este pozitiv')

# daca utilizatorul are sub 18 ani, nu poate paria

# if, else if, else

# 1 - cum luam date de la tastatura? => cu input('mesajul/intrebarea')
# 2 - ne asiguram ca sunt transformate din string in int
    # ora = int(input('Introdu ora: ')

# cum ne saluta robotelul in functie de ora?

# ora = input('Introdu ora: ') #daca lasam asa si introduce 17, ne va da eroare
 # si corectam astfel:
ora = int(input('Introdu ora: '))  #tot ce punem in paranteze dupa int, va fi transformat in int (integer/ numar intreg)
#print(ora == 17)

if ora < 0:
    print('ora invalida')
elif ora <= 11:
    print('buna dimineata')
elif ora <= 18:
    print('buna ziua')
elif ora <= 21:
    print('buna seara')
elif ora <=24:
    print('noapte buna')
else:
    print('ora invalida mai mare decat 24')


# Exercitiu:

#<0 viteza invalida, 0 stationeaza, <= 50 in localitate, <= 90 drum judetean, >90 autostrada

viteza = int(input('Introdu viteza:'))
if viteza < 0:
    print('ora invalida')
elif viteza == 0:
    print('stationeaza')
elif viteza <= 50:
    print('in localitate')
elif viteza <= 90:
    print('drum judetean')
else:
    print('autostrada')

# CTRL + / = sa transformam in/din comentariu

# Exercitiu:
# robotel telefonie:
optiune = int(input('Alege o optiune: '))
if optiune == 0:
    print('meniu anterior')
elif optiune == 1:
    print('ati ales limba romana')
elif optiune == 2:
    print('Ati ales limba engleza')
else:
    print('nu am identificat optiunea, mai incearca')


# exercitiu Robotel telefonic:
# Pentru limba romana apasa tasta 1, pentru limba engleza tasteaza 2, pentru meniul anterior tasteaza 0

optiune = int(input('Alegeti o optiune: '))
if optiune == 1:
    print('Ati ales limba romana')
elif optiune == 2:
    print('Ati ales limba engleza')
elif optiune == 0:
    print('Ati ales sa va intoarceti la meniul anterior')
else:
    print('optiunea dumneavoastra nu corespunde nici unei optiuni')