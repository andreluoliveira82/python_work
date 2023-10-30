
# criando uma classe
class Dog: # nome da classe (Inicial em maisuscula)
    """simples tentativa de modelar um cachorro"""

    def __init__(self, name, age):
        """inicializa os atributos e nome e idade"""
        self.name = name
        self.age = age

    def sentar(self):
        """simula um cachorro sentado em resposta a um comando"""
        print(f"{self.name.title()} está sentando.")


    def rolar(self):
        """simula o cachorro rolando em resposta a um comando"""
        print(f"{self.name.title()} está rolando.")