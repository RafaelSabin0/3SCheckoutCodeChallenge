"""
Considerando a a sequência numérica a seguir (11, 18, 25, 32, 39... ) faça uma função que 
recebe como entrada uma posição e devolve qual o valor do número naquela posição, considerando
a sequência numérica apresentada, para todos os efeitos, a sequência começa da posição 1.

Ex:
print_valor(x=1) retornará 11; print_valor(x=2) retornará 18; print_valor(x=200)
retornará 1404; print_valor(x=254) retornará 1.782;
print_valor(x=3.542.158) retornará 24.795.110;
"""

def print_valor(arr:list, posicao:int):
    if len(arr) <= 1:
        return print("São necessários no mínimo 2 valores para calcular a progressão aritmética") 
    

    razao = arr[1] - arr[0]
    posicaoFormatada = posicao - 1

    return print(f"O {posicao}° item dessa progressão é: {arr[0] + (posicaoFormatada * razao)}")


print_valor([11, 18, 25, 32, 39], 254)
print_valor([11, 18, 25, 32, 39], 3542158)
print_valor([11], 256)
print_valor([11,18], 200)
