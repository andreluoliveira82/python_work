
current_users = ['admin','andre','pedro','tiago','abraao','eva','dorcas']
new_users = current_users

#novos usuarios se cadastraram no site
new_users.append('joao')
new_users.append('paulo')
new_users.append('tito')

for user in new_users:
    if user[-1:].lower() == 'a' and user[0].lower() == 'a' or user[0].lower() == 't': # Verifica se os nomes terminam com a letra 'o'
        # imprime os nomes com as iniciais em maiusculas
        print(f'{user.title()}')


   