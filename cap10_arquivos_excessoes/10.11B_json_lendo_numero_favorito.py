# André Oliveira
# 03/11/2023 14h

# Livro Curso intensivo de Python
# cap. 10 - Arquivos e exceções
# -----------------------------------------------------------------
# exercicio 10.11 Numeros favoritos com Json

from pathlib import Path
import json

#------------------------------------------------------------------
# lendo um arquivo json e mostrando o resultado na tela

json_file = Path("database.json")
conteudo = json_file.read_text() # como o arquivo de dados é somente um txt podemos lê-lo com o metodo read_text

num_favorito = json.loads(conteudo)

print(f"Eu sei o seu número favorito. É... \n {num_favorito}.")

print("-----FIM-----\n")