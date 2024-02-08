distancia = float(input('Qual a distância da sua viagem ? '))
print('Você está preste a começãr uma viagem de {:.2f}Km'.format(distancia))
if distancia <= 200:        
   valor = distancia * 0.50
else:
   valor = distancia * 0.45
print('A viagem vai custar {:.2f}R$'.format(valor))