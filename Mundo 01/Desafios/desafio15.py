dia = int(input('Por quantos dias foi alugado? '))
km = float(input('Quantos KM rodados? '))
precd = 60 * dia
preckm = 0.15 * km
junto = precd + preckm
print('Você deve pagar R${:.2f}'.format(junto))