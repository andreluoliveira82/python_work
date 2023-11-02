# André Oliveira
# 02/11/2023
# Um palindromo é uma palavra que tem a mesma grafia da esquerda para a direita e vice-versa

# Esta função recebe uma palavra como parametro e verifica se é um palindromo, retornando True ou False

def is_palindromo(word):
    """Verifica se 'word' é um palindromo"""
    word = word.lower()

    inverse_word = word[::-1] # inverte a palavra

    # compara a palavra com a palavra invertida e retorna o resultado
    return   word == inverse_word

print(is_palindromo("game"))