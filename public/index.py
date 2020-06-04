
"""
Autor: Leonardo Amancio
Data: 
versão: 03 (Utilizdo a condição elif)
Descrição: Faça um programa que leia um numero e exiba o dia correspindente da semana. 
(1 - Domingo, 2 - segunda,  3 - Terça ...), se digitrar outro valor, deve aparecer valor inválido.
"""

dia = int(input('Digite o dia da semana: ')) 
if dia == 1:
	print("Domingo")
elif dia == 2:
	print("Segunda")
elif dia == 3:
	print("Terça")
elif dia == 4:
	print("Quarta")
elif dia == 5:
	print("Quinta")
elif dia == 6:
	print("Sexta")
elif dia == 7:
	print("Sábado")
else: 
	print("Dia invalido") 
#teste de edição 



telefones = {"nomes1" : "+ 55 21 97993-9083"}
telefones["Fulano"]

telefones["nomes1"]



try: 
	print('O telefone e: ')
	print(telefones['Fulano'])
except KeyError:
	print('Não encontrado')




try: 
	print('O telefone e: ')
	print(telefones['nomes1'])
except KeyError:
	print('Não encontrado')


while True:
	try:
		x = int(input('Por favor, informe um numero: '))
		break
	except ValueError:
		print('Oops! Nao foi um número valido. Tente Novamente ...')