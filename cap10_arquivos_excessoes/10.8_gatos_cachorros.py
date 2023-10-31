# André Oliveira
# 31/10/2023 20h55

# Livro Curso intensivo de Python
# cap. 10 - Arquivos e exceções
# ----------------------------------------------------------------------------
# exercicio 10.8 Gatos e cachorros

from pathlib import Path

cat_names =["nice","luna","bichano"]
dog_names = ["pit","brad","biden"]

cats_file = Path("cats.txt")
dogs_file = Path("dogs.txt")

# montando a lista de nomes dos gatos e cachorros para depois escrever tudo em um arquivo
lista_cats = ""
lista_dogs = ""

# for cat_name in cat_names:
#     lista_cats += (f"{cat_name.title()}\n")

# for dog_name in dog_names:
#     lista_dogs += (f"{dog_name.title()}\n")

# # gravar os nomes em seus respectivos arquivos
# try:
#     cats_file.write_text(lista_cats,"utf-8")
#     dogs_file.write_text(lista_dogs,"utf-8")
# except FileNotFoundError:

#     print("Um ou mais arquivo(s) não foi localizado")
# else:
#     print("Arquivos criados com sucesso")

# lendo os arquivos criados. lançando uma exceção de proposito:

try:
    lista_cats = cats_file.read_text("utf-8")
    lista_dogs = dogs_file.read_text("utf-8")

    print(f"\nLista de Gatos:\n{lista_cats}")
    print(f"\nLista de Cachorros:\n{lista_dogs}")
except:

    print("Um ou mais arquivo(s) não foi localizado")
else:
    print("Procedimento concluído com sucesso")