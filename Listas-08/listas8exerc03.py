# Arquivo: 03_relatorio_numeros.py

# Leia seis números inteiros e guarde todos em uma lista. Mostre a lista, a soma, a média, o maior e o menor valor.

# Teste com 3, -2, 0, 7, 7, -3: soma 12, média 2.0, maior 7 e menor -3.

numeros = []


for numero in range(1,7):
    
    numero = int(input("digite um numero:"))
    numeros.append(numero)

print("Quantidade:",len(numeros)) 
print("soma:", sum(numeros))
print("maior", max(numeros))
print("menor", min(numeros))
print("media", sum(numeros)/len(numeros)) 




















