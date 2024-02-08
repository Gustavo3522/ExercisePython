from math import sqrt
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = co * co + ca * ca
print('A hipotenusa vai medir {:.2f}'.format(sqrt(hi)))