# André Oliveira
# 14/10/2023- 10h30
# Curso intensivo de Python
# cap. 8 - Funções
# ----------------------------------------------------------------------------
# Exercicio 8.7 - Função para retornar um diionario com nome do artista e titulo do album

#=============================================================================

def make_album(artist_name, album_name, musics=None):

    """armazena o nome do artista e do album em um dicionario"""

    # cria um dicionario chamado album
    album = {'artist': artist_name.lower(), 'album':album_name.lower()}

    # se o argumento musics for preenchido, adiciona no dicionario
    if musics:
        album['musics'] = musics

    return album # retorna o dicionario

#=============================================================================

# exibindo o resultado da função cujo resultado foi armazenado em um dicionario

#1
album = make_album("Rick & Renner", "saudade")
print(f"\nO album da semana é...\n {album}")

#2
album2 = make_album("Mariane",'o amor bateu na porta')
print(f"\nO album da semana 2 é:\n {album2}")

#3 - adicionando o album com todos os parametros
album3 = make_album("LILICA", "BOM DIA",21)
print(f"\nO album da semana 3 é: \n{album3}")