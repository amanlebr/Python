def divi(x, y):
	try:
		result = x / y 
	except ZeroDivisionError: 
		print('Divisao por zero.')
	else: 
		print('Resultado e ', reruslt)
	finally:
		print('Executando a clausula finally')

mod_exec_div.py

from mod_div import divi
x = int(input('Digite o dividendo: '))
y = int(input('Digite o divisor: '))

divi(x, y)
