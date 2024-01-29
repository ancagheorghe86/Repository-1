def salut():
    nume_prenume = input('Cum te numesti? : ')
    print(f"Bine ai venit {nume_prenume}")

salut()

def media_numerelor(a, b, c):
    return (a + b + c) / 3
print(media_numerelor(3,4,5))

def verificare_majorat(varsta):
    if varsta >= 18:
        return True
    else:
        return False

varsta = int(input(f" Ce varsta ai?"))
if verificare_majorat(varsta):
    print("Felicitari! Cont Creat.")
else:
    print("Nu ai varsta necesara (18) pentru a crea cont")