#https://www.youtube.com/watch?v=pDi5VtF9TfA&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc&index=5

#fstrings

#fstrings são uma forma de formatar strings, que é mais fácil de ler e escrever

resposta = 42
print(f"tudo tem {resposta} como solução")

#fstring substitui o que está entre chaves pelo valor da variável. se não houver variável, ocorre um erro

#o fstring também funciona com valores decimais

#no Python pode se usar qualquer caracter unicode como variável
#Um caractere Unicode é um componente escrito, como uma letra, número, marca de pontuação ou marca de acento, que pode ser representado por um valor numérico.

preco = 9.6666
print(f"o preço é R${preco:.2f}")
#o :.2f diz que o número deve ser formatado com duas casas decimais

a = 42
b = 13
print(a > b)
type(True) #boolean é uma classe lógica, significa veradeiro ou falso
print(a > 100)
print(a == 42) #a = 42 é um post it que atribui 42 a a. a == 42 é uma comparação, uma pergunta pra entender se a é = a 42
print(b == 42)
print(b != 42) #!= é diferente
print(a == 42 or b ==42) #quero verificar se um dos dois sejam verdadeiro para voltar o boolean verdadeiro
#se eu atribuir a = 10, e tentar rodar de novo print(a == 42 or b ==42), o boolean será falso, pois nenhuma das duas variáveis são iguais a 42

nota = 7
faltas = 21
print(nota >= 6 and faltas <= 20) # and: quero que as duas condições sejam verdadeiras para que o boolean seja verdadeiro, se uma for falsa, o boolean será falso
#no caso acima, o retorno será falso pois as faltas são maiores que 20