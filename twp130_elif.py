#https://www.youtube.com/watch?v=NYD16LUbVKg&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc&index=15

#Modifique o programa da empresa Tchau para uma promoção onde a tarifa é de R$0,08 
#quando você utiliza mais de 800 minutos

#flat é melhor que escadinha

minutos = int(input("Digite a quantidade de minutos: "))
if minutos < 200:
	preco = 0.20
elif minutos >= 200 and minutos < 400:
	preco = 0.18
elif minutos >= 400 and minutos < 800:
	preco = 0.15
else:
	preco = 0.08
total = minutos * preco
print(f"Total a pagar: R$ {total:.2f}")

#O elif é uma abreviação de else if, ou seja, é uma condição complementar
#a condição do elif só é verificada se a condição do if for falsa

#solução do professor

minutos = int(input("Minutos: "))
if minutos < 200:
	preco = 0.20
elif minutos <= 400:
    preco = 0.18
elif minutos <= 800:
	preco = 0.15
else:
	preco = 0.08
print(f"R${minutos * preco:.2f}")

#a solução do professor é melhor porque é mais simples e mais fácil de entender