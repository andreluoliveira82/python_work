# André Oliveira
# 03/11/2023 14h

# Livro Curso intensivo de Python
# cap. 10 - Arquivos e exceções
# -----------------------------------------------------------------
# exercicio 10.11 Numeros favoritos com Json

from pathlib import Path
import json

# salvando uma entrada do usuario em um arquivo json
num_favorito = input("Digite seu numero favorito: ")
json_file = Path("database.json")

if num_favorito != "":
    num_favorito = json.dumps(num_favorito)
    json_file.write_text(num_favorito)

print("-----ARQUIVO SALVO COM SUCESSO-----\n")