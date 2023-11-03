# André Oliveira
# 03/11/2023 14h

# Livro Curso intensivo de Python
# cap. 10 - Arquivos e exceções
# -----------------------------------------------------------------
# exercicio 10.12 Relebrando numeros favoritos com Json

from pathlib import Path
import json

#------------------------------------------------------------------
# lendo um arquivo json e mostrando o resultado na tela

users_file = Path("users.json")

if users_file.exists():

    conteudo = users_file.read_text()
    username = json.loads(conteudo)

    print(f"Bem vindo de volta, {username}!")
# se o arquivo não existe
else:
    username = input("Digite seu nome de usuario para salvar:\n ")

    # verifica se digitou um username válido com mais de 3 caracteres
    if not username.isnumeric or len(username) > 3:
        conteudo = json.dumps(username)
        users_file.write_text(conteudo)

        print(f"Lembraremos seu nome quando voltar, {username}!")
    else:
        print("\nDigite um username não numérico e com mais de 03 letras.")

print("-----FIM-----\n")

