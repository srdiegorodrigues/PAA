# Algoritmo de busca em profundidade para grafos.


graph = {
    'A': ['C', 'B', 'D'],
    'B': ['E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': [],
    'G': ['I'],
    'H': [],
    'I': []
}

def dfs(graph, start, target):
    visited = set() # define um conjunto vazio para receber os nós visitados
    queue = [start] #cria uma fila contendo apenas o nó inicial

    while queue:
        node = queue.pop() #remove o último elemento da fila e o retorna
        
           
        #verifica se o nó visitado é igual ao alvo, caso sim, o adiciona no conjunto de visitados
        if node == target:
            visited.add(node)
            return f" Nós visitados até encontrar o alvo {target}: {visited}" # Retorna os nós visitados até o nó alvo ser encontrado
        
        #verifica se o nó não foi visitado, caso negativo, adiciona o nó no conjunto de visitados
        if node not in visited:
            visited.add(node) # adiciona o nó a visited            
            queue.extend(set(graph[node]) - visited) #retorna os vizinhos que ainda não foram visitados
            print(queue)
    
    
    return f"O alvo {target} não foi encontrado. Nós visitados: {visited}" # Retorna os nós visitados se o nó alvo não for encontrado
            



start = 'A'
target = 'G'

visited_nodes = dfs(graph, start, target) #chamada da função
print(visited_nodes)

""" 
Implementar o algoritmo de busca em profundidade para grafos.

O algoritmo de busca em profundidade começa pelo nó inicial e explora um caminho 
inteiro do grafo antes de retroceder e explorar os outros. Isso significa que a busca 
é realizada aprofundando-se o máximo possível em um caminho antes de volar para explorar outros.

Analisando a complexidade de tempo do algoritmo, podemos observar que:

    A criação do conjunto de nós visitados. O(1).
    A criação da fila queue. O(1).
    O loop while é executado enquanto existir nós dentro da pilha, o que pode ocorrer até V vezes, onde V é o número de vértices no grafo.
    A remoção do último elemento da fila. O(1).
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

    O espaço utilizado pelo algoritmo inclui a pilha de nós a serem visitados e o 
    conjunto de nós visitados. O tamanho da pilha pode chegar a V no pior caso, 
    onde V é o número de vértices do grafo. O tamanho do conjunto de nós visitados 
    também pode chegar a V no pior caso. Portanto, a complexidade de espaço é O(V), 
    sendo V o número de Vértices do grafo
"""