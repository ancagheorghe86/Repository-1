# variabila = o zona din memoria unui calculator care tine date
# variabila = o cutiuta in care punem valori

# am declarat si initializat variabila marca
#  = nu inseamna egal, el este un operator de atribuire

marca_masina = 'Volvo'
model_masina = 'XC 60'

# nu putem sa punem spatiu in numele variabilei
# ( este gresit sa scriem marca masina. Corect este marca_masina.
# o variabila incepe cu o litera mica

# marca_masina = este un string
# un string este un sir de date de la tastatura delimitate de '' sau " "

# loosely typed = nu trebuie sa specificam tipurile variabilelor

# print(f'exemplu') = f vine de la format string

print(f'Am cumparat o masina marca : {marca_masina}')
print(f'Este modelul {model_masina}')

# suprascrierea
model_masina = 'XC 60 facelift'

print(f'Am cumparat o masina marca : {marca_masina}')
print(f'Este modelul {model_masina}')

nume = 'Gheorghe'
prenume = 'Anca'
varsta = 34
#print(prenume + ' ' + nume + varsta) #asa primim eroare, trebuie sa le formatam cu f (format string)
print(f'{prenume} {nume} si am varsta de {varsta}')    # esta este o concatenare (adunare) de stringuri



