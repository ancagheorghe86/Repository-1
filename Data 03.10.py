from datetime import date
from obiecte import Om

om1 = Om("Daniel", 0, 3.200, date.today())
om2 = Om("Rares", 0, 3.00, date.today())
om3 = Om("Gina", 0, 3.00, date.today())
om4 = Om("Giani", 0, 3.00, date.today())

maternitate = [om1, om2, om3, om4]

# print(om1)
# print(om2)
# print(om3)
# print(om4)

for element in maternitate:
    print(element)