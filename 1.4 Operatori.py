# if else
'''
Operatori:
aritmetici : +, -, *, /
de comparatie: < >, ==, !=, >=, <=
    > mai mare ca..
    < mai mic ca
    >= mai mare sau egal
    <= mai mic sau egal
    == daca este egal cu
    != nu este egal cu
logici: and, or
'''

a = 3
b = 5

print(a + b)  # asa se aduna cele doua numere a si b si se primeste rezultatul 8
print(a - b)  #asa se scad cele doua variabile a si b
print(a * b)  # asa se inmultesc

print(a<b)
print(a>b)
print(a == b)  #intrebam calculatorul daca a este egal cu b
print(a != b) # vrem o confirmare ca a nu este egal cu b

print(a < b and a < 4)  # True si True => True
print(a < b or a < 2)  # True sau False => True

# cu mama sau tata sau (cu bunicu si bunica)
mama = False
tata = False
bunicu = True
bunica = True
print(mama or tata or (bunicu and bunica))


