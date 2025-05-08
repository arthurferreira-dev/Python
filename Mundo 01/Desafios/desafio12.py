print('Coloque um . ao inves da , POR FAVOR! (você pode colocar um número inteiro)')
prc = float(input('Digite um preço: R$'))
des = prc - (prc * 5 / 100)
print('O preço do produto foi de R${} para R${} com os 5% de Desconto.'.format(prc, des))
