# Cum citim o listă de la tastatură?
#solicităm numărul de elemente
n = int(input("n = "))
#creăm o listă ce nu conține nimic
lista = [] #sau lista = list()
#pentru fiecare element citit
for x in range(n):
    lista.append(input())
#la final, o afișăm
print(lista)