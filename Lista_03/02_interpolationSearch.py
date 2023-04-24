#2. Implemente o metodo interpolation search.
#O algoritmo Interpolation Search é uma técnica de 
#busca que utiliza uma fórmula matemática para estimar a posição da chave buscada.


def interpolationSearch(array, item):
    begin = 0 #recebe o índice 0
    end = len(array) - 1 # recebe o último índice
    #executa o laço enquanto todas as restrições não forem atendidas.
    if array[begin] == array[end]:
        return -2
    while begin <= end and array[begin] <= item <= array[end]:
        #fórmula de interpolação
        position = (begin +((item - array[begin])*(end - begin)// (array[end] - array[begin])))
        #verifica se o valor encontrado na posição é igual o item e o retorna 
        print(position, end=" ")       
        if array[position] == item:
            return position            
        #verifica se o valor encontrado é menor que o do item        
        elif array[position] < item:
            #passa a considerar como índice inicial do array, o encontrado em position + 1
            begin = position+1
        else:
            #passa a considerar como índice final do array, o encontrado em position - 1
            end = position - 1       
    return -1
#array de valores iguais
arrayRep = [5] * 10

#array de valores distribuídos uniformemente
array = [1,2,3,4,5,6,7,8,9,10]

#array de valores exponenciais
arrayExp = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024,1025,2048]
item = 5
search = interpolationSearch(array, item)


print("\n",array)
if search == -1:
    print(f"\nO item {item} não foi encontrado")
elif search == -2:
    print(f"O array contém apenas números repetidos, ou não está ordenado")    
else:
    print(f"\nO item {item} está na posição {search}")


""" 

Complexidade de custo de tempo

Assim como na busca binária, o desempenho da busca interpolada (interpolation search) 
é medido pela função de custo, que determina o número de operações necessárias para 
encontrar o elemento procurado. No entanto, a função de custo da busca interpolada 
varia de acordo com a distribuição dos elementos na estrutura de dados.

Função de recorrência:
    T(n) = T(n/2) + O(log(log(n))) ->Onde n é o tamanho do array e c representa o 
    tempo constante necessário para realizar as comparações e atribuições na função.

    Pior caso: no pior caso da busca interpolada, o elemento procurado não está presente 
    na estrutura de dados, está localizado em uma das extremidades da estrutura ou os
    valores não estáo distribuídos uniformemente. Nesse     caso, a função de custo é O(n),
      onde n é o número de elementos na estrutura de dados.
                Pior caso: O(n) -> valores exponencialmente distribuídos, ausencia do item procurado, 
                ou o item procurado está em uma das extremidades.

    Caso médio: no caso médio da busca interpolada, a distribuição dos elementos na estrutura 
    é uniforme. Nesse caso, a função de custo é O(log(log n), onde n é o número de 
    elementos na estrutura de dados.
                Caso médio: O(log(log n)) -> para valores uniformemente distribuídos

    Melhor caso: no melhor caso da busca interpolada, o elemento procurado está localizado 
    no centro da estrutura de dados uniformemente distribuída. Nesse caso, a função de custo 
    é O(1), pois o elemento pode ser encontrado diretamente na posição estimada.
                Melhor caso: O(1)
Desvantagem:
    Em situações práticas, as chaves tendem a se aglomerar em torno de determinados valores e
    não são uniformemente distribuídas

Complexidade de custo de espaço

A função de custo de espaço do algoritmo de Interpolation Search é O(1), que é constante.
Isso ocorre porque o algoritmo não usa estruturas de dados extras, apenas variáveis ​​locais 
para armazenar as posições de início e fim da pesquisa.
"""
