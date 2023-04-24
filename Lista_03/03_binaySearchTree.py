#3. Implemente a estrutura de dados binary search tree e os m´etodos buscar e inserir.


#classe de criação do nó
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

#classe de criação da árvore binária
class BinaryTree:
    def __init__(self, data=None, node=None):             
        if node:
            self.root = node        
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None
        self.visited_nodes = []  


#classe de criação da árvore binária de busca
class BinarySearchTree(BinaryTree):    
    def insert(self, newNode):
        parent = None
        x = self.root
        while (x):
            parent = x
            if newNode < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(newNode)
        #envia os vértices de menor valor para a esquerda do nó pai
        elif newNode < parent.data:
            parent.left = Node(newNode)
        #envia os vértices de maior valor para a direita do nó pai
        else:
            parent.right = Node(newNode)
    
    def search(self, value):
        #criar uma lista que recebe os nós visitados até achar o alvo
        self.visited_nodes = []
        #chama a função _search passando o alvo e o nó raiz
        return self._search(value, self.root)
        
    
    def _search(self, value, node):              
        if node is None:                       
            return node
        self.visited_nodes.append(node.data)  
        if node.data == value:            
            return BinarySearchTree(node)
        if value < node.data:              
            return self._search(value, node.left)        
         
        return self._search(value, node.right)
    
    def show_visited_nodes(self):
        return self.visited_nodes
           

#        return self.visited_nodes


items = [30,25,38,89,77,72,33,28,31,12,15]

bst = BinarySearchTree()
for v in items:
    bst.insert(v)

value = 28


key = bst.search(value)
if key is None:
    print(f"\nO valor {value} não foi encontrado")                
else:
    print(f"\n{key.root.data} encontrado.")

print(f"Nós visitados: {bst.show_visited_nodes()} ")
print(
""" 
Modelo da árvore binária implementada pelo array do teste
             30
            /  \\
           25   38
          / \   / \\
         12 28 33  89
           \   /  /
           15 31 77
                /
               72

""")

"""
 
Complexidade de custo de tempo

    A complexidade de custo do algoritmo de árvore de busca binária 
    depende do tipo de operação que está sendo realizada.
        Função de recorrência: T(n) = T(k) + T(n - k - 1) + c
        onde k é o número de nós na subárvore esquerda, n - k - 1 
        é o número de nós na subárvore direita, e c é o tempo para visitar um nó.

    A complexidade de tempo média para pesquisar um elemento em uma 
    árvore de busca binária balanceada é O(log n), onde "n" é o número 
    de elementos na árvore. No entanto, no pior caso, a árvore pode 
    degenerar em uma lista, e a complexidade da pesquisa se torna O(n), 
    onde "n" é o número de elementos na árvore.

    Para inserir um elemento em uma árvore de busca binária, a complexidade 
    de tempo é O(log n) no caso médio e O(n) no pior caso.
    Para ambos os casos, n equivale a altura da árvore

    
Complexidade de custo de espaço

A função de custo de espaço de uma árvore binária de busca depende do número
de nós e da estrutura da árvore. Em uma árvore binária de busca com "n" nós 
balanceada, a função de custo de espaço é O(n), que é linear. Isso ocorre porque 
a árvore precisa armazenar "n" nós, cada um com uma chave e referências para seus 
filhos esquerdo e direito. No entanto, se a árvore não estiver balanceada, a
função de custo de espaço pode chegar a O(n²) no pior caso, devido ao fato de 
a árvore estar muito desequilibrada e ter muitos nós extras, como em uma árvore 
degenerada em uma lista.
"""
