
#If-Else-Elif

nota = 85

if nota >= 90:
   print ("Excelente")

elif nota >= 80:
   print ("Muito bom")

elif nota >= 70:
   print ("Bom")

else:
   print ("Precisa melhorar")
   
#---------------------------------------------------
#For-While

frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)
    
contador = 0

while contador < 5:

    print(contador)
    contador += 1
    
contador = 0


while True:

    print(contador)
    contador += 1

    if contador == 5:
        break #Encerra todos os Loops
     
     
for i in range(10):

    if i % 2 == 0:
        continue #encerra o loop atual e começa o próximo
    print(i)
    
