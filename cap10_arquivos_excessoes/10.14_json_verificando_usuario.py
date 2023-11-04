# André Oliveira
# 03/11/2023 14h

# Livro Curso intensivo de Python
# cap. 10 - Arquivos e exceções
# -----------------------------------------------------------------
# exercicio 10.14 salvando um dicionario com informações do usuario

# anotaçoes para mim mesmo:
# refatorar este codigo,criar uma classe, definindo os metodos:
# validar_dados (se o usuario digitou informações corretas no input)
# cumprimentar_usuario
# etc

from pathlib import Path
import json
#------------------------------------------------------------------
def valida_user_info(
        username:str,
        idade:str, 
        senha:str):
    valida_user_info = False

    # verifica se digitou um username válido com mais de 3 caracteres
    if username.isnumeric() or len(username) <= 3:
        print("\nNome de usuario inválido. o username precisa ser alfanumérico e deve ter mais de 03 letras. Verifique e tente novamente.")
    
    elif int(idade) < 16:
        print("Você não tem idade suficiente para se cadastrar.")
    elif len(senha) < 6:
        print("Senha inválida. A senha deve ter mais de 06 caracteres.")
    
    else:
        valida_user_info = True

    return valida_user_info

#------------------------------------------------------------------
def get_new_user(users_file):
    """
    Cadastra um novo usuario e salvar em um jsonz|'
    """
    username = input("\nDigite seu username: ")
    idade = input("Digite sua idade: ")
    senha = input("Digite sua senha: ")

    if not valida_user_info(username, idade, senha):
        print("Os dados digitados (username, idade ou senha) podem estar inválidos. Verifique e tente novamente.")
    else:
        dic_user["username"] = username
        dic_user["idade"] = idade
        dic_user["senha"] = senha

        conteudo = json.dumps(dic_user)
        users_file.write_text(conteudo)
      
        return username
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

    # verificando se o usuario atual é o último usuario salvo
    if input(f"seu username é {username}?\nDigite 'y' para sim ou 'n' para não ").lower() == "y":

        print(f"\nBem vindo de volta, {username}!\nAqui estão seus dados:\n{user_info}")
    else:
        
        new_user = get_new_user(users_file)

        if new_user is not None:
            print(f"Informações salvas com sucesso.\nLembraremos seus dados quando voltar, {new_user}!")
        else:
            new_user = get_new_user(users_file)

print("\n-----FIM-----\n")

