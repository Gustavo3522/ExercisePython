print('Pense em 3 valores diferentes')
a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = float(input('Terceiro valor: '))
#verificando quem é o menor
if a < b and a < c:
    menor = a 
if b < a and b < c:
    menor = b 
if c < a and c < b:
    menor = c 
print('O menor valor é {:.0f}'.format(menor))
#verificando quem é o maior 
if a > b and a > c:
    maior = a 
if b > a and b > c:
    maior = b 
if c > a and c > b:
    maior = c 
print('O maior valor é {:.0f}'.format(maior))
