# André Oliveira
# 14/10/2023- 0609h43h52
# Curso intensivo de Python
# cap. 7 - Loops While
# ----------------------------------------------------------------------
# preenchendo dicionario com uma pesquisa por meio do input

responses = {}

print(f"\nPor favor preencha nossa pesquisa:\n")

pesquisa_ativa = True

# enquanto o flag estiver true
while pesquisa_ativa:

    name = input(f"\nPor favor informe seu nome: ")
    response = input(f"\nEm que lugar você gostaria de passar suas próximas férias: ")

    # armazena a resposta no dicionário associada ao nome
    responses[name] = response

    # detecta se mais alguém que responder a pesquisa:
    repeat = input(f"Por favor informe se gostaria de responder novamente a pesquisa. Digite y [sim] ou n [não]:" )

    if repeat.lower() == "n":
        pesquisa_ativa = False

# Exibe a informação de pesquisa finalizada e mostra os resultadois:
mensagem = "\n-----PESQUISA CONCLUÍDA-----\n"

print(mensagem)

# extrai os itens do dicionário para mostrar o resultado da pesquisa:
for name, response in responses.items():
    print(f"{name.title()} gostaria de passar as proximas férias em {response.title()}")