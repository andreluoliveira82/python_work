import re

class Palavra:
    """
    Diversos métodos para verificação de textos
    """ #---------------------------------------------------------------------------
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
    def abrir_arquivo_txt(nome_arquivo:str):
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
    # -------------------------------------------------------------------------
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
