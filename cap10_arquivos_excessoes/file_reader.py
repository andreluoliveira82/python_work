# André Oliveira
# 30/10/2023- 05h34
# Curso intensivo de Python
# cap. 10 - Arquivos e Exceções
# ----------------------------------------------------------------------------
# Lendo o conteudo de um arquivo

from pathlib import Path

file = Path("cap10_arquivos_excessoes\pi_digits.txt") # como o arquivo está salvo no mesmo diretorio que este programa, basta passar o nome do arquivo

# lendo o conteúdo do arquivo
# na sequencia remove caracteres extras ao final da saída
contents = file.read_text().rstrip()

# acessando cada linha do arquivo com o metodo splitlines()
# e na sequencia usamos um loop for para ler cada linha
lines = contents.splitlines()

pi_string = " "

for line in lines:
    pi_string += line.lstrip()


print(pi_string)
print(len(pi_string))