import math
def aria_patrat():
    a = int(input("Ce lungire are latura patratului tau?"))
    return (a**2)

def diagonala():
    a = int(input("Ce lungire are latura patratului tau?"))
    return a*(math.sqrt(2))

print(aria_patrat())
print(diagonala())

def triunghi_dreptunghic():
    a = int(input("cateta 1 ? "))
    b = int(input("cateta 2 ? "))
    ipotenuza = math.sqrt(a**2+b**2)
    return ipotenuza

print(triunghi_dreptunghic())

def triunghi():
    a = int(input("latura 1 ? "))
    b = int(input("latura 2 ? "))
    c = int(input("latura 3 ? "))
    if a < b + c and b < a + c and c < a + b:
        return (f'Laturile tale formeaza un triunghi')
    else:
        return (' Laturile tale nu formeaza un triunghi')

print(triunghi())

def prima_cifra():
    a = input("Scrie un numar format din 3 cifre  ")
    return a[0]
print(prima_cifra())
