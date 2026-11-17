# Arquivo: 08_fila_atendimento.py

# Crie uma lista vazia e um menu com as opções:

# 1 - Adicionar pessoa ao final da fila
# 2 - Atender a primeira pessoa
# 3 - Mostrar a fila e sua quantidade de pessoas
# 0 - Sair
# Utilize append() para adicionar e pop(0) para atender. Antes de atender, verifique se há alguém na fila. Opções desconhecidas devem apresentar uma mensagem de erro.

# Teste atender com a fila vazia e adicionar Ana e Bruno para conferir a ordem dos atendimentos.



pessoas = []

while True:

    print("1 - adicionar pessoa ao final da fila")
    print("2 - atender a primeira pessoa")
    print("3 - mostrar a fila e sua quantidade de pessoas")
    print("sair")



    opcao = int(input("escolha uma opcao: "))
    if opcao == 1:
        pessoa = input("digite o nome de uma pessoa: ")
        pessoas.append(pessoa)
    elif opcao == 2: 
        print("pessoa atendida")
        pessoas.pop(0)
        print("Pessoa removida!")

    elif opcao == 3:    
        for indice in range(len(pessoas)):
            print(f"{indice + 1} - {pessoas[indice]}")
        print(f"\nQtd. Pessoas: {len(pessoas)}")
    elif opcao == 0:   
        print("saindo ...")
        break
 

