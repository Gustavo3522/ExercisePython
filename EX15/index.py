dia = int(input('Por quantos dias o carro foi alugado ? '))
km = float(input('Quantos km o carro rodou ? '))
pago = (dia *60) + (km * 0.15)
print('O total a pagar é de R${}'.format(pago))