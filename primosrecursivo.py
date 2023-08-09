#Bibliotecas
import os

#Entrada de dados
while True:
    try:
        n=int(input("Insira o valor de N para receber os numeros primos até N: "))
    except ValueError:
        print("Erro: O valor de N deve ser inteiro e maior que 1.")
        continue
    if n > 1:
        break
    else:
        os.system("cls")
        print("O valor esta fora do intervalo definido.")

tabprimos = []

def primos(n):
    if n == 2:
        tabprimos.append(n)
    else:
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            tabprimos.append(n)
    if n > 2:
        primos(n - 1)
primos(n)

#Imprime
print(f"p({n})={tabprimos}")
