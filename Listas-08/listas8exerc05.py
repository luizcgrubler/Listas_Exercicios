# Arquivo: 05_separando_pares.py

# Leia oito inteiros e armazene-os em uma lista. Percorra essa lista para criar outra contendo apenas os números pares. Mostre as duas listas. Preserve a ordem e os repetidos.

# Lembre-se: numero % 2 == 0 identifica um par, incluindo zero e pares negativos. Teste também uma execução sem nenhum par.





original = [1,7,2,12,15,6,9,4,20,17,13,18,-7, -11,-8]

pares = []
impares = []
negativos = []
for numero in original:
    if numero % 2 ==0:
        pares.append(numero)
    else:
        impares.append(numero)
    if numero <0:
        negativos.append(numero)

print(original)
print()
print(pares)
print()
print(impares)








