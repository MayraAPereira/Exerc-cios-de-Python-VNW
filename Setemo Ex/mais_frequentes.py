'''
Dada uma lista de números, crie uma função que retorne os três números mais frequentes
em ordem decrescente de frequência. Se houver empates, ordene pelo valor numérico.
'''

def contar_top3_mais_frequentes(numeros:list):
    frequencia = {}
    
    for numero in numeros:
        
        if numero in frequencia.keys():
            frequencia[numero] +=1
        else:
            frequencia[numero] = 1
            
        numeros_ordenados = sorted(frequencia.keys(), key=lambda chave: (frequencia[chave], chave), reverse=True)
        
    return numeros_ordenados[:3]
            
lista_numeros = [1,1,1,2,4,5,5,2,2,2,5,5,1]

print(contar_top3_mais_frequentes(lista_numeros)) 