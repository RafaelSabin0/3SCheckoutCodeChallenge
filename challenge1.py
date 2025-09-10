 #Escreva uma função que determina se uma string termina com ‘A’ e começa com 'B'

def validateFirstAndLastCharacter(word:str):

    if word.startswith("b") and word.endswith("a"):
        return print(True)
    
    return print(False)

