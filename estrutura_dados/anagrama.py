# André Oliveira
# 02/11/2023
# Um anagrama ocorre quando as letras de uma palavra são reorganizadas para formar outra palavra com as mesmas letras.
# para verificar se duas palavras são anagramas, podemos reorganizar as letras das duas palavras em ordem alfabética e comparar se são iguais

# 
def anagram(word1, word2):
    """
    Organiza as duas palavras em ordem alfabética e as compara.
    se as palavras ordenadas forem iguais, o retorno será 
    """
    word1 = word1.lower()
    word2 = word2.lower()

    return sorted(word1) == sorted(word2)

print(anagram("cinema", "menica"))