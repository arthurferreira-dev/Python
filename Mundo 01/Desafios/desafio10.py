print('ISSO É FICCIONAL NÃO É PARA COLOCAR REALMENTE O VALOR DO DINHEIRO QUE VOCÊ TEM!')
print('CONSIDERE: US$1.00 = R$5.67 | €1.00 = R$6.36 | ¥1.00 = R$0.039')
real = float(input('Quantos Reais você tem? R$'))
dol = real / 5.67
euro = real / 6.36
iene = real / 0.039
print('Você consegue comprar US${:.2f} Dólar(es)'.format(dol))
print('Você consegue comprar €{:.2f}'.format(euro))
print('Você consegue comprar ¥{:.2f}'.format(iene))