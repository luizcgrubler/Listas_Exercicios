# Arquivo: 09_central_missoes.py

# Desenvolva um menu para registrar as pontuações das missões de um robô:

# 1 - Registrar pontuação
# 2 - Mostrar relatório
# 3 - Desfazer o último registro
# 0 - Sair
# Comece com uma lista vazia de pontuações. 
# Na opção 1, leia um inteiro de 0 a 100. Repita a leitura enquanto estiver fora da faixa e adicione apenas o valor válido.
# Na opção 2, mostre as pontuações na ordem de registro, a quantidade, o total, a média e a maior pontuação. Mostre também quantas missões tiveram pelo menos 70 pontos.
# Se a lista estiver vazia, o relatório deve informar que não há missões registradas, sem calcular média ou maior pontuação.
# Na opção 3, remova e mostre a última pontuação com pop(). Se a lista estiver vazia, informe que não há registro para desfazer.
# A opção 0 encerra o programa. Outras opções mostram uma mensagem de erro.
# Teste de mesa: registre 80, 60 e 100. O relatório deve mostrar três missões, total 240, média 80.0, maior pontuação 100 e duas missões com pelo menos 70 pontos. Desfaça o último registro: restarão [80, 60], com média 70.0 e uma missão com pelo menos 70 pontos.

# Desafio adicio nal: crie outra lista contendo somente as pontuações a partir de 70, sem modificar a lista original.



pontuacoes = []

while True: 
    print("\n === Central de missoes ===")
    print("1 registrar pontuacao")
    print("2 mostrar relatorio")
    print("3 desfazer o ultimo registro")
    print("0 sair")

    opcao = int(input("escolha uma opcao:"))

    if opcao == 1:
        pontuacao = int(input("digite a pontuacao da missao (0 a 100):"))

        while pontuacao < 0 or pontuacao > 100:
            print("pontuacao invalida. digite uma pontuacao entre 0 e 100")
            pontuacao = int(input("digite a pontuacao da missao (0 a 100):"))

        pontuacoes . append(pontuacao)
        print("pontuacao registrada com sucesso")    

    elif opcao == 2:
        if not pontuacoes:
            print("nao existe missoes registradas.") 
        else:
            print("pontuacoes: ", pontuacoes)   
            print("quantidade de missoes:", len(pontuacoes))
            print("total:",sum(pontuacoes))
            print("media:", sum(pontuacoes)/ len(pontuacoes))
            print("maior pontuacao: ", max(pontuacoes))

            acima_70 = 0
            for valor in pontuacoes:
                if valor >= 70:
                    acima_70 += 1

            print("missoes com pelo menos 70 pontos:", acima_70)   

    elif opcao == 3:
        if not pontuacoes:
            print("nao a registro para desfazer.") 
        else:
            removida = pontuacoes.pop()  
            print(f"ultima pontuacao removida: {removida}")   
            print("lista atual", pontuacoes)  

    elif opcao == 0:
        print("programa encerrado")       
        break

    else:
        print("opcao invalida")

        pontuacoes_70 = [p for p in pontuacoes if p >= 70]

        print("pontuacoes maiores ou iguais a 70:", pontuacoes_70)