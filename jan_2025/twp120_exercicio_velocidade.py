#https://www.youtube.com/watch?v=NvVVMPIJmdI&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc&index=13

#Pergunte a velocidade de um carro, supondo um valor inteiro.
#Caso ultrapasse 110km/h, exiba uma mensagem dizendo que o usuário foi multado.
#Nesse caso, exiba o valor da multa, cobrando R$ 5,00 por km acima de 110km/h.

velocidade = int(input("Digite a velocidade do carro: "))
if velocidade > 110:
    print("Você foi multado")
    multa = (velocidade - 110) * 5
    print(f"Valor da multa: R${multa:.2f}")
else:
    print("Siga em frente!") #o else significa "caso o contrário" ou "senão" ou "caso não", e é utilizado em condições complementares
