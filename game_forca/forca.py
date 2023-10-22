# 
# 
# 
# 
def hangman(word):
    wrong = 0

    stages = ["",
              "_____________     ",
              "|           |     ",
              "|          🪢     ",
              "|          😲     ",
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
            
            print(f"\nRestam {len(stages) - wrong} chances")

        # mostra as letras que já foram inseridas
        print(f"{sorted(inserted_letters)}\n")

        # mostra a composição da palavra até o momento
        print ((" ".join(board)))

        e = wrong + 1
        print("\n".join(stages[0:e]))

        

        if "_" not in board:
            print("Você venceu!")
            print(" ".join(board.upper()))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong]))

        print(f"Você perdeu!\nA palavra era {word.upper()}.\n") 


jogar = hangman("vigarista")
