salario = float(input('Qual o salario do funcionario ? R$'))
novo = salario + (salario * 15 / 100)
print('Um funcionario que ganhava R${}, com 15% de aumento, passa a ganhar R${:.2f}'.format(salario, novo))   