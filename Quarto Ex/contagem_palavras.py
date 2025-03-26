'''
Crie uma função que recebe uma string e conta quantas vezes cada palavra aparece nela.
Retorne um dicionário onde a chave é a palavra e o valor é a quantidade de ocorrências.
'''

def contar_palavra(string):
    contador = {}
    lista = string.split(', ')
    for palavra in lista:
        if not palavra in contador.keys():
            contador[palavra] = lista.count(palavra)
            
    return contador

palavras = 'banana, maça, goiaba, pera, pera, mamão, maça, banana, banana'

print(f'O retorno são: {contar_palavra(palavras)}')

# def contar_palavras(animal):
#     contador = {}
#     lista = animal.split(' ')
#     for palavra in lista:
#         if not palavra in contador.keys():
#             contador[palavra] = lista.count(palavra)         
#     return contador

# animais = 'leão, leão, leão, cobra, elefante, foca, peixe, cachorro, gato, gato, leão, foca, gato'

# print(contar_palavras(animais))