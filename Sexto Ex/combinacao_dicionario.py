'''
Escreva uma função que recebe dois dicionários onde as chaves são strings e os valores são
inteiros. A função deve combinar os dicionários somando os valores das chaves que
aparecem em ambos.
'''

dicionario_1 = {'A':2, 'B':1, 'C':4}
dicionario_2 = {'A':1, 'B':1, 'C':3}

def combinar_dicts(dicionario_1: dict, dicionario_2: dict):
    novo_dicionario = {}
    
    for chave_dict1, valor_dict1 in dicionario_1.items():
        
        for chave_dict2, valor_dict2 in dicionario_2.items():
            
            if chave_dict1 == chave_dict2:
                novo_dicionario[chave_dict1] = valor_dict1 + valor_dict2
            elif chave_dict1 != chave_dict2:
                novo_dicionario[chave_dict1] = valor_dict1
                novo_dicionario[chave_dict2] = valor_dict2
    return novo_dicionario

print(combinar_dicts(dicionario_1, dicionario_2))

#TAREFA -> CONCERTA A LOGICA 