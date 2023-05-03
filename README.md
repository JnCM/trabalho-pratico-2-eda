# Trabalho Avaliativo 2 - EDA
Repositório contendo os códigos do trabalho avaliativo 2, da disciplina INF610 - Estrutura de dados e algoritmos.

## Execução dos códigos

Para executar a implementação, basta digitar o comando no terminal:
```bash
python main.py nome_do_arquivo.txt
```
Em que `nome_do_arquivo.txt` é o caminho do arquivo de entrada contendo a representação do grafo.

Na pasta `tests`, há o código para gerar as matrizes a partir de um arquivo contendo a lista de adjacência do grafo. Para executar, basta digitar no terminal:
```bash
python convert_adj_list.py nome_do_arquivo opcao
```
Repare que o nome do arquivo neste caso não precisa da extensão, pois ele espera receber o padrão `nome_do_arquivo`+`_list_adj.txt`, então deve-se garantir que o nome do arquivo possua este formato.

A `opcao` indica se for 1, irá gerar a representação de matriz de incidência e se a opção for omitida irá gerar a representação de matriz de adjacência.

O código fornecido para gerar grafos eulerianos na representação de lista de adjacência foi alterado, e para executa-lo basta digitar:
```bash
python create_eulerian_graph.py nome_do_arquivo nodos
```

Ou seja, o primeiro parâmetro é o nome do arquivo sem extensão, pois assim o código pode gerar o arquivo com o padrão de nome `nome_do_arquivo`+`_list_adj.txt` utilizado no código anterior, e o segundo parâmetro é a quantidade de nós do grafo a ser gerado.
