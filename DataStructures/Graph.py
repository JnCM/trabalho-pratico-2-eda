from itertools import combinations
from DataStructures.Stack import Stack
from DataStructures.GraphStructures.AdjacencyList import AdjacencyList
from DataStructures.GraphStructures.AdjacencyMatrix import AdjacencyMatrix
from DataStructures.GraphStructures.IncidenceMatrix import IncidenceMatrix

class Graph:
    """Classe que abstrai a implementação de um grafo
    de maneira encapsulada.

    Parâmetros
    ----------
        - filename (str): Nome do arquivo de entrada
    """

    def __init__(self, filename: str):
        # Leitura do arquivo
        file = open(filename, "r")
        lines_of_file = file.readlines()
        file.close()

        # Indica se o grafo é lista de adjacência
        self.__is_adjacency_list = False
        # Cria a instância do grafo de acordo com os dados
        self.__graph = self.create_graph(lines_of_file)

    def create_graph(self, lines: list):
        """Cria a instância do grafo de acordo com
        o arquivo de entrada.
        
        Parâmetros
        ----------
        - lines (list): Linhas do arquivo lido de entrada.

        Retorno
        -------
        - graph (AdjacencyList | AdjacencyMatrix | IncidenceMatrix): Instância do grafo.
        """

        if ',' in lines[0]: # Se o arquivo de entrada possui vírgulas
            # É lista de adjacência
            graph = AdjacencyList(lines)
            self.__is_adjacency_list = True
        elif len(lines[0].replace("\n", "").split(" ")) == len(lines): # Se as linhas são iguais as colunas
            # É matriz de adjacência (|V| x |V|)
            graph = AdjacencyMatrix(lines)
        else: # Se não, é o último caso
            # É matriz de incidência (|V| x |A|)
            graph = IncidenceMatrix(lines)
        
        return graph
    
    def set_graph(self):
        """Inicializa uma cópia do grafo para ser usada no algoritmo.
        Pelo fato da estrutura sofrer alteração, trabalha em cima de
        uma cópia para não alterar o grafo original e manter os dados.
        """

        # Implementação encapsulada de acordo com a ED utilizada
        self.__graph.set_graph()
    
    def get_list_of_vertices(self):
        """Retorna a lista de vértices de um grafo.

        Retorno
        -------
        - vertices (list): Lista contendo os vértices do grafo.
        """

        # Implementação encapsulada de acordo com a ED utilizada
        return self.__graph.get_list_of_vertices()

    def find_neighbors(self, v: int):
        """Retorna os vizinhos de um vértice v.
        
        Parâmetros
        ----------
        - v (int): Vértice de entrada.

        Retorno
        -------
        - neighbors (list): Lista contendo os vizinhos de v.
        """

        # Implementação encapsulada de acordo com a ED utilizada
        return self.__graph.find_neighbors(v)

    def dfs(self, v: int, visited: list):
        """Algoritmo de busca em profundidade.
        
        Parâmetros
        ----------
        - v (int): Vértice de entrada.
        - visited (list): Lista de booleanos dos vértices visitados.
        """

        visited[v] = True
        neighbors_of_v = self.find_neighbors(v)
        for w in neighbors_of_v: # Para cada vértice adjacente de v
            if not visited[w]:
                self.dfs(w, visited)

    def depth_first_search_components(self):
        """Inicializa o algoritmo de busca em profundidade.
        Calcula o número de componentes de um grafo.
        
        Retorno
        -------
        - count_components (int): Quantidade de componentes de um grafo.
        """

        count_components = 0
        vertices = self.get_list_of_vertices()
        # Inicializa o dicionário de visitados
        visited = dict()
        for v in vertices:
            visited[v] = False
        
        for v in vertices: # Para cada vértice v do grafo
            if not visited[v]:
                self.dfs(v, visited)
                count_components += 1
        
        # print("Número de componentes: {}".format(count_components))
        return count_components

    def is_connected(self):
        """Retorna se um grafo é conectado.
        Ou seja, analisa se um grafo possui apenas 1 componente.
        
        Retorno
        -------
        - is_connected (bool): Booleano indicando se um grafo é conectado ou não.
        """

        # Implementação encapsulada de acordo com a ED utilizada
        return self.depth_first_search_components() == 1

    def is_eulerian(self):
        """Retorna se um grafo é euleriano.
        Ou seja, se possui todos os vértices com grau par.
        
        Retorno
        -------
        - is_eulerian (bool): Booleano indicando se um grafo é euleriano ou não.
        """

        # Implementação encapsulada de acordo com a ED utilizada
        return self.__graph.is_eulerian()
    
    def count_edges(self):
        """Retorna a quantidade de arestas que incidem em cada vértice.
        
        Retorno
        -------
        - count_edges (dict): Dicionário contendo a
        quantidade de arestas de cada vértice.
        """

        # Implementação encapsulada de acordo com a ED utilizada
        return self.__graph.count_edges()

    def traverse(self, u: int):
        """Atravessa uma aresta (u,v) do grafo.
        
        Parâmetros
        ----------
        - u (int): Vértice de origem.

        Retorno
        -------
        - v (int): Vértice de destino.
        """

        # Implementação encapsulada de acordo com a ED utilizada
        return self.__graph.traverse(u)

    def get_eulerian_circuit(self, initial_v: int = 0):
        """Retorna um circuito euleriano para um dado grafo.
        
        Parâmetros
        ----------
        - initial_v (int): Vértice de partida do circuito.
        """

        # Inicializa uma cópia do grafo para ser usada no algoritmo
        self.set_graph() # Alterações serão feitas
        
        # Requisitos para encontrar um circuito euleriano
        if not self.is_connected():
            print("O grafo não é conectado, " \
                  "portanto não possui um circuito euleriano!")
        elif not self.is_eulerian():
            print("O grafo não possui todos os vértices com grau par, " \
                  "portanto não possui um circuito euleriano!")
        else:
            final_circuit = Stack() # Pilha contendo os vértices do circuito final
            current_circuit = Stack() # Pilha contendo os vértices do circuito intermediário
            
            # Dicionário contendo a quantidade de arestas de cada vértice
            count_remaining_edges = self.count_edges()
            
            current_v = initial_v
            current_circuit.stack_up(current_v)
            while not current_circuit.is_empty(): # Enquanto houver um circuito a ser explorado
                # Se o vértice atual possui aresta para ser explorada
                if count_remaining_edges[current_v] > 0:
                    current_circuit.stack_up(current_v) # Empilha o vértice atual
                    
                    # Busca o próximo vértice (atravessa uma aresta)
                    next_v = self.traverse(current_v)
                    
                    # Após atravessar a aresta, ela não pode mais ser considerada (Atravessa somente uma vez)
                    count_remaining_edges[current_v] -= 1 # Diminui a qtde de arestas restantes do vértice atual
                    if current_v != next_v: # Se a aresta é um laço não precisa diminuir duas vezes
                        count_remaining_edges[next_v] -= 1 # Diminui a qtde de arestas restantes do próximo vértice
                    
                    current_v = next_v # Atribui o próximo vértice como sendo o vértice atual
                else: # Se o vértice atual não possui mais arestas para serem exploradas
                    final_circuit.stack_up(current_v) # Empilha o vértice atual (Terminou um circuito)
                    current_v = current_circuit.unstack() # O vértice atual passa a ser o vértice anterior
                    # Busca um novo circuito a partir do vértice anterior
            
            # Exibe o circuito euleriano encontrado desempilhando os vértices do circuito final
            print("Circuito euleriano encontrado: ", end="")
            eulerian_circuit = ""
            while not final_circuit.is_empty():
                v = final_circuit.unstack()
                eulerian_circuit += "{} -> ".format(v)
            eulerian_circuit = eulerian_circuit[:-4]
            print(eulerian_circuit)
    
    def is_adjacency_list(self):
        """Retorna se o grafo é uma lista de adjacência.
        Método utilizado apenas para verificar a ED utilizada
        antes de fazer o algoritmo de verificação de grafos
        hamiltonianos.
        
        Retorno
        -------
        - is_adjacency_list (bool): Booleano indicando se o grafo é
        uma lista de adjacência ou não.
        """

        return self.__is_adjacency_list

    def get_powerset_of_v(self):
        """Retorna o conjunto potência dos vértices de um grafo.
        
        Retorno
        -------
        - result (list): Lista de tuplas contendo todas as combinações
        possíveis de vértices.
        """

        vertices = self.get_list_of_vertices()
        result = list()
        # Cria os conjuntos de vértices variando o tamanho destes conjuntos
        for size in range(len(vertices)+1): # 0,1,2,...,|V|
            result += list(combinations(vertices, size))

        return result

    def is_hamiltonian(self):
        """Retorna se um grafo é hamiltoniano ou não.
        
        Retorno
        -------
        - is_hamiltonian (bool): Booleano indicando se o grafo
        é hamiltoniano ou não.
        """

        # Inicializa uma cópia do grafo para ser usada no algoritmo
        self.set_graph() # Alterações serão feitas

        any_S = self.get_powerset_of_v()
        any_S.pop(0) # Remove o conjunto vazio
        any_S.pop() # Remove o conjunto que é igual a V

        for s in any_S: # Para qualquer subconjunto próprio não vazio S c V
            self.__graph.set_induced_graph(s) # Grafo induzido G-S
            # Busca em profundidade para encontrar o número de componentes do grafo induzido G-S
            num_components = self.depth_first_search_components() # w(G-S)
            if num_components > len(s): # Se w(G-S) <= |S|, continua verificando
                print("O grafo não é hamiltoniano!")
                return False
        
        print("O grafo pode ser hamiltoniano!")
        return True

