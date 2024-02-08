real = float(input('Quanto dinheiro você tem na carteira ? R$'))
dolar = real / 4.98
euro = real / 5.33
print(' Com R${:.2f} Reais voce consegue comprar \n {:.2f} Dolares \n {:.2f} Euros '.format(real, dolar, euro))