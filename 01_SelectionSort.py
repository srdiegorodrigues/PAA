# Algoritmo Selection Sort


def selectionSort(array):

    #executa um loop até percorrrer todos os índices da lista e encontrar o índice do menor elemento
    for i in range(len(array)): 
        #armazena o índice do menor elemento
        min_i = i        

        #executa um loop no restante dos elementos à direita do elemento.
        for right_element in range(i + 1, len(array)):            

            #comparara o elemento à direita com o valor armazenado na variavel min_i
            if array[right_element] < array[min_i]:
                #se o elemento a direita for menor, substitui o index da variavel min_i pelo índice do elemento à direita
                min_i = right_element      
        
        array[i], array[min_i] = array[min_i], array[i]
     
    
array = [6,1,5,2,8,6,3,4,2,1,5]

print(f"Array original:\n{array}")
selectionSort(array) #chamada para ação
print(f"Array ordenado pelo método Selection Sort:\n{array}") 

""" 
Implementar o algoritmo Selection Sort

O algoritmo Selection Sort é um método simples de ordenação de elementos em uma lista ou array. 
A ideia básica dele é selecionar repetidamente o menor elemento da lista e colocá-lo 
na sua posição correta ordenando a lista.


Analisando a complexidade de tempo do algoritmo, podemos observar que:

    O primeiro loop percorre todos os índices da lista. O número de iterações desse loop é igual ao 
    tamanho da lista, portanto seu custo é O(n), onde n é o tamanho da lista.

    O segundo loop  percorre os elementos à direita do elemento atual no loop externo. 
    O número de iterações desse loop é igual ao número de elementos à direita do elemento 
    atual, que é n - i - 1, onde n é o tamanho da lista e i é o índice atual do loop externo.
    Portanto, o custo desse loop é O(n-i).

Complexidade de tempo:
    Sua complexidade de tempo é O(n^2) no pior caso e O(n) no melhor caso. 

Complexidade de espaço:

    O algoritmo Selection Sort opera diretamente no array de entrada, sem criar nenhuma outra estrutura de dados adicional.
    Portanto, a complexidade de espaço do algoritmo é O(1).
"""
