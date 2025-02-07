#https://www.youtube.com/watch?v=qHGki5ZSfi0&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc&index=14

#Estruturas aninhadas
#Considere a empresa de telefonia Tchau
#Abaixo de 200 minutos, a empresa cobra R$ 0,20 por min
#Entre 200 e 400 minutos, a empresa cobra R$ 0,18 por min
#Acima de 400 minutos, a empresa cobra R$ 0,15 por min
#Calcule a conta de telefone

minutos = int(input("Digite a quantidade de minutos utilizados: "))
if minutos <= 200:
	conta = minutos * 0.20
	print(f"Valor a pagar: R${conta:.2f}")
if minutos > 200 and minutos < 400:
	conta = minutos * 0.18
	print(f"Valor a pagar: R${conta:.2f}")
if minutos >= 400:
	conta = minutos * 0.15
	print(f"Valor a pagar: R${conta:.2f}")
	
#Resposta do professor e melhor solução
minutos = int(input("Digite a quantidade de minutos utilizados: "))
if minutos < 200:
	preco = 0.20
else:
	if minutos <= 400:
		preco = 0.18
	else:
		preco = 0.15
print(f"R${minutos * preco:.2f}")