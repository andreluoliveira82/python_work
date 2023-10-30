# André Oliveira
# 30/10/2023 09h48

# Livro Curso intensivo de Python
# cap. 10 - Arquivos e exceções
# ----------------------------------------------------------------------------
# exercicio 10.5 armazenando varios nomes em um arquivo

import pathlib

# encontrando o arquivo
meu_arquivo = pathlib.Path("guest_book.txt")

# lista para armazenar os nomes digitados
nomes = []

print("\nPara sair do programa a qualque momento pressione a tecka q")

# coletando os nomes inseridos pelo usuario até que pressione 'q' para sair
while True:
    nome = input("Digite o nome:\n")

    if nome.lower() == "q":
        break

    nomes.append(nome.lower())

# montando a lista de nomes para posteriormente escrever tudo de uma vez no arquivo de texto
lista_nomes =""
for nome in nomes:
    lista_nomes += f"{nome.title()}\n"

try:
    # escrevendo os nomes no arquivo de texto
    meu_arquivo.write_text(lista_nomes,"utf-8")
except FileNotFoundError:
    print("\nNão foi possível localizar o arquivo")

else:
    print("Arquivo criado com sucesso!")