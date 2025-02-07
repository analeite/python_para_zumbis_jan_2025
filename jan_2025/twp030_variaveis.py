#https://www.youtube.com/watch?v=qHx8SRYqW2E&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc&index=4

#soma
3 + 4

#multiplicação
12 * 5

#expoenenciação
2 ** 10

#divisãoclear
10 / 3

#no python, a divisão sempre retorna um número de ponto flutuante. 
# em outras linguagens, a divisão de inteiros retorna um inteiro
1 / 2 # = 0.5

#type diz o tipo da variável
type(42) # = int

type(3.14) # = float
#float é um número de ponto flutuante, ou seja, que pode ter casas decimais

type("abacate") # = str

#dit vai me mostrar todos os métodos e atributos de uma string, que eu posso usar
dir("abacate") 

#em programação, 42, 3.14 e "abacate" são objetos, que podem ter métodos e atributos
#dir é um método reservado

help("abacate".upper)
#help me mostra a sintaxe de um método, ou seja, o que posso fazer com upper
#toda função precisa de parenteses, mesmo que não tenha argumentos

"abacate".upper()

#consultar a documentação do python quando for necessário

a = 42
b = "abacate"
#é como se o 42 existisse em um lugar na memória, e a variável a (post-it) aponta para esse lugar
print(a*3)
a = "banana"
#python não tem ponto e virgula
#não é necessário declarar o tipo da variável
#as variáveis são dinâmicas, ou seja, podem mudar de tipo