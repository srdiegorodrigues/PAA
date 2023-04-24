# Algoritmo SequentialSearch2

def sequential_search_2(array, element):
    
    n = len(array) 
    i = 0    
    array.append(element)
    #enquanto o elemento do índice for diferente do elemento buscado o laço é executado
    
    while array[i] != element:
        i += 1
    array.pop() #remove o elemento sentinela da lista
    
    #compara o índice i com o índice n. Se for diferente, significa que ele foi encontrado
    if i != n:
        return f"\nO elemento {element} foi encontrado e está no índice {i}\n" #retorna o elemento quando encontrado e informa em qual índice
    else:
        return f"\nO elemento {element} não foi encontrado no array\n" #informa ao usuário que o elemento não existe no array
    
    


array = [8, 10, 15, 22, 17, 18, 25, 30]
element = 30

print(sequential_search_2(array, element))


""" 

Implementar o algoritmo SequentialSearch2 (Ver Secão 3.2 Introduction to the Design and 
Analysis of Algorithms (3rd Edition) - Anany Levitin).

Recebe uma lista 'array' e um elemento 'element' a ser buscado.
Retorna o índice do elemento se encontrado, ou uma mensagem informando que não o encontrou.


Analisando a complexidade de tempo do algoritmo, podemos observar que:

    Atribuição da variável n com o tamanho do array (n = len(array)) é O(1).
    Atribuição da variável i com valor 0 é O(1).
    O laço while executa no máximo n vezes ou até encontrar o elemento desejado. O pior caso é quando 
    o elemento não está presente e é necessário percorrer todo o array. Nesse caso, a complexidade de tempo é O(n).
    A verificação final if i != n: é O(1).
    A instrução return é O(1).
    Somando todas as complexidades e levando em consideração o elemento de maior expoente, temos que a complexidade de tempo do algoritmo é O(n), ou seja
    ela é linear


Complexidade de espaço:

    A atribuição das variáveis n e i é O(1).
    Não são criadas outras variáveis no algoritmo.
    Portanto, a complexidade de espaço do algoritmo é O(1).
"""
