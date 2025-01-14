#teste de mesa
divida = 0
commpra = 10.59
divida = divida + commpra
compra = 50.34
divida = divida + compra
compra = 4.50
divida = divida + compra
print(divida)

#pythontutor.com para realizar testes de mesa
#o teste de mesa é uma técnica de programação que consiste em simular a execução de um algoritmo de forma manual, a fim de verificar se o mesmo está funcionando corretamente.

nome = "Ana Beatriz"
print(nome)

#eu posso sobrescrever a variavel acima com outro nome, mas o correto é na verdade receber uma entrada do usuário usando o input

nome = input("Digite seu nome: ")
print(nome)

#o input sempre retorna uma string, mesmo que o usuário digite um número
n1 = input("n1: ")
n2 = input("n2: ")
print(n1 + n2) #uma string é concatenada com outra string

#para somar os números, é necessário converter a string para int
n1 = int(input("n1: ")) #não posso esquecer de colocar dois parenteses no final, pois dára erro. se eu esqueço de fechar o parenteses, ele tenta procurar o parenteses depois
n2 = int(input("n2: "))
print(n1 + n2)

#posso fazer a mesma coisa com float
n1 = float(input("n1: "))
n2 = float(input("n2: "))
print(n1 + n2)

#sempre que eu tiver problemas em uma linha e não encontrar o problema, devo verificar a linha anterior