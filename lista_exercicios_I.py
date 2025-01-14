import sys
sys.set_int_max_str_digits(0)

#https://www.youtube.com/watch?v=IZwUmam6K5c&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc&index=9

#1) Faça um programa que peça dois números inteiros e imprima a soma desses dois números
print("Questão 1") #CORRETO
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print(str(n1 + n2) + "\n")

#2) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
print("Questão 2") #CORRETO
metros = int(input("Digite o valor em metros: "))
milimetros = int((metros* 1000))
print(f"O valor em milimetros é {milimetros}\n")

#3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
print("Questão 3") #CORRETO
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))
total_segundos = (dias * 86.400 + horas * 3600 + minutos * 60 + segundos)
print(f"O total em segundos é {total_segundos}\n")

#4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e aporcentagem do aumento. Exiba o valor do aumento e do novo salário.
print("Questão 4") #CORRETO
salario_inicial = float(input("Digite o valor do salário: "))
porcentagem = float(input("Digite a porcentagem do aumento: "))
aumento = (salario_inicial * porcentagem) / 100
salario_final = salario_inicial + aumento
print(f"Aumento: R${aumento:.2f}, Salário Final: R${salario_final:.2f}\n")

#5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
print("Questão 5") #CORRETO
preco_mercadoria = float(input("Digite o valor da mercadoria: "))
percentual = float(input("Digite o percentual de desconto: "))
desconto = (preco_mercadoria * percentual) / 100
preco_desconto = preco_mercadoria - desconto
print(f"Valor do desconto: R${desconto:.2f}, Preço a pagar: R${preco_desconto:.2f}\n")

#6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
print("Questão 6") #CORRETO
distancia = int(input("Digite a distância a ser percorrida: "))
velocidade_media = int(input("Digite a velocidade média: "))
tempo_de_viagem = distancia // velocidade_media
print(f"Tempo de viagem: {tempo_de_viagem} horas\n")

#7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
print("Questão 7") #CORRETO
celsius = int(input("Digite a temperatura em Celsius: "))
fahrenheit = 9 * celsius // 5 + 32
print(f"Celsius: {celsius} C°, Fahrenheit: {fahrenheit} F°\n")

#8) Faça agora o contrário, de Fahrenheit para Celsius.
print("Questão 8") #CORRETO
fahrenheit = int(input("Digite a temperatura em Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"Celsius: {celsius} C°, Fahrenheit: {fahrenheit} F°\n")

#9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
#usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
print("Questão 9") #CORRETO
km = int(input("Digite a quantidade de km rodado: "))
qtd_dias = int(input("Digite a quantidade de dias em que o carro foi alugado: "))
preco = qtd_dias * 60 + km * 0.15
print(f"Valor a pagar: R${preco:.2f}\n")

#10) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
#quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
#perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
#total de dias.
print("Questão 10") #ESSA QUESTÃO ESTÁ CERTA AGORA
#Regra de três: 1 dia = 1440 minutos - 144 cigarros/poredia
cigarros = int(input("Digite quantos cigarros você fuma por dia: "))
anos = int(input("Digite há quantos anos você fuma: "))
total_cigarros = anos * 365 * cigarros
dias = total_cigarros / 144
print(f"Você perdeu {dias:.1f} dias de vida\n")

#11) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.
print("Questão 11")
print(len(str(2 ** 1000000000)))