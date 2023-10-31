# criando o popular jogo de cartas War (Guerra).

# no jogo War, cada jogador retira uma carta do baralho e o que tiver a carta mais alta ganha.
# Criaremos classes para representar uma carta, um baralho, um jogador, e o proprio jogo.

class Card:
    """
    Esta é a classe que modela as cartas do jogo.
    """ 
    # -----------------------------------------
    # representa todos os naipes que uma carta pode ter: (espadas, copas, ouro, paus)
    suits = ("espadas",
             "copas",
             "ouro",
             "paus")
    
    # representam os diferentes valores numéricos de uma carta (2-10, Valete, Dama, Rei e Ás)
    # -----------------------------------------
    values = (None, None, "2","3",
              "4","5","6","7",
              "8","9","10",
              "Valete","Dama",
              "Rei","Ás",) 
    # os dois primeiros indices da lista values são None apenas para que os demais indices conincidam com os valores que os representa (assim o indice 2 representa o valor 2 e assim por diante)

    # -----------------------------------------

    def __init__(self, v,s):
        """suit + value are ints"""
        self.value = v
        self.suit = s
    # -----------------------------------------

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    # -----------------------------------------

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
    # -----------------------------------------

    def __repr__(self):
        """
        este metodo mágico Usa as variáveis de instancia 'value' e 'suit' para procurar o valor e o naipe da carta nas respectivas listas (Values e Suits).
        Retorna a carta que um objeto Card representa
        """
        v = self.values[self.value] + " de " + self.suits[self.suit]
        
        return v
    
#-----------------------------------------------------------------------------
# criando a classe para modelar o baralho
from random import shuffle

class Deck:
    """
    Modela um baralho de cartas.
    """
    # -----------------------------------------

    def __init__(self):
        """
        cria as 52 cartas do baralho sendo uma carta de cada valor para cada nipe (sabemos que um baralho possui 4 nipes e cada nipe 13 valores (de 2 até o Ás))
        """
        self.cards = []

        # cria as 52 cartas do baralho sendo uma carta de cada valor para cada nipe (sabemos que um baralho possui 4 nipes e cada nipe 13 valores (de 2 até o Ás))
        for i in range(2,15):

            for j in range(4):
                self.cards.append(Card(i,j))

        # metodo da classe ramdom para embaralhar os valores em ordem aleatória
        shuffle(self.cards)
    # -----------------------------------------

    def rm_card(self):
        """
        Remove a carta de cima (pop) do baralho e a retorna ou retorna None se ela estiver vazia.
        """
        if len(self.cards) == 0:
            return
        
        return self.cards.pop()
    
#-----------------------------------------------------------------------------
# criando a classe para modelar o jogador

class Player:
    """
    Modela um jogador para o jogo de baralho.
    as variáveis de instancia:
    wins: registra quantas rodadas um jogador venceu.
    card: representa a carta que um jogador tem atualmente.
    name: registra o nome de um jogador
    """
    def __init__(self, name):
        self.wins = 0
        self.cards = None
        self.name = name

#-----------------------------------------------------------------------------
# finalmente vamos criar a classe para modelar o jogo em si

class Game:
    """
    ...
    """
    # -----------------------------------------

    def __init__(self):
        """
        ...
        """
        name1 = input("Nome do jogador 1: ")
        name2 = input("Nome do jogador 1: ")

        # instancia um Deck e os Players
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    # -----------------------------------------

    def wins(self, winner):
        """
        ...
        """
        w = "\n{} venceu nesta rodada."
        w = w.format(winner)
        print(w)

    # -----------------------------------------

    def draw(self, p1n, p1c, p2n, p2c):
        """
        ...
        """
        d = "{} tirou {} {} tirou {}"
        d = d.format(p1n,
                     p1c,
                     p2n,
                     p2c)
        
        print(d)
    # -----------------------------------------

    def play_game(self):
        """
        ...
        """
        cards = self.deck.cards
        print("Iniciando War!")

        while len(cards) >=2:
            m = "\nq para sair. Qualquer tecla para jogar: "
            response = input(m)

            if response.lower() == 'q':
                break
            
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name

            self.draw(p1n, p1c, p2n, p2c)

            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)

        print("A Gerra Acabou. {} Venceu!".format(win))
    # -----------------------------------------

    def winner(self, p1, p2):
        """
        ...
        """
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        
        return "Empate!"