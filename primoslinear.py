#Bibliotecas
import os

#Entrada de dados
while True:
    try:
        n=int(input("Insira o valor de N para receber os numeros primos até N: "))
    except ValueError:
        print("Erro: O valor de N deve ser inteiro, maior que 1.")
        continue
    if n > 1:
        break
    else:
        os.system("cls")
        print("O valor esta fora do intervalo definido.")

#Validação de condição
primos=[]

for numeros in range (2,n+1):
    for primo in primos:
        if (numeros % primo) == 0:
            break
    else:
        primos.append(numeros)

#Imprime 
print(f"p({n})={primos}")