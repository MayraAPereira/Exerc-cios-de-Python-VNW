'''
Dada uma lista de tupla, onde cada tupla contém o nome de uma pessoa e sua idade,
escreva uma função que retorne a lista ordenada pela idade de forma crescente.

'''

def ordernar_tupla(lista_tupla):
    lista_ordenada = sorted(lista_tupla, key=lambda x: x[1])
    return lista_ordenada

lista_de_tuplas = [('Maria', 55), ('Ingridy', 34), ('Stephanny', 32), ('Thiago', 25), ('Mayra', 33), ('Manuella', 12), ('Lourdes', 77)]

print (f'O resultado é: {ordernar_tupla(lista_de_tuplas)}')
