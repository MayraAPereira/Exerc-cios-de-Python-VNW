'''
Escreva 
'''

def somar_pares(lista):
    resultado = 0
    for item in lista:
        if item %2 == 0:
            resultado += item
    
    return resultado

lista_numeros = [9, 3, 1, 7, 4, 2, 8, 5, 6]


print(f'O resultado da soma dos elementos pares é: {somar_pares(lista_numeros)}')


# print(f'O resultado da soma é: {numero_1 + numero_2}')

