# André Oliveira
# 16/10/2023 - 05h20
# Curso intensivo de Python
# cap. 8 - Funções

# Inicializa uma lista para armazenar álbuns
lista_albums = []

def make_album(artist_name, album_name, musics=None):
    """Retorna um dicionário com nome do artista e título do álbum."""
    album = {"name": artist_name, "album": album_name}
    if musics:
        album["musics"] = musics
    return album

# Início da pesquisa para armazenar as respostas em uma lista:

pesquisa_ativa = True

while pesquisa_ativa:
    resposta = input("Insira 'q' a qualquer momento para encerrar sua participação\n")

    if resposta.lower() == 'q':
        break

    artista = input("\nInforme o nome do seu cantor ou banda favorita: ")
    album = input("Informe o nome do álbum favorito: ")
    qtd_musicas = input("Se souber, informe a quantidade de músicas no álbum: ")

    album_info = make_album(artista, album, qtd_musicas)
    lista_albums.append(album_info)

# Exibe o resultado das pesquisas armazenadas na lista:

print("\nResultados das pesquisas:\n")

for album in lista_albums:
    print(f"Artista: {album['name']}\nÁlbum: {album['album']}")
    if 'musics' in album:
        print(f"Músicas: {album['musics']}")
    print()

print("\n=================================================================\n")
