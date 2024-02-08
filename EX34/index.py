salario = float(input('Qual o salario do funcionario ? '))
if salario >= 1250:
   aumento = salario + (salario * 10 / 100)
else:
    aumento = salario + (salario * 15 / 100)
print('O funcionario que ganhava {:.2f}, passa a ganhar {:.2f}'.format(salario, aumento))