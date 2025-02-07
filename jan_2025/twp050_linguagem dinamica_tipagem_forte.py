#https://www.youtube.com/watch?v=Az0ri1W2Ygc&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc&index=7

#python é uma linguagem dinamicamente tipada, fortemente tipada e orientada a objetos

#linguagem dinamica: as mudanças que eu posso realizar na variável são feitas em tempo de execução
a = 42
print(a) #a variável a foi criada e recebeu o valor 42
a = 'abacate'
print('abacate') #a variável a mudou de tipo, de int para str. isso é uma característica de linguagem dinâmica
a = 3.14
print(a) #a variável a mudou de tipo, de int para float. isso é uma característica de linguagem dinâmica

#tipagem forte: o python não faz conversões automaticas de tipos
#print(42 + 'abacate') #vai dar erro, pois não é possível somar um número com uma string, o python não faz conversões automaticas de tipos
print(str(42) + 'abacate') #para somar um número com uma string, é necessário converter de forma explicita o número para string
#explicito é melhor que implicito

#orientada a objetos: tudo em python é um objeto
#poo é um paradigma de programação, que diz que tudo é um objeto
#A POO é um modelo que aproxima o mundo real do virtual, através da interação entre objetos, atributos, códigos e métodos.
#Ou seja, a POO é um paradigma de programação que utiliza objetos para representar elementos do mundo real.
#por exemplo, se eu digitar 'abacate'. eu vou ver todos os métodos e atributos que eu posso usar com a string

print('abacate'.upper()) #upper é um método que deixa a string em maiusculo
#os dados tem métodos, ou seja, não são apenas informações, mas possuem super poderes

a = 3
b = 'abacate'
a, b = b, a  #a variável a foi trocada pela variável b e vice versa. isso se chama atribuição multipla
print(a, b) #a variável a agora é 'abacate' e a variável b agora é 3
a, b , c = 1, 2, 3 #a variável a recebe 1, a variável b recebe 2 e a variável c recebe 3
d, m, e = "13/01/2025".split('/') #a variável d recebe 13, a variável m recebe 01 e a variável e recebe 2025, separado pela barra '/'

print(d, m, e) #13 01 2025

