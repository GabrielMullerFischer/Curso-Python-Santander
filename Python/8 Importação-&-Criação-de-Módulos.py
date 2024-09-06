
#Importar módulos

import math
#ou "from math import sqrt"


resultado = math.sqrt(25) #Raiz
print(resultado)  # Imprime 5.0

#----------------------------------------

# Funções e classes de módulos padrão

import random
import datetime

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime um número inteiro aleatório entre 1 e 10

data_atual = datetime.datetime.now()
print(data_atual)  # Imprime a data e hora atual

#-----------------------------------------

#Módulo personalizado

import meu_modulo

meu_modulo.saudar("João")  # Imprime "Olá, João!"
resultado = meu_modulo.calcular_soma(5, 3)
print(resultado)  # Imprime 8