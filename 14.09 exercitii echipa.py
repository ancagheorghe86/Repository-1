# # Structuri de date
#
#
#
# # 12. Ne imaginăm o echipă de fotbal pt teren sintetic.
# # 3 Schimbări maxime admise:
# #
# # Declară o Listă cu 5 jucători
# # Schimbari_efectuate = te joci tu cu valori diferite
# # Schimbari_max = 3
# #
# # Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# # Efectuează schimbarea
# # Șterge jucătorul scos din listă
# # Adaugă jucătorul intrat
# # Afișază a intrat x, a ieșit y, mai ai z schimbări
# #
# # Dacă jucătorul nu e în teren:
# # Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
# # Afișază ‘mai ai z schimbări’
# #
# # Testează codul cu diferite valori
# #
# # Google search hint
# # “how to check if item is în list python”
#
# import random
# da_team = ['Vasile', 'Valentin_Mihai', 'Corneliu', 'Raul', 'Anca', 'Bianca', 'Valentin_Sorin', 'Razvan', 'Ioana', 'Marius', 'Bogdan', 'Dorian', 'Madalina', 'Alexandru']
# sesiune = 4 #deja au trecut 4 sesiuni
# print(da_team)
# while len(da_team) >= 1:
#     prezinta_azi = random.choice(da_team)
#     sesiune = sesiune + 1
#     print(f'Sesiunea a {sesiune}-a, prezinta: {prezinta_azi}.')
#     da_team.remove(prezinta_azi)

#2. Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:

# Declară o Listă cu 5 jucători
# Schimbari_efectuate = te joci tu cu valori diferite
# Schimbari_max = 3

echipa = ['Hagi', 'Mutu', 'Ronaldo', 'Banel', 'Mesi']
schimbari_efectuate = 0
schimbari_max = 3

jucator_schimbat = input('Jucatorul scos: ')
jucator_introdus = input('Jucator introdus: ')

if schimbari_efectuate <= schimbari_max and jucator_schimbat in echipa:
    schimbari_efectuate = schimbari_efectuate + 1
    print(f'Afiseaza a intrat {jucator_introdus}, a iesit {jucator_schimbat}, mai ai {schimbari_max-schimbari_efectuate}')
elif schimbari_efectuate == schimbari_max:
    print('Nu mai avem schimbari posibile')
else:
print(f'Jucatorul {jucator_schimbat} nu se afla in echipa'}