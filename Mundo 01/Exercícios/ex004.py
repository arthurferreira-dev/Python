# Resolução do Exercício 4 feito pelo Professor Guanabara, mas eu fiz e está na pasta de Desafios.
a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfábetico?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Está em minúsculas?', a.islower())
print('Está capitalizada?', a.istitle())