# André Oliveira
# 16/10/2023- 05h20
# Curso intensivo de Python
# cap. 8 - Funções
# ----------------------------------------------------------------------------
# Exercicio 8.8 - Função para retornar um dicionario com nome do artista e titulo do album incluidos por meio de inputs do usuario em um loop while:

# definição da lista para armazenar todos os albuns
lista_albums = []

# Definição da função que preencherá o dicionário:
def make_album(artist_name, album_name, musics=None):
    """Função para retornar um dicionario com nome do artista e titulo do album incluidos por meio de inputs do usuario em um loop while:"""

    # armazena tudo em um dicionario
    album = {"name" : artist_name.lower(), "album": album_name.lower()}

    if musics:
        album["musics"] = musics

    return album

#===============================================================================
# Inicio da pesquisa para armazenar as respostas em um dicionário:

pesquisa_ativa = True

while pesquisa_ativa:
   
    resposta = input("Insira 'q' a qualquer momento para encerrar sua participação\n")

    if resposta.lower() == 'q':
        break

    artista = input("\nInforme o nome do seu cantor ou banda favorita: ")
    album = input("\nInforme o nome do album favorito: ")
    qtd_musicas = input("\nSe souber informe a quantidade de musicas no album: ")

    albun_info = make_album(artista,album,qtd_musicas)
    lista_albums.append(albun_info)

    resposta = input("Gostaria de cotinuar respondendo? digiste s [sim] ou n [não]")

# Exibe o resultado das pesquisas armazenado no dicionario:

print(f"\n Resultado da pesquisa:\n")

for album in lista_albums:
    print(f"Artista: {album['name']}\nÁlbum: {album['album']}\nMúsicas: {album['musics']}")
    #if 'musics' in album:
        #print(f"Músicas: {album['musics']}")
    print()

print("\n=================================================================\n")