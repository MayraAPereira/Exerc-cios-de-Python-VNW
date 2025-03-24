'''
Crie uma função que recebe uma string e conta quantas vezes cada palavra aparece nela.
Retorne um dicionário onde a chave é a palavra e o valor é a quantidade de ocorrências.
'''

def contar_palavras(animais):
    contador = {}
    lista = animais.split(' ')
    for palavra in lista:
        if not palavra in contador.keys():
            contador[palavra] = lista.count(palavra)         
    return contador

animais = 'leão, leão, leão, cobra, elefante, foca, peixe, cachorro, gato, gato, leão, foca, gato'

print(contar_palavras(animais))