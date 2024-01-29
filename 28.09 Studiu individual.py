#                     # EXERCITII OPERATORI SI TIPURI DE DAT
#
# '''1. Afișați în consolă rezultatul expresiei: 9 * (12-5) - 2**3'''
# print(9*(12-5)-2**3)
#
# '''2. Realizați un nou program care calculează și afișează șapte la puterea a treia.'''
# print(7**3)
#
# '''3. Se știe că Andrei are 7 mere. Ana are de 3 ori mai multe mere decât Andrei,
# iar Ștefan are de 49 de ori mai multe mere decât Andrei. Să se afle câte mere au
# cei trei copii în total folosindu-se o expresie care conține adunarea,
# înmulțirea și ridicarea la putere (+,*,**).'''
# andrei = 7
# ana = andrei*3
# stefan = andrei*7**2
# impreuna = andrei + ana + stefan
# print(impreuna)
#
#
# '''4. O mașină folosește o cantitate de x litri pentru a parcurge distanța Constanța-București.
# O altă mașină folosește y litri pentru aceeași distanță, știind că y=2*x.
# Să se scrie un program în care să se citească variabila x și să se determine suma necesarului de combustibil.
# Obs. Atenție la tipul datelor...'''
#
#
# x = int(input('cati litri vrei? : '))
# y = 2*x
# suma_litri = x+y
# print(suma_litri)
#
#
# '''5. Creați un convertor de timp, transformând astfel orele și minutele introduse de la tastatură în secunde.
# Exemplu: Pentru ore=5, minute=54, se va tipări 21240 de secunde.'''
# ora = int(input(f'Scrie o ora: '))
# minute = int(input(f'Scrie si minutele: '))
# ora1 = ora*60**2
# minute1 = minute*60
# total_secunde = ora1 + minute1
# print(total_secunde)
#
#
# '''6. Să se scrie un program în care să se convertească șirul "110" într-un
# număr întreg și afisați tipul de dată astfel obținut.'''
# sir = "110"
# numar_intreg = int(sir)
# print(numar_intreg)
# print(type(numar_intreg))
#
#
# '''7. Într-un stup sunt 5 albine și de 2 ori mai mulți bondari. Fiecare albină produce 200ml de miere zilnic.
# Câți bondari sunt în stup? Dar câtă miere este produsă zilnic de cele 5 albine?'''
# albine = 5
# bondari = albine*2
# miere = albine*200
# print(bondari)
# print(miere)
#
# '''8. La gradina zoologică sunt 5 urși panda, 2 hipopotami, 4 iepuri și 6 vulpi.
# Câte picioare au în total animalele de la gradina zoologică?'''
# ursi = 5*4
# hipopotami = 2*4
# iepuri = 4*4
# vulpi = 6*4
# gradina_zoologica = ursi + hipopotami + iepuri + vulpi
# print(gradina_zoologica)


'''9. La întâlnirea de 10 ani a veteranilor de război, Andy Anderson își revede cu drag colegii, 
alături de care a luptat pe front pentru libertatea țării. Andy își dă seama că cifrele 
numerelor de identificare, însumate, reprezintă vârsta camarazilor săi. 
Ajută-l pe Andy să afle dacă ceilalți veterani sunt mai bătrâni decât el.
xemplu: Dacă se citește următorul cod pentru un veteran: 9987998, se va afișa 59.'''

#
# def getSum(cod_camarad):
#     sum = 0
#     for digit in str(cod_camarad):
#         sum += int(digit)
#     return sum
#
# cod_camarad = int(input(f'Scrie numarul de identificare al camaradului: '))
# varsta_camarad = print(getSum(cod_camarad))


'''10. O populație de bacterii se dublează la fiecare oră a zilei și se înjumătățește 
la fiecare oră din noapte. Se consideră ziua de h1 ore și noaptea de h2 ore. 
De cate ori va crește populația de bacterii după z zile? (h1,h2,z - variabile introduse de la tastatură)'''

# populatie_bacterii = int(input(f'Cate bacterii ai: '))
# ore_zi = int(input(f'Cate ore pe zi: '))
# ore_noapte = int(input(f'Cate ore pe noapte: '))
# zile = int(input(f'Cate zile tii bacteriile: '))
# bacteri_ziua = ((populatie_bacterii*2)*ore_zi)*zile
# bacterii_noaptea = ((populatie_bacterii/2)*ore_noapte)*zile
# nr_bacterii = bacteri_ziua+bacterii_noaptea
# de_cate_ori = (bacteri_ziua+bacterii_noaptea)//populatie_bacterii
# print(nr_bacterii)
# print(de_cate_ori)

list1 = [1, 2, 3, 'male', 1]
list1.append('lolo')
print(list1)