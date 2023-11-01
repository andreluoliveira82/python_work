
class Stack:
    """
    Esta classe tem cinco métodos.
    Modela uma pilha (stack) de um objeto qualquer
    """
    #--------------------------------------------------
    def __init__(self):
        """
        Inicializa os atributos da classe
        """
        # inicializa com uma lista vazia
        self.items = []
    #--------------------------------------------------
    def is_empty(self):
        """
        Retorna True se a pilha estiver vazia
        """
        return self.items == []
    #--------------------------------------------------
    def push(self, item):
        """
        adiciona um item na última posição (no topo) da pilha
        """
        self.items.append(item)
    #--------------------------------------------------
    def pop(self):
        """
        Remove e retorna o item do topo da pilha
        """
        return self.items.pop()
    #--------------------------------------------------
    def peek(self):
        """
        Retorna o item do topo da pilha, mas não o remove
        """
        last = len(self.items) -1
        return self.items[last]
    #--------------------------------------------------
    def size(self):
        """
        Retorna a quantidade (int) de elementos existentes na pilha
        """
        return len(self.items)
    
#-----------------------------------------------------------------------------
# definição da classe Queue (Fila - enˈkyo͞o)
class Queue():
    """
    Modelando uma estrutura de empilhamento (fila), onde uma lista de elementos são empilhados e só podem ser adicionados e/ou removidos em uma ordem específica, onde o primeiro elemento a entrar deve ser o primeiro a sair (FIFO - First In First Out)
    """
    #--------------------------------------------------
    def __init__(self):
        """ Inicializa os atributos da classe"""
        self.items = []
    #--------------------------------------------------
    def is_empty(self):
        """
        Retorna True se a pilha estiver vazia
        """
        return self.items == []
    #--------------------------------------------------
    def enqueue(self, item): # enfileirar
        """
        Enfileira o item adicionado, de tal forma que o primeiro a entrar seja o primeiro a sair quando o método 'dequeue' for chamado.
        """
        # o elemento atual (o último a entrar) está sendo adicionado na posição 0 da fila.
        # desta forma, ele será o último a sair quando for chamado o método 'dequeue' para extrair os elementos de self.items
        self.items.insert(0,item)
    #--------------------------------------------------
    def dequeue(self):
        """Remove o primeiro elemento que entrou na fila"""
        return self.items.pop()
    
     #--------------------------------------------------
    def peek(self):
        """
        Retorna o item do topo da fila, mas não o remove
        """
        last = len(self.items) -1
        return self.items[last]
    
    #--------------------------------------------------
    def size(self):
        """
        Retorna a quantidade (int) de elementos existentes na fila
        """
        return len(self.items)