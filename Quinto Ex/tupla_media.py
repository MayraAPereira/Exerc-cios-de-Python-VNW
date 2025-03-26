'''
Dado um dicionário onde as chaves são nomes de alunos e os valores são listas com suas
notas, crie uma função que retorna uma lista de tuplas, onde cada tupla contém o nome do
aluno e sua média de notas.
'''
# função
def calculcar_medias(notas:dict):
    # lista vazia
    lista_medias = []
    # Percorrer o dicionario
    for chave, valor in notas.items():
        # 
        media = round((valor[0] + valor[1] + valor[2]) / len(valor), 2) 
        lista_medias.append( (chave, media) )
    return lista_medias

notas = {'Mayra': [8, 10, 8], 'Stephanny': [10, 9, 9], 'Ingridy': [9, 10, 10], 'Thiago': [8, 9, 9]}

print(calculcar_medias(notas))

# def ordenar_media(lista_alunos):
#     media_alunos = sorted(lista_alunos, key=lambda x: x[1])
#     return media_alunos

# lista_de_alunos = [('Mayra', 8), ('Stephanny', 10), ('Thiago', 6), ('Ingridy', 9)]

# print(ordenar_media(lista_de_alunos))

# Fazer a função ser reutilizavel 