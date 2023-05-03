class Stack:
    """Classe que abstrai a implementação de uma pilha
    utilizando uma lista contígua.
    """

    def __init__(self):
        # Inicializa a lista vazia que será a pilha
        self.__stack = []

    def is_empty(self):
        # Retorna se o tamanho da lista é igual a zero
        return len(self.__stack) == 0

    def stack_up(self, value):
        # Empilha no final da lista o elemento do topo
        self.__stack.append(value)
    
    def unstack(self):
        # Desempilha no final da lista o elemento do topo
        value = self.__stack[-1]
        self.__stack.pop()
        return value # Retorna o elemento desempilhado
