
# começa com uma lista de usuarios que precisam ser verificados:
# uma lista vazia a fim de armazenar os usuarios confirmados
#
unconfirmed_users = ['mariana','mariane','liliane','marcelo','pedro','livia']
confirmed_users = []

# faz a verificação de todos os usuarios até que a lista de usuarios não confirmados esteja vazia

while unconfirmed_users :
    current_user = unconfirmed_users.pop() # remove o ultimo elemento da lista

    #simulando um processo de confirmação do usuario
    print(f"Verificando usuario: {current_user.title()}")

    # adiciona o usuario na lista de usuarios confirmados
    confirmed_users.append(current_user)

# exibe todos os usuarios confirmados:
print(f"\nOs seguintes usuarios foram confirmados:")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())