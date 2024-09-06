
#Entrada de dados

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: ")) #int() ou float()

print("Olá, " + nome + "!")
print("Você tem ", idade, " anos.")

idade = int(input("Insira sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#---------------------------------------------------------

#Saída de dados

nome = "Juan"
idade = 25

print(f"Olá, meu nome é {nome} e tenho {idade} anos.")

#---------------------------------------------------------

#Leitura & Escrita de arquivos: leitura ("r"), escrita ("w") ou anexar ("a")

#Leitura
arquivo = open("dados.txt", "r") 
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

#Escrita
arquivo = open("dados2.txt", "w")
arquivo.write("Olá, mundo!")
arquivo.close()

#Método automatidado
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)