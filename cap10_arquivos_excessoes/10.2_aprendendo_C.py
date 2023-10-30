# André Oliveira
# 30/10/2023 09h48

# Livro Curso intensivo de Python
# cap. 10 - Arquivos e exceções
# ----------------------------------------------------------------------------
# exercicio 10.2 Aprendendo C (substituindo a palavra Python por C)

import pathlib

# encontrando o arquivo
meu_arquivo = pathlib.Path("aprendendo_python.txt")

# lendo o conteúdo do arquivo
conteudo = meu_arquivo.read_text(encoding="utf-8")

# 2. exibindo o conteudo na tela linha por linha usando a função splitlines()
print("\n-----Exibindo o conteúdo linha por linha-----\n")
lines = conteudo.splitlines()
for line in lines:

    # em cada linha, substitui a palavra Python por C
    # e exibe na tela o texto ajustado
    line = line.replace("Python","C")
    print(line.strip())