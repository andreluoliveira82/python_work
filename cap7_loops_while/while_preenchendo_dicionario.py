# André Oliveira
# 14/10/2023- 06h22
# Curso intensivo de Python
# cap. 7 - Loops While
# ----------------------------------------------------------------------
# preenchendo um dicionario com entrdas do usuario

respostas = {} # dicionário vazio

# define uma flag para sinalizar que a pesquisa está ativa:
pesquisa_ativo = True

while pesquisa_ativo:
    # coleta as informações do usuario:
    nome = input(f"\nQual é o seu nome? ")   
    resposta = input(f"Que montanha você gostaria de escalar? ")

    # armazena a resposta no dicionario:
    respostas[nome] = resposta

    # detecta se mais alguém particiará da pesquisa:
    repete = input("Gostaria de responder novamente? (y/n)")
    if repete.lower() == "n":
        pesquisa_ativo = False
    
# a pesquisa está finalizada. mostre os resultados:
print("\n---- Resultado da Pesquisa----")

# extraindo o par chave-valor do dicionario por meio de um loop for
for nome, resposta in respostas.items():
    print(f"{nome} gostaria de escalar {resposta}.")

print("\nObrigado por responderem a pesquisa.\n")