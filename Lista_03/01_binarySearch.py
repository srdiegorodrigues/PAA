#1. Implemente o algoritmo de busca binária.

array = [2,5,7,8,9,11,16,18,21, 23, 25, 28, 39, 45, 49, 51]

print(f"Array:\n{array}")


def binarySearch(array, item, begin=0, end=None):
    #uma condição para verificar o tamanho do array.

    if end is None: 
        #diminui número de elementos do array por 1
        end = len(array) - 1
    if begin <= end: # Theta(1)
        # divide o array por dois arredondando o valor para baixo em caso de número fracionado
        middle = (begin + end)//2
        print(middle, end=" ")
        #compara o elemento encontrado na operação anterior com o item buscado 
        if array[middle] == item: # Theta(1)
            #retorna o índice do elemento quando encontrado
            return {middle} 
        # compara se o item é menor que o valor armazenado pelo resultado da divisão
        elif item < array[middle]: # Theta(1)
            #retorna a função, recursivamente, passando como parâmetro final o índice do meio - 1             
            return binarySearch(array, item, begin, middle-1) 
        else: # Theta(1)
            #retorna a função, recursivamente, passando como parâmetro inicial o índice do meio + 1            
            return binarySearch(array, item, middle+1, end) 
    # se o elemento não for encontrado, retorna -1
    return -1 

item = 11
search = binarySearch(array, item)
if search != -1:
    print(f"\nO item {item} está na posição {search}")
else:
    print(f"\nO item {item} não foi encontrado")





""" 

Complexidade de custo de tempo

    Pior caso: no pior caso, o elemento procurado não está presente na estrutura de dados e o algoritmo 
    precisa percorrer toda a estrutura para chegar a essa conclusão. A função de custo para o pior caso é 
    O(log n), onde n é o número de elementos na estrutura de dados.
        Pior caso = T(n/2) + 1 ->  O(log n)  -> onde n é o tamanho do array e c representa o tempo constante 
        necessário para realizar as comparações e atribuições na função.
        
    Caso médio: no caso médio, o elemento procurado está presente na estrutura de dados e sua posição é 
    aleatória. Nesse caso, a função de custo é O(log n), onde n é o número de elementos na estrutura de dados.
        Caso médio caso = T(n/2) + 1 -> O(log n)

    Melhor caso: no melhor caso, o elemento procurado é o elemento central da estrutura de dados. 
    Nesse caso, a função de custo é O(1), pois o algoritmo encontra o elemento na primeira comparação.
        Melhor Caso = T(1) -> O(1)

Complexidade de custo de espaço

A função de custo de espaço do algoritmo de busca binária é O(1), que também é constante. 
Isso ocorre porque o algoritmo não usa estruturas de dados extras. Durante a pesquisa, 
apenas um pequeno número de variáveis ​​locais é usada para armazenar os valores atuais de 
início, fim e meio do intervalo de pesquisa.


"""
