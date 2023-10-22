# 
# 
# 
# 
import random as rm


palavras_aleatorias = [
    'abacate', 'almofada', 'borboleta', 'canivete', 'dinossauro', 'eletricidade', 'feriado', 'girassol', 'hipopótamo', 'independência',
    'jacaré', 'kiwi', 'lamparina', 'macarrão', 'nariz', 'ovelha', 'piano', 'quadro', 'raquete', 'sanduíche',
    'tartaruga', 'ursinho', 'violino', 'xícara', 'zoológico', 'agua', 'bolo', 'carrossel', 'deserto', 'espelho',
    'foguete', 'garfo', 'helicóptero', 'iguana', 'jardim', 'leão', 'mesa', 'navio', 'ouro', 'palmeira', 'queijo',
    'raio', 'sabonete', 'tênis', 'universo', 'vassoura', 'waffle', 'xadrez', 'yogurte', 'zeppelin'
]

def sortear_palavra():
    """com base em uma lista de palavras, escolhe aleatoreamente uma palavra e a devolve como resultado desta função"""
    palavra_sorteada = palavras_aleatorias[rm.randint(0,len(palavras_aleatorias))]
    return palavra_sorteada

# chama a função hangman passando como parametro uma palavra sorteada aleatoreamente pela função sorter paalvra
palavra = sortear_palavra()


def hangman(word):
    wrong = 0

    stages = ["",
              "_____________     ",
              "|           ¥     ",
              "|           ‖     ",
              "|          💀     ",
              "|          /|\    ",
              "|          | |    ",
              "|                 ",
              "|                 ",
              "|                 ",
    ]

    rletters = list(word)

    board = ["_"] * len(word)

    inserted_letters = []
    
    win = False
    print ("\nBem vindo ao Jogo da Forca")
    print(f"\nA palavra tem {len(word)} letras.")

    while wrong < len(stages) -1:
        print("\n")

        msg = "Insira uma letra: "
        char = input(msg)[0] #pega apenas o 1 caractere mesmo se for inserido varios
        inserted_letters.append(char.upper())      

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char.upper()
            rletters[cind] = "$"

        else:
            wrong += 1
            
            e = wrong + 1
            print("\n".join(stages[0:e]))

            print(f"\nRestam {len(stages) - wrong-1} chances")

        # mostra as letras que já foram inseridas
        print(f"\n{sorted(inserted_letters)}\n")

        # mostra a composição da palavra até o momento
        print ((" ".join(board)))

        if "_" not in board:
            print("Você venceu!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong]))

        print(f"Você perdeu!\nA palavra era {word.upper()}.\n") 



jogar = hangman(palavra)
