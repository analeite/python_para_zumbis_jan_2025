#https://www.youtube.com/watch?v=edeDmCN9_oA&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc&index=11

#Eu amo dois pontos e identação!
#Não preciso colocar as chaves, pois o bloco de comandos associados a condição é definido pelo espaço esquerdo (identação = boas práticas)

#if
#Verificar se um carro é novo ou velho
#Se o carro tiver pelo menos três anos é novo

idade = int(input("Digite quantos anos o seu carro tem: "))
if idade <= 3:
    print("Seu carro é novo!")
if idade > 3:
    print("Seu carro é velho!")