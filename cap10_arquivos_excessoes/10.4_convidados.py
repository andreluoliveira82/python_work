# André Oliveira
# 30/10/2023 09h48

# Livro Curso intensivo de Python
# cap. 10 - Arquivos e exceções
# ----------------------------------------------------------------------------
# exercicio 10.4 recebendo um nome pelo input do ususario e armazenando este nome em um arquivo de texto chamdo guest.txt

import pathlib

# encontrando o arquivo
meu_arquivo = pathlib.Path("guest.txt")

# lendo o conteúdo do arquivo
conteudo = input("Digite seu nome completo:\n").lower()

# verifica se o conteudo digitado tem ao menos tres caracteres
if  len(conteudo) >=3:
    meu_arquivo.write_text(conteudo,"utf-8")

    print("conteúdo inserido com sucesso.")

else:
    print("Digite um nome válido:")
    conteudo = input("Digite seu nome completo:\n")