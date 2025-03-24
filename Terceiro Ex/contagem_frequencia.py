'''
Escreva uma função que recebe uma string e retorna um dicionário onde as chaves são os
caracteres da string e os valores representam quantas vezes cada caractere aparece.
'''

def contar_frequencia(palavra):
    dicionario = {}
    lista = palavras.split(', ')
    for item in lista:
        if not item in dicionario.keys():
            dicionario[item] = lista.count(item)    
    return dicionario

palavras = 'Java, Java, Java, Java, JavaScript, Python, Ruby, Lua, Ruby, Python, Java, Java, Rust, Cobol'

print(contar_frequencia(palavras))