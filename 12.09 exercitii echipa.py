'''Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.'''
#
'''1. Declară o listă note_muzicale în care să pui do re mi etc până la do
Afișeaz-o.
Inversează ordinea folosind slicing și suprascrie această listă.
Printează varianta actuală (inversată).
Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.

Concluzii: slicing e temporar, dacă vrei să păstrezi nouă variantă va trebui să suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face suprascrierea automat și permanentizează aceste modificări. Ambele variante își găsesc utilitatea în funcție de ce ne dorim în acel moment.
'''
# 2. De câte ori apare ‘do’?
#
# 3. Transforma lista de mai sus intr-o tupla. Incearca sa adaugi o nota noua.
#
# 4. Declara un dictionar cu notele muzicale de mai sus. Cheia va fi nota, iar valoarea un numar care arata de cate ori apare nota in gama. Afiseaza-l.
#

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']  #aceasta este o lista
# note_muzicale = note_muzicale [::-1]
print(note_muzicale)
#
# note_muzicale.reverse() # lista in sens invers
# print(note_muzicale)

#.  2. De câte ori apare ‘do’?
# print(note_muzicale.count('do'))
#
# count = 0
# for nota in note_muzicale:
#     if nota == 'do':
#         count = count + 1
# print(f'Am gasit nota do de {count} ori')

# 3. Transforma lista de mai sus intr-o tupla. Incearca sa adaugi o nota noua.
# print(tuple(note_muzicale))
#
# note_muzicale.append('do')  # astfel am adaugat inca un do in  listaa de sus
# t = tuple(note_muzicale)
# print(t)

#4. Declara un dictionar cu notele muzicale de mai sus. Cheia va fi nota, iar valoarea un numar care arata de cate ori apare nota in gama. Afiseaza-l.
# dictionar = {
#     'do': note_muzicale.count('do'),
#     're': note_muzicale.count('re'),
#     'mi': note_muzicale.count('mi'),
#     'fa': note_muzicale.count('fa'),
#     'sol': note_muzicale.count('sol'),
#     'la': note_muzicale.count('la'),
#     'si': note_muzicale.count('si')
# }
# print(dictionar)