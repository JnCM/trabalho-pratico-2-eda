import copy

class IncidenceMatrix:
    """Classe que abstrai a matriz de incidência
    de um grafo e suas operações.

    Parâmetros
    ----------
        - lines (list): Linhas do arquivo de entrada.
    """

    def __init__(self, lines: list):
        self.__graph = []
        for line in lines:
            temp_line = line.replace("\n", "").split(" ")
            # Converte os valores da matriz para inteiros
            temp_line = [int(e) for e in temp_line]
            self.__graph.append(temp_line) # Adiciona uma linha na matriz
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

        return list(range(len(self.__graph_copy)))

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
        for e in range(len(self.__graph_copy[v])): # Para cada aresta incidente a v
            if self.__graph_copy[v][e] == 1: # Se e é incidente a v
                for w in range(len(self.__graph_copy)): # Para cada vértice do grafo
                    # Verifica quem é o outro vértice que liga em e que não seja v
                    # e não esteja adicionado na lista de vizinhos de v
                    if self.__graph_copy[w][e] == 1 and w != v and w not in neighbors:
                        neighbors.append(w) # w é vizinho de v
                        break
        
        return neighbors

    def is_eulerian(self):
        """Retorna se um grafo é euleriano.
        Ou seja, se possui todos os vértices com grau par.
        
        Retorno
        -------
        - is_eulerian (bool): Booleano indicando se um grafo é euleriano ou não.
        """

        for u in range(len(self.__graph)): # Para cada vértice do grafo
            degree_of_u = 0
            for e in range(len(self.__graph[u])): # Para cada aresta incidente a u
                degree_of_u += self.__graph[u][e] # Basta somar quantas arestas incidem em u
            
            if degree_of_u % 2 != 0: # Verifica se o vértice u possui grau ímpar
                return False # Retorna falso caso u tenha grau ímpar
        return True # Retorna verdadeiro caso todos os vértices tenham grau par
    
    def count_edges(self):
        """Retorna a quantidade de arestas que incidem em cada vértice.
        
        Retorno
        -------
        - count_edges_of_vertices (dict): Dicionário contendo
        a quantidade de arestas de cada vértice.
        """

        count_edges_of_vertices = dict()
        for u in range(len(self.__graph)): # Para cada vértice do grafo
            count = 0
            for v in range(len(self.__graph[u])): # Para cada aresta incidente a u
                if self.__graph[u][v] == 2: # Um laço conta como uma aresta incidindo duas vezes em u
                    count += 1 # Conta a aresta apenas uma vez
                else: # Soma os valores que indicam que há aresta incidindo em u
                    count += self.__graph[u][v]
            count_edges_of_vertices[u] = count
        
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

        # O próximo vértice é sempre o primeiro vértice que tem a mesma aresta incidente encontrada na matriz
        for edge in range(len(self.__graph_copy[curr_v])):
            if self.__graph_copy[curr_v][edge] == 2:
                # Se a aresta é um laço, o próximo vértice é igual ao atual
                next_v = curr_v
                break
            elif self.__graph_copy[curr_v][edge] == 1: # Encontra aresta não visitada
                for w in range(len(self.__graph_copy)): # Acha o vizinho desta aresta
                    if self.__graph_copy[w][edge] == 1 and w != curr_v:
                        next_v = w
                        break
                break
        
        # Remove a aresta (u,e) e (v,e) quando u e v são vértices diferentes
        self.__graph_copy[curr_v][edge] = 0
        if curr_v != next_v: # Se for um laço, não precisa remover duas vezes
            self.__graph_copy[next_v][edge] = 0
        
        return next_v
