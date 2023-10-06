#André Oliveira
#06/10/2023-07h13
#Curso intensivo de Python

#----------------------------------------------------------------
#praticando exercicios de testes condicionais e uso de Listas e Loops For

# 5.8 Programa Olá Admin
# Escreva um programa que exiba uma mensagem de boas vindas aos usuarios logados em um site.

logged_users = ['admin','andre','pedro','tiago','abraao','eva','dorcas']

#Removendo todos os usuario da lista para brincar com o teste da lista vazia:
logged_users = []

print(f'A lista contém agora {len(logged_users)} usuarios\n')

#verificando se a lista não está vazia:
if logged_users:
    #para cada usuario na lista de usaurios
    for user in sorted(logged_users):
        if user.lower() == 'admin':
            print(f'Olá Administrador!\nGostaria de ver um relatório de status?\n')
        else:
            print(f'Olá {user.title()}!\nObrigado por entrar novamente. Seja bem vindo!\n')
else:
    print(f'\nÉ necessário cadastrar alguns usuários.')


#========================================================================
# Exercicio 5.10 - Verificando nomes de usuarios:

print('----------------------------------------')
print('Exercicio 5.10 - Verificando nomes de usuarios:')

current_users = ['admin','andre','pedro','tiago','abraao','eva','dorcas']
new_users = ['andre','pedro','tiago']

#novos usuarios se cadastraram no site
new_users.append('joao')
new_users.append('paulo')
new_users.append('tito')

#Percorra a lista de novos usuarios para garantir que os nomes estejam disponíveis, isto é, que não existam na lista current_users:

if new_users: # se a lista de novos usuarios NÃO for vazia
    for new_user in new_users:
        # se o new_user consta (já existe) em current_users
        if new_user.lower() in current_users:
            print(f'O nome {new_user} não está disponível. Digite outro nome.\n')
        else:
            print(f'\nO nome {new_user} está disponivel. Gostaria de se cadastrar?')

