import copy

class AdjacencyList:
    """Classe que abstrai a lista de adjacência
    de um grafo e suas operações.

    Parâmetros
    ----------
        - lines (list): Linhas do arquivo de entrada.
    """

    def __init__(self, lines: list):
        v = 0
        self.__graph = dict()
        for line in lines:
            vertices = line.replace("\n", "").split(",")
            # Converte os vértices para inteiros
            final_vertices = []
            for u in vertices:
                if u != '':
                    final_vertices.append(int(u))
            self.__graph[v] = final_vertices # Atribui os vértices de v
            v += 1
        self.set_graph()
        # print("Grafo: {}".format(self.__graph))

    def set_graph(self):
        """Inicializa uma cópia do grafo para ser usada no algoritmo.
        Pelo fato da estrutura sofrer alteração, trabalha em cima de
        uma cópia para não alterar o grafo original e manter os dados.
        """

        self.__graph_copy = copy.deepcopy(self.__graph)
    
    def get_list_of_vertices(self):
        """Retorna a lista de vértices de um grafo.

        Retorno
        -------
        - vertices (list): Lista contendo os vértices do grafo.
        """

        return list(self.__graph_copy.keys())
    
    def set_induced_graph(self, s: tuple):
        """Cria um grafo induzido G-S a partir de um conjunto S,
        representado pela tupla recebida como parâmetro.
        
        Parâmetros
        ----------
        - s (tuple): Tupla contendo os vértices do conjunto S.
        """

        self.__graph_copy = copy.deepcopy(self.__graph)
        for v in s:
            adj_vertices = self.__graph_copy.pop(v)
            for w in adj_vertices:
                if w != v:
                    self.__graph_copy[w].remove(v)

    def find_neighbors(self, v: int):
        """Retorna os vizinhos de um vértice v.
        
        Parâmetros
        ----------
        - v (int): Vértice de entrada.

        Retorno
        -------
        - neighbors (list): Lista contendo os vizinhos de v.
        """

        neighbors = []
        for w in self.__graph_copy[v]: # Para cada vértice adjacente a v
            # Se w não é igual a v e w não foi adicionado na lista de vizinhos
            if w != v and w not in neighbors:
                neighbors.append(w) # w é vizinho de v
        
        return neighbors

    def is_eulerian(self):
        """Retorna se um grafo é euleriano.
        Ou seja, se possui todos os vértices com grau par.
        
        Retorno
        -------
        - is_eulerian (bool): Booleano indicando se um grafo é euleriano ou não.
        """

        for v, adj_vertices in self.__graph.items(): # Para cada vértice e seus vértices adjacentes
            degree = len(adj_vertices) # O grau equivale ao tamanho da lista de vértices adjacentes
            count_loop = 0
            for w in adj_vertices:
                if v == w:
                    count_loop += 1
            if count_loop >= 1: # Indica laço: Conta como 2
                degree += count_loop # Adiciona a quantidade de v novamente
            
            if degree % 2 != 0: # Verifica se o vértice v possui grau ímpar
                return False # Retorna falso caso v tenha grau ímpar
        return True # Retorna verdadeiro caso todos os vértices tenham grau par

    def count_edges(self):
        """Retorna a quantidade de arestas que incidem em cada vértice.
        
        Retorno
        -------
        - count_edges_of_vertices (dict): Dicionário contendo
        a quantidade de arestas de cada vértice.
        """

        count_edges_of_vertices = dict()
        for v in self.__graph.keys(): # Para cada vértice do grafo
            # A quantidade de arestas é o tamanho da lista de vértices adjacentes de v
            count_edges_of_vertices[v] = len(self.__graph[v])
        
        return count_edges_of_vertices
    
    def traverse(self, curr_v: int):
        """Atravessa uma aresta (u,v) do grafo.
        
        Parâmetros
        ----------
        - curr_v (int): Vértice de origem.

        Retorno
        -------
        - next_v (int): Vértice de destino.
        """

        # O próximo vértice é sempre o primeiro da lista de adjacência do vértice atual
        next_v = self.__graph_copy[curr_v][0]
        # Remove a aresta (u,v) e (v,u) quando u e v são vértices diferentes
        self.__graph_copy[curr_v].remove(next_v)
        if curr_v != next_v: # Se for um laço, não precisa remover duas vezes
            self.__graph_copy[next_v].remove(curr_v)
        
        return next_v
