"""
Crie uma função que recebe o número de casas do tabuleiro e devolve:
1 - Quantidade mínimo de turnos para se chegar ao destino (caminho ótimo);
2 - Probabilidade de um usuário conseguir executar o caminho ótimo;
3 - Quantas combinações de movimentos diferentes um jogador conseguiria
 executar sem efetuar nenhum looping no tabuleiro.
"""

import math
import random

def gameStats(qtdCasas:int):
    max_pts_roletas = 3
    roleta_sequencia_pts = [1, 2, 3]
    turnos:int = math.ceil(qtdCasas/max_pts_roletas)
    possibilidadesValidasList:list = []
    contadorTodasAsPossibilidades:int = 0

    for _ in range(qtdCasas):
        possibilidades = [random.choice(roleta_sequencia_pts) for _ in range(turnos)]
        contadorTodasAsPossibilidades += 1
        if sum(possibilidades) == qtdCasas:
            possibilidadesValidasList.append(possibilidades)
       # print(possibilidades)
    
    probabilidade = len(possibilidadesValidasList)/contadorTodasAsPossibilidades

    #so faltou ajustar a qtd de combinacoes sem loop, mas ainda nao tinha conseguido a execucao ideal

    
    return {"Qtd Minima de Turnos": turnos, "Probabilidade do usuário conseguir executar o caminho ótimo": probabilidade, "Combinacoes sem loop": "sem resposta por enquanto"}
    

print(gameStats(10))