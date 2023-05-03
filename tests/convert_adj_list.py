import sys

def parse_graph(filename: str="graph_parsed", option: int=0):
    file = open(filename + "_lista_adj.txt", "r")
    lines_of_file = file.readlines()
    file.close()

    if option == 1: # Converte para matriz de incidência
        edges = []
        u = 0
        for line in lines_of_file:
            adj_vertices = line.replace("\n", "").split(",")
            # Converte os valores da matriz para inteiros
            final_vertices = []
            for v in adj_vertices:
                if v != '':
                    final_vertices.append(int(v))
            for v in final_vertices:
                if (v,u) not in edges: # Não repete arestas
                    edges.append((u,v)) # Armazena cada aresta do grafo
            u += 1
        
        # |V| x |A|
        graph = [[0 for e in range(len(edges))] for v in range(len(lines_of_file))]
        for e in range(len(edges)):
            u,v = edges[e]
            graph[u][e] += 1
            graph[v][e] += 1

    else: # Converte para matriz de adjacência
        # |V| x |V|
        graph = [[0 for v in range(len(lines_of_file))] for v in range(len(lines_of_file))]
        
        u = 0
        for line in lines_of_file:
            adj_vertices = line.replace("\n", "").split(",")
            # Converte os valores da matriz para inteiros
            final_vertices = []
            for v in adj_vertices:
                if v != '':
                    final_vertices.append(int(v))
            for v in final_vertices:
                graph[u][v] += 1
            u += 1
    
    ext = "_matriz_incid.txt" if option == 1 else "_matriz_adj.txt"
    output = open(filename + ext, "w")
    for u in range(len(graph)):
        for v in range(len(graph[u])):
            if v == len(graph[u]) - 1:
                output.write("{}".format(graph[u][v]))
            else:
                output.write("{} ".format(graph[u][v]))
        output.write("\n")
    output.close()
            

if __name__ == "__main__":
    filename = sys.argv[1]
    try:
        option = int(sys.argv[2])
    except:
        option = None
    
    parse_graph(filename, option)