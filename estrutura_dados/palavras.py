import re

# ---------------------------------------------------------------------------
# Esta função recebe uma palavra como parametro e verifica se é um palindromo, retornando True ou False

def is_palindromo(word):
    """Verifica se 'word' é um palindromo"""
    word = word.lower()

    inverse_word = word[::-1] # inverte a palavra

    # compara a palavra com a palavra invertida e retorna o resultado
    return   word == inverse_word

# ---------------------------------------------------------------------------

def is_anagram(word1, word2):
    """
    Organiza as duas palavras em ordem alfabética e as compara.
    se as palavras ordenadas forem iguais, o retorno será True
    """
    word1 = word1.lower()
    word2 = word2.lower()

    return sorted(word1) == sorted(word2)

# ---------------------------------------------------------------------------

# Função para remover caracteres especiais
def remover_caracteres_especiais(texto):
    # Lista de caracteres especiais a serem removidos
    caracteres_especiais = r'[!@#$%^&*()_+{}\'\'‘’“”\[\]:;"<>,.?\\|/`~=-]'

    # Usando uma expressão regular para remover apenas caracteres especiais
    texto_limpo = re.sub(caracteres_especiais, '', texto)

    return texto_limpo
# ---------------------------------------------------------------------------

# Função que abre o arquivo txt
def abrir_arquivo_txt(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()

        # tratando o texto antes de substituir os caracteres especiais.
        texto = texto.replace("-"," ")# substituindo '-' por ' ' (traço por espaço)
        texto = texto.replace("."," ") # substituindo '.' por ' ' (ponto por espaço)
        texto = texto.strip() # removendo espaços extras.
    
    return texto

# -------------------------------------------------------------------------
def lista_palavras_sem_repeticao(texto):
    """ Recebe um texto qualquer e, após tratá-lo, retorna uma lista de palavras únicas ordenada alfabeticamente"""

    # separando as palavras do texto em uma:
    # aqui temos todos os caracteres do texto original
    palavras = texto.split()

    # Usando uma lista de compreensão para obter palavras com mais de três caracteres e que não são digitos (numeros) e únicas (que não se repetem)
    palavras = sorted(
                [palavra for palavra in palavras 
                if len(palavra) > 3
                and not palavra.isdigit()
                and palavras.count(palavra) == 1]
                )
    return palavras

# --------------------------------------------------------------------------

# obtém um texto por meio da função abrir_arquivo_txt
texto = abrir_arquivo_txt("noticias_google.txt")

# Remove os caracteres especiais do texto
texto_limpo = remover_caracteres_especiais(texto)

# Exibe o texto sem os caracteres especiais
# print(texto_limpo.upper())
# print(texto_limpo)

lista_palavras = lista_palavras_sem_repeticao(texto_limpo)

print("--------------------------------------------------")
print(f"Há {len(lista_palavras)} palavras que não se repetem na lista\n")

# # exibindo cada palavra na lista de palavras
# for palavra in sorted(palavras):
#     print(palavra.upper())

# ======================================================================
# muito louco esta lógica que fiz sozinho.
# compara cada palavra da lista de palavras com a proxima palavra
# eu fiz isso pq quero brincar com a função 'anagram' que verifica se duas palavras são anagramas. Daí pra deixar tudo mais interessante, fiz esta lógica que pega um arquivo de texto qualquer e extrai uma lista de palavras únicas e compara cada palavra com a a outra passando as duas para a função anagram.


j = 1
anagrams_count = 0
palindroms_count = 0
anagramas = []
palindromos = []

while lista_palavras:
    
    try:
        palavra1 = lista_palavras[0]

        for palavra in lista_palavras:
            try:
                palavra2 = lista_palavras[j]
            except:
                pass
            else:
                # # exibe as palvaras comparadas lado a lado
                # print(f"{palavra1} - {palavra2}")
                
                # verifica se as palavras comparadas são anagramas
                if palavra1.lower() != palavra2.lower() and is_anagram(palavra1, palavra2):
                    # print(f"{palavra1} - {palavra2}")
                    anagramas.append(str(palavra1) + "-" + str(palavra2))
                    anagrams_count += 1
                j += 1

        # print(f"------{i}---------")
        # verificar se a palavra1 é um palindromo
        
        if is_palindromo(palavra1):
            palindromos.append(palavra1)
            palindroms_count =+ 1
        lista_palavras.remove(palavra1)

        j = 1

    except:
        #pass
        print(f"Erro: ")
    else:
        continue

print ("\n--------------------------------------------------------")

if anagrams_count == 0:
    print("\nNenhuma anagrama foi encontrado nas palavras deste texto")
else:
    print(f"foram localizadas {anagrams_count} anagramas:\n{anagramas}")

if palindroms_count > 0:
    print(f"\nForam localizadas {palindroms_count} palindromos:\n{palindromos}")
else:
    print("\nNenhum palindromo foi encontrado nas palavras deste texto")

print("\n-----Fim do Programa-----\n")
