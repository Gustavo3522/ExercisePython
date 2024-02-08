km = float(input('Qual a velocidade do veiculo ? '))
if km > 80:
    print('MULTADO! Você exedeu o limite permitido que é de 80km/h')
    multa = (km - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança')
