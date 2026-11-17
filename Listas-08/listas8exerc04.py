# Arquivo: 04_busca_mochila.py

# Use a lista ["corda", "água", "mapa", "água"]. Leia o nome de um item e informe se ele existe e quantas vezes aparece. Diferencie maiúsculas e minúsculas.

# Teste com água (duas ocorrências), mapa (uma) e lanterna (nenhuma).

recursos = ["corda","agua","mapa","agua"]
print(recursos[0]) # corda
print(recursos[1]) # agua
print(recursos[2]) # mapa
print(recursos[3]) # agua


item = input("digite um item:")
print(item in recursos)
print(recursos.count(item))










