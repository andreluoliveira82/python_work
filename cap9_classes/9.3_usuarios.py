
from minhas_classes.usuario import Usuario as user

this_user = user("andre","oliveira","03/08/1982","m")

# # chama o metodo que incrementa o atributo 'login_attemps'
# this_user.increment_login_attemps()
# total_acessos = this_user.login_attemps


# -----------------------------------------------------------------
# imprimindo o log de acesso:
print("-----imprimindo o log de acesso-----")

# usando um loo for para simular vários acessos ao sistema
for n in range(1,11):
    # incrementa o atributo 'login_attemps' (o contador)
    this_user.increment_login_attemps()
    total_acessos = this_user.login_attemps
    this_user.describe_user()
    
    # print(f"Total de acessos: {total_acessos}.")

# simulando o reset de acessos:
print("-----simulando o reset de acessos-----")
this_user.reset_login_attemps()
this_user.describe_user()


