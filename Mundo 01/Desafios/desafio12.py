print('Coloque um . ao inves da , POR FAVOR! (você pode colocar um número inteiro)')
prc = float(input('Digite um preço: '))
des = prc * 0.05
fim = prc - 1.25
print('O preço do produto foi de {}R$ para {}R$ com os 5% de Desconto.'.format(prc, fim))
