# Algoritmo de busca em largura para grafos



from collections import deque
"""
Obs: Deque é preferível a uma lista nos casos em que precisamos de operações append e pop mais rápidas de ambas as 
extremidades do contêiner, pois deque fornece uma complexidade de tempo O(1) para operações append e pop em 
comparação com uma lista que fornece O(n) complexidade de tempo.
"""

graph = {0: {1, 4, 5},
         1: {0, 2, 6},
         2: {1, 3, 6},
         3: {2, 4, 7},
         4: {0, 3, 8},
         5: {0, 6, 8},
         6: {1, 2, 5},
         7: {3, 8, 9},
         8: {4, 5, 7},
         9: {7}}

def bfs(graph, target, start=0):
    visited = set([]) # conjunto para armazenar os nós já visitados
    queue = deque([start]) # cria uma fila e adiciona o elemento inicial. Armazenará os nós a serem explorados no grafo
    
    #executa um loop enquanto existir nós dentro da fila
    while queue:
        node = queue.popleft() # remove um elemento da extremidade esquerda da fila(1º elemento) e o retorna.       

        #verifica se o nó visitado é igual ao alvo, caso sim, retorna a lista de visitados até aquele momento
        if node == target:
            visited.add(node) # adiciona o nó a visited      
            return f" Nós visitados antes de encontrar o alvo {target}: {visited}" # Retorna os nós visitados até o nó alvo ser encontrado

        #verifica se o nó não foi visitado, caso negativo, adiciona o nó no conjunto de visitados
        if node not in visited:
            visited.add(node) # adiciona o nó a visited
            queue.extend(graph[node] - visited)  #retorna os vizinhos que ainda não foram visitados
    
    return f"O alvo {target} não foi encontrado. Nós visitados: {visited}" # Retorna os nós visitados se o nó alvo não for encontrado


target = 3

visited = bfs(graph, target)

print (visited)



""" 

Implementar o algoritmo de busca em largura para grafos.

O algoritmo de busca em largura começa pelo nó inicial e explora todos os 
seus vizinhos antes de se mover para os próximos nós adjacentes 
aos já visitados. Isso significa que a busca é realizada em camadas, explorando todos os 
nós de uma camada antes de avançar para a próxima.

Analisando a complexidade de tempo do algoritmo, podemos observar que:

    A criação do conjunto de nós visitados. O(1).
    A criação da fila deque. O(1).
    O loop while é executado enquanto existir nós dentro da fila, o que pode ocorrer até V vezes, onde V é o número de vértices no grafo.
    A remoção do primeiro elemento da fila. O(1).
    A verificação se o nó visitado é igual ao alvo. O(1).
    A adição do nó visitado ao conjunto de visitados. O(1).
    A verificação se o nó não está na fila de visitados. O(1).
    A adição do nó visitado ao conjunto de visitados. O(1).
    A extensão da fila com os nós adjacentes não visitados ao nó atual. O(E).
    
Calcular a complexidade de tempo:
    
    
    Não há garantia de que o alvo será encontrado, por isso o pior caso deve ser considerado. 
    No pior caso, o algoritmo visitará todos os nós do grafo, ou seja, sua complexidade de tempo 
    é O(V+E), onde V é o número de vértices e E é o número de arestas do grafo.

Calcular a complexidade de espaço:

    A complexidade de espaço do algoritmo é dominada pelo conjunto de nós visitados e pela 
    fila de nós a serem visitados, ambos podendo ter até V elementos. Portanto, a complexidade de espaço é de O(V).

"""
