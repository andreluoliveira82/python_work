
class Pilha:
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