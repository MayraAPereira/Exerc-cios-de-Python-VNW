'''
Dada uma lista de tupla, onde cada tupla contém o nome de uma pessoa e sua idade,
escreva uma função que retorne a lista ordenada pela idade de forma crescente.

'''

def ordernar_tupla(lista_tupla):
    lista_ordenada = sorted(lista_tupla, key=lambda x: x[1])
    return lista_ordenada

lista_de_tuplas = [('Samuel', 23), ('Karynne', 20), ('Carol', 22), ('Jonathan', 15)]

print(ordernar_tupla(lista_de_tuplas))