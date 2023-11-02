import re

# Função para remover caracteres especiais
def remover_caracteres_especiais(texto):
    # Lista de caracteres especiais a serem removidos
    caracteres_especiais = r'[!@#$%^&*()_+{}\'\'‘’“”\[\]:;"<>,.?\\|/`~=-]'

    # Usando uma expressão regular para remover apenas caracteres especiais
    texto_limpo = re.sub(caracteres_especiais, '', texto)

    return texto_limpo

# Abre o arquivo para leitura
with open('news.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

    # tratando o texto antes de substituir os caracteres especiais.
    texto = texto.replace("-"," ")# substituindo '-' por ' ' (traço por espaço)
    texto = texto.replace("."," ") # substituindo '.' por ' ' (ponto por espaço)
    texto = texto.strip() # removendo espaços extras.

# Remove os caracteres especiais do texto
texto_limpo = remover_caracteres_especiais(texto)

# Exibe o texto sem os caracteres especiais
# print(texto_limpo.upper())
print(len(texto_limpo))

# obtendo uma lista de palavras do texto:
palavras = texto_limpo.split()

# Usando uma lista de compreensão para obter palavras com mais de três caracteres
palavras = [palavra for palavra in palavras if len(palavra) > 3]

# # exibindo cada palavra na lista das primeiras 1000 palavras
# for palavra in palavras[:500]:
    
#     print(palavra.upper())

def anagram(word1, word2):
    """
    Organiza as duas palavras em ordem alfabética e as compara.
    se as palavras ordenadas forem iguais, o retorno será True
    """
    word1 = word1.lower()
    word2 = word2.lower()

    return sorted(word1) == sorted(word2)

i = 0
while palavras:

    try:
        palavra1 = palavras[i]
    except:
        pass
    else:
        j= i + 1
      
        for palavra in palavras:
            try:
                palavra2 = palavras[j]
            except:
                pass
            else:
                print(f"{palavra1} - {palavra2} ")
                j += 1

        palavras.remove(palavra1)
        i+=1
