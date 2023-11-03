# André Oliveira
# 03/11/2023 14h

# Livro Curso intensivo de Python
# cap. 10 - Arquivos e exceções
# -----------------------------------------------------------------
# exercicio 10.13 salvando um dicionario com informações do usuario

from pathlib import Path
import json

#------------------------------------------------------------------
# lendo um arquivo json e mostrando o resultado na tela

users_file = Path("users.json")

username = ""
idade = ""
senha = ""

dic_user = {}

if users_file.exists():
    
    conteudo = users_file.read_text()
    user_info = json.loads(conteudo)
    username = user_info["username"]

    print(f"\nBem vindo de volta, {username}!\nAqui estão seus dados:\n{user_info}")
# se o arquivo não existe
else:
    username = input("\nDigite seu username: ")
    idade = input("Digite sua idade: ")
    senha = input("Digite sua senha: ")

    # verifica se digitou um username válido com mais de 3 caracteres
    if not username.isnumeric or len(username) > 3\
          and int(idade) > 16\
          and len(senha) >= 6:
        
        dic_user["username"] = username
        dic_user["idade"] = idade
        dic_user["senha"] = senha

        conteudo = json.dumps(dic_user)
        users_file.write_text(conteudo)

        print(f"Lembraremos seus dados quando voltar, {username}!")
    else:
        print("\nDigite um username não numérico e com mais de 03 letras.")

print("\n-----FIM-----\n")

