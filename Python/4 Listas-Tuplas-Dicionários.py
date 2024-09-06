
#Listas

frutas = ["maçã", "banana", "laranja"]

print(frutas[0])  # Imprime "maçã"
print(frutas[1])  # Imprime "banana"
print(frutas[2])  # Imprime "laranja"
print(frutas[-1])  # Imprime "laranja"
print(frutas[-2])  # Imprime "banana"
print(frutas[-3])  # Imprime "maçã"

#append(elemento): adiciona um elemento ao final da lista.
#insert(indice, elemento): insere um elemento em uma posição específica da lista.
#remove(elemento): remove a primeira ocorrência de um elemento na lista.
#pop(indice): remove e retorna o elemento em uma posição específica da lista.
#sort(): ordena os elementos da lista em ordem ascendente.
#reverse(): inverte a ordem dos elementos na lista.

frutas.append("pera")
print(frutas)  # Imprime ["maçã", "banana", "laranja", "pera"]
frutas.insert(1, "uva")
print(frutas)  # Imprime ["maçã", "uva", "banana", "laranja", "pera"]
frutas.remove("banana")
print(frutas)  # Imprime ["maçã", "uva", "laranja", "pera"]
fruta_removida = frutas.pop(2)
print(frutas)  # Imprime ["maçã", "uva", "pera"]
print(fruta_removida)  # Imprime "laranja"
frutas.sort()
print(frutas)  # Imprime ["maçã", "pera", "uva"]
frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "maçã"]

números = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in números if x % 2 == 0]
print(quadrados)  # Imprime [4, 16]

#-----------------------------------------------------------------------------------------------------

#Tuplas

ponto = (3, 4)
print(ponto[0])  # Imprime 3
print(ponto[1])  # Imprime 4

#count(elemento): devolve o número de vezes que um elemento aparece na tupla. 
#index(elemento): devolve o índice da primeira aparição de um elemento na tupla. Opcionalmente, pode-se especificar o início e fim da busca. 
#len(tupla): embora não seja um método de tupla propriamente dito, esta função incorporada devolve o comprimento da tupla.

minha_tupla = (1, 2, 3, 2, 4, 2)
print (minha_tupla.index(2))   # Saída: 1
print (minha_tupla.index(2, 2))   #Saída: 3
print (minha_tupla.index(2, 2, 4))   #Saída: 3

#-------------------------------------------------------------------------------------------------

#Dicionários

pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}

print(pessoa["nome"])  # Imprime "João"
print(pessoa["idade"])    # Imprime 25
print(pessoa["cidade"])  # Imprime "Madri"

#keys(): retorna uma visualização de todas as chaves do dicionário.
#values(): retorna uma visualização de todos os valores do dicionário.
#items(): retorna uma visualização de todos os pares chave-valor do dicionário.
#update(outro_dicionario): atualiza o dicionário com os pares chave-valor de outro dicionário.

print(pessoa.keys())    # Imprime dict_keys(["nome", "idade", "cidade"])
print(pessoa.values())  # Imprime dict_values(["João", 25, "Madri"])
print(pessoa.items())   # Imprime dict_items([("nome", "João"), ("idade", 25), ("cidade", "Madri")])

pessoa.update({"profissao": "Engenheiro"})
print(pessoa)  # Imprime {"nome": "João", "idade": 25, "cidade": "Madri", "profissao": "Engenheiro"}

#--------------------------------------------------------------------------------------------------

#Conjuntos SET

numeros = set([1, 2, 3, 4, 5])

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

#união (|), a interseção (&), a diferença (-) e a diferença simétrica (^)

uniao = conjunto1 | conjunto2
print(uniao)  # Imprime {1, 2, 3, 4, 5}
intersecao = conjunto1 & conjunto2
print(intersecao)  # Imprime {3}
diferenca = conjunto1 - conjunto2
print(diferenca)  # Imprime {1, 2}
diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  # Imprime {1, 2, 4, 5}

frutas = {"maçã", "banana", "laranja"}

#add(elemento): adiciona um elemento ao conjunto.
#remove(elemento): remove um elemento do conjunto. Se o elemento não existir, gera um erro.
#discard(elemento): remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.
#clear(): remove todos os elementos do conjunto.

frutas.add("pera")
print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}
frutas.remove("banana")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}
frutas.discard("uva")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}
frutas.clear()
print(frutas)  # Imprime set()