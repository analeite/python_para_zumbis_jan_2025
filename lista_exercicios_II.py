#https://www.youtube.com/watch?v=jVlwYb8AiCs&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc&index=16 - dicas de como resolver a lista de exercícios
#https://www.youtube.com/watch?v=P7NzRyfc51M&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc&index=17 - resolução da lista de exercícios

import calendar
#1. Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser 
#um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
print("Questão 1") #CORRETO
lado1, lado2, lado3 = input("Digite os três lados do triângulo utilizando espaços: ").split()
if lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado1 + lado2:
    print("Não é um triângulo")
elif lado1 == lado2 == lado3:
	print("Triangulo equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
	print("Triangulo isosceles")
else:
	print("Triangulo escaleno")
	
#2. Determine se um ano é bissexto. Verifique no Google como fazer isso...
#help(calendar.isleap) #-> verifica como o método funciona. Posso utilizar o dir para fazer isso também
print("\nQuestão 2") #CORRETO
ano = int(input("Digite o ano: "))
if calendar.isleap(ano) == True:
	print(f"O ano {ano} é bissexto")
else:
	print(f"O ano {ano} não é bissexto")

'''
3. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de
seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do
estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você
faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na
variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais
variáveis com o conteúdo ZERO.
'''
print("\nQuestão 3") #CORRETO
peso = int(input("Digite o valor do peso: "))
if peso > 50:
	excesso = peso - 50
	multa = excesso * 4
	print(f"Excesso: {excesso}, Multa: R${multa:.2f}")
else:
	excesso = 0
	multa = 0
	print(f"Excesso: {excesso}, Multa: R${multa:.2f}")
	
#4. Faça um Programa que leia três números e mostre o maior deles.
print("\nQuestão 4") #CORRETO
n1, n2, n3 = int(input("Digite os três números utilizando espaços entre eles: ")).split()
if n1 >= n2 and n1 >= n3:
	print(f"{n1} é o maior número")
elif n2 >= n3:
	print(f"{n2} é o maior número")
else:
	print(f"{n3} é o maior número")
	
#5. Faça um Programa que leia três números e mostre o maior e o menor deles.
print("\nQuestão 5") #CORRETO
n1, n2, n3 = int(input("Digite os três números utilizando espaços entre eles: ")).split()
if n1 > n2 and n1 > n3:
	if n2 > n3:
		print(f"{n1} é o maior número e {n3} é o menor número")
	else:
		print(f"{n1} é o maior número e {n2} é o menor número")
elif n2 > n1 and n2 > n3:
	if n1 > n3:
		print(f"{n2} é o maior número e {n3} é o menor número")
	else:
		print(f"{n2} é o maior número e {n1} é o menor número")
elif n3 > n1 and n3 > n2:
	if int(n1) > int(n2):
		print(f"{n3} é o maior número e {n2} é o menor número")
	else:
		print(f"{n3} é o maior número e {n1} é o menor número")
		
#Solução do professor
n1, n2, n3 = int(input("Digite os três números utilizando espaços entre eles: ")).split()
if n1 <= n2 and n1 <= n3:
	print(f"{n1} é o menor número e {n3} é o maior número")
elif n2 <= n1 and n2 <= n3:
    print(f"{n2} é o menor número e {n3} é o maior número")
else:
    print(f"{n3} é o menor número e {n2} é o maior número")
		
'''
6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
descontos e o salário líquido, conforme a tabela abaixo:
a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$
'''
print("\nQuestão 6") #CORRETO
salario_hora = float(input("Digite quanto você ganha por hora: "))
hora_trabalhadas = int(input("Digite o número de horas trabalhadas no mês: "))
salario_bruto = salario_hora * hora_trabalhadas
ir = 11 / 100 * salario_bruto
inss = 8 / 100 * salario_bruto
sindicato = 5 / 100 * salario_bruto
salario_liquido = salario_bruto - ir - inss - sindicato
print(f"Salário Bruto: R${salario_bruto:.2f}\n Imposto de Renda: R${ir:.2f}\n INSS: R${inss:.2f}\n Sindicato: R${sindicato:.2f}\n Salário Líquido: R${salario_liquido:.2f}")

'''
7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas
'''
print("\nQuestão 7") #CORRETO
area = int(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
metros_latas = 18 * 3
if area % metros_latas == 0:
	latas = area / metros_latas
	preco = latas * 80
	print(f"Quantidade de latas a serem compradas: {latas:.0f}\nPreço a ser pago: R${preco:.2f}")
else:
	latas = area / metros_latas + 1
	preco = int(latas) * 80
	print(f"Quantidade de latas a serem compradas: {latas:.0f}\nPreço a ser pago: R${preco:.2f}")