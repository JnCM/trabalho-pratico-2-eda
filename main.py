import sys
from DataStructures.Graph import Graph

if __name__ == "__main__":
    filename = sys.argv[1] # Nome do arquivo
    graph = Graph(filename) # Inicializa o grafo
    graph.get_eulerian_circuit() # Exibe um circuito euleriano, caso exista
    if graph.is_adjacency_list(): # Implementação apenas para a lista de adjacência
        graph.is_hamiltonian() # Verifica a condição necessária para grafos hamiltonianos
