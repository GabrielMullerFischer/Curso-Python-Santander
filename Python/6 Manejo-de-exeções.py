
# try

try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
    
#--------------------------------------------------------------------

# Except
    
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Valor inválido")
    
#--------------------------------------------------------------------
    
# Finally
    
try:
    # Tentar abrir o arquivo
    arquivo = open("arquivo.txt", "r")
    # Realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    # Verificar se o arquivo foi realmente aberto antes de tentar fechá-lo
    try:
        arquivo.close()
    except NameError:
        pass  # Se o arquivo não foi aberto, não faz nada

# ou 

try:
    with open("arquivo.txt", "r") as arquivo:
        # Realizar operações com o arquivo
        pass
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
    
#--------------------------------------------------------------------

# Exeções personalizadas
condicao = 0

def funcao():
    # Código que pode gerar uma exceção personalizada
    if condicao != 0:
        raise Exception("Descrição do erro")

try:
    funcao()
except Exception as e:
    print(f"Erro: {str(e)}")
