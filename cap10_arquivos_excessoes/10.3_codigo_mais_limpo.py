# André Oliveira
# 30/10/2023 09h48

# Livro Curso intensivo de Python
# cap. 10 - Arquivos e exceções
# ----------------------------------------------------------------------------
# exercicio 10.3 Codigo mais limpo (utlizando diretamente o metodo splictlines() sem passar para dentro de outra variavel)

import pathlib

# encontrando o arquivo
meu_arquivo = pathlib.Path("aprendendo_python.txt")

# lendo o conteúdo do arquivo
conteudo = meu_arquivo.read_text(encoding="utf-8")

print("\n-----Exibindo o conteúdo linha por linha-----\n")

for line in conteudo.splitlines():

    # em cada linha, substitui a palavra Python por C
    # e exibe na tela o texto ajustado
    line = line.replace("Python","C")
    print(line.strip())