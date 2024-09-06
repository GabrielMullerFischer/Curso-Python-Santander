#Definição e chamada de funções

def saudacao():
    print("Olá, mundo!")
    
saudacao() #imprime "Olá, mundo!"

#---------------------------------------------------

#Parâmetros e argumentos

def saudacao(nome):
    print(f"Olá, {nome}!")
    
saudacao("João")  # Imprime "Olá, João!"
saudacao("Maria")  # Imprime "Olá, Maria!"

#--------------------------------------------------

#Valores de retorno

def soma(a, b):
    return a + b

resultado = soma(3, 4)
print(resultado)  # Imprime 7

#-------------------------------------------------

#Funções anônimas (lambda)

quadrado = lambda x: x ** 2
print(quadrado(5))  # Imprime 25

#-------------------------------------------------

#Escopo das variáveis (local vs. global)

def funcao():
    variavel_local = 10
    print(variavel_local)  # Acessível dentro da função

variavel_global = 20

def funcao2():
    print(variavel_global)  # Acessível de qualquer lugar

funcao()  # Imprime 10
funcao2()  # Imprime 20
print(variavel_global)  # Imprime 20
#print(variavel_local)  # Gera um erro, a variável não está definida neste escopo.


def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(soma_variavel(1, 2, 3))  # Imprime 6
print(soma_variavel(4, 5, 6, 7))  # Imprime 22