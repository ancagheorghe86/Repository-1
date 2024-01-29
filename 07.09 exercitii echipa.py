# # 8.
# # X, y, z - laturile unui triunghi.
# # Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
#
x = float(input('x =  '))
y = float(input('y = '))
z = float(input('z = '))
#
# if x == y == z:
#     print('triunghiul este echilateral')
# elif x != y != z and x != z:
#     print('triunghiul este oarecare ')
# else:
#     print('triunghiul este isoscel')


# 15.
#  X, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.


if x + y + z == 180 and x > 0 and y > 0 and z> 0:
    print('triunghiu este valid')
else:
    print('nu este valid')
