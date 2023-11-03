
import re
import random as rm

from unidecode import unidecode

def remove_acentos(texto):
    # Usa a função unidecode para remover acentos
    texto_sem_acentos = unidecode(texto)
    return texto_sem_acentos

# Função para remover caracteres especiais
def remover_caracteres_especiais(texto):
    # Lista de caracteres especiais a serem removidos
    caracteres_especiais = r'[!@#$%^&*()_+{}\'\'‘’“”\[\]:;"<>,.?\\|/`~=-]'

    # Usando uma expressão regular para remover apenas caracteres especiais
    texto_limpo = re.sub(caracteres_especiais, '', texto)

    return texto_limpo
# ---------------------------------------------------------------------------

def count_characters(palavra):
    """
    Percorre cada caractere de uma string e retorna quantas vezes cada caractere ocorre
    """
    count_dict = {}

    for c in palavra:
        if c in count_dict:
            count_dict[c] += 1

        else:
            count_dict[c] = 1

    print(count_dict)
    return count_dict

# ---------------------------------------------------------------------------

# Abre o arquivo para leitura
with open('noticias_google.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

    # tratando o texto antes de substituir os caracteres especiais.
    texto = texto.replace("-"," ")# substituindo '-' por ' ' (traço por espaço)
    texto = texto.replace("."," ") # substituindo '.' por ' ' (ponto por espaço)
    texto = texto.strip() # removendo espaços extras.

# Remove os caracteres especiais do texto
texto_limpo = remover_caracteres_especiais(texto)

# Exibe o texto sem os caracteres especiais
# print(texto_limpo.upper())
# print(texto_limpo)

# obtendo uma lista de palavras do texto:
palavras_aleatorias = texto_limpo.split()

def sortear_palavra():
    """com base em uma lista de palavras, escolhe aleatoreamente uma palavra e a devolve como resultado desta função"""
    palavra_sorteada = palavras_aleatorias[rm.randint(0,len(palavras_aleatorias))]
    return palavra_sorteada

# chama a função hangman passando como parametro uma palavra sorteada aleatoreamente pela função sorter paalvra
palavra = remove_acentos(sortear_palavra())


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
