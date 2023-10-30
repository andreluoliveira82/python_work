# André Oliveira
# 30/10/2023- 05h34
# Curso intensivo de Python
# cap. 10 - Arquivos e Exceções
# ----------------------------------------------------------------------------
# verificando se uma sequencia de data de aniversario estpa contido em PI

from pathlib import Path

file = Path("cap10_arquivos_excessoes\pi_digits.txt") # como o arquivo está salvo no mesmo diretorio que este programa, basta passar o nome do arquivo

# lendo o conteúdo do arquivo
# na sequencia remove caracteres extras ao final da saída
contents = file.read_text().rstrip()

# acessando cada linha do arquivo com o metodo splitlines()
# e na sequencia usamos um loop for para ler cada linha
lines = contents.splitlines()

pi_sting = " "

for line in lines:
    pi_sting += line.lstrip()

birthday = input("Infome sua data de aniversario no formato 'mmddaa' \n")

if birthday in pi_sting:
    print("sua data de aniversário aparece dentro da sequencia do numero PI:")
else:
    print("sua data de aniversário não aparece dentro da sequencia do numero PI:")