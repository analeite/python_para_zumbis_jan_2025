#https://www.youtube.com/watch?v=wLRPo8hydXc&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc&index=12

#if
#Verificar se um carro é novo ou velho
#Se o carro tiver pelo menos três anos é novo

idade = int(input("Digite quantos anos o seu carro tem: "))
if idade <= 3: #ou a idade é maior que 3 ou é menor ou igual a 3
    print("Seu carro é novo!")
#if idade > 3: #se eu tenho duas condições complementares (ou seja, duas possibilidades), eu posso usar o else ao invés de outro if
else:
    print("Seu carro é velho!") 