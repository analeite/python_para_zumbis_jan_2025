#https://www.youtube.com/watch?v=Vz6XNxReuNo&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc&index=20

#Antes do while eu começo com algumas variáveis

#Altere o código abaixo para imprimir de 1 até um número lido

x = 0
fim = int(input("Fim: "))
while x <= fim:
    print(x)
    x = x + 1
    
# Contadores: incremento constante
# Acumuladores: soma variável

# Soma dez inteiros lidos

n = 1 # Contador
soma = 0 # Variável acumuladora
while n <= 10:
    x = int(input(f"{n} número: "))
    soma = soma + x
    n = n + 1
print(f"Soma: {soma}")

# Calcular a média dos dez números

n = 1 # Contador
media = 0 # Variável acumuladora
soma = 0 
while n <= 10:
    x = int(input(f"{n} número: "))
    soma = soma + x
    n = n + 1
media = soma / x
print(f"Média: {media:.2f}")
