# André Oliveira
# 30/10/2023 09h48

# Livro Curso intensivo de Python
# cap. 10 - Arquivos e exceções
# ----------------------------------------------------------------------------
# exercicio 10.1 Aprendendo Python

import pathlib

# encontrando o arquivo
meu_arquivo = pathlib.Path("aprendendo_python.txt")

# lendo o conteúdo do arquivo
conteudo = meu_arquivo.read_text(encoding="utf-8") # leia o texto tratando os caracteres para o portugues corretamente.

# 1. exibindo o conteudo na tela e uma única vez
print(conteudo)


# 2. exibindo o conteudo na tela linha por linha usando a função splitlines()
print("\n-----Exibindo o conteúdo linha por linha-----\n")
lines = conteudo.splitlines()
for line in lines:
    print(line.strip())