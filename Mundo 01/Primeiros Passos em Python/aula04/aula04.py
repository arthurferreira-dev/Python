Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print('Olá, Mundo!')
Olá, Mundo!
print(Olá, Mundo!)
SyntaxError: invalid syntax
print(7+4)
11
print('7' + '4')
74
7 + 4
11
'7' + '4'
'74'
print('Olá' + '5')
Olá5
print('Olá' + 5)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print('Olá' + 5)
TypeError: can only concatenate str (not "int") to str
print('Olá' , 5)
Olá 5
print('Variáveis')
Variáveis
nome = 'Guanabara'
nome
'Guanabara'
>>> idade = 25
>>> idade
25
>>> peso = 75.8
>>> peso
75.8
>>> print(nome , idade , peso)
Guanabara 25 75.8
>>> print(nome+idade+peso)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(nome+idade+peso)
TypeError: can only concatenate str (not "int") to str
>>> nome = input('Qual é seu nome?')
Qual é seu nome? Roberto
>>> idade = input('Quantos anos você tem?') 47
SyntaxError: invalid syntax
>>> idade = input('Quantos anos você tem?')
Quantos anos você tem? 22
>>> peso = input('Quanto você pesa?')
Quanto você pesa? 68.8
>>> print(nome, idade, peso)
 Roberto  22  68.8
