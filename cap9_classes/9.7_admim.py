# André Oliveira
# 28/10/2023- 16h45
# Curso intensivo de Python
# cap. 9 - Classes
# ----------------------------------------------------------------------------
# Exercicio 9.7 - escrever uma classe-filha para modelar uma sorveteria

from minhas_classes.admin_user import Admin

use_adm = Admin("andre","oliveira","03/08/1982","masculino")
acessos = use_adm.increment_login_attemps()

list_privileges = use_adm.privileges.show_privileges()

print("Descrevendo o perfil completo do usuário")
use_adm.describe_user()

print(f"\nEste usuário possui os seguintes privilégios:")

for privilege in list_privileges:
    print(f" -{privilege}")

# ----------------------------------------------------------------------------
# Adicionando um previlégio:
print(f"\nAdicionando previlégios:")

previlegios_add = ["Pode adicionar usuario comum", "pode cadastrar produtos"]

for p in previlegios_add:           
    use_adm.privileges.add_privileges(p)
    print(f" -{p}")

# exibindo a lista atualizada de previlegios
print(f"\nLista atualizada com todos os privilégios:")

for privilege in list_privileges:
    print(f" -{privilege}")

# ----------------------------------------------------------------------------
# Removendo um previlégio:
print(f"\nRemovendo previlégios:")

previlegios_remove = ["pode banir usuário", "pode cadastrar produtos"]

for p in previlegios_remove:           
    use_adm.privileges.remove_privileges(p)
    print(f" -{p}")

# exibindo a lista atualizada de previlegios
print(f"\nLista atualizada com todos os privilégios:")

for p in list_privileges:
    print(f" -{p}")