from algebra import monomio

m1 = monomio([2, 'w', 3])
print(m1)

m1.grafica()
m2=monomio([-5, 'w',3])
m3=m1/m2
print(type(m3))