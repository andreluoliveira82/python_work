
# importa a classe Restaurant
from minhas_classes.restautante import Restaurant as rt

# define o nome do restaurante e o tipo de comida
meu_restaurante = rt("coelhão","mineira")
meu_restaurante.number_served = 600

print(f"\n----------Abrindo o restaurante----------")
meu_restaurante.describe_restaurant()


nome = meu_restaurante.restaurant_name.title()
tipo_cozinha = meu_restaurante.cuisine_type.title()
pessoas_atendidas = int(meu_restaurante.number_served)

# =======================================================================
# fechando o restaurante
meu_restaurante.open_restaurant = "não"
meu_restaurante.number_served = 0
restaurante_aberto = meu_restaurante.open_restaurant
pessoas_atendidas=meu_restaurante.number_served

# print("--------------------------------------")
print(f"\n----------Fechando o restaurante----------")
print(f"Nome do restaurante: {nome}.\nCozinha tipo: {tipo_cozinha}\nRestaurante está aberto? {restaurante_aberto.title()}.\nPessoas atendidas: {pessoas_atendidas}.")

# =======================================================================
# abrindo novamente o restaurante
print(f"\n----------Abrindo o restaurante novamente----------")
meu_restaurante.open_restaurant
meu_restaurante.number_served = 850
meu_restaurante.describe_restaurant()

# ajustando o numero de pessoas atendidas por meio do metodo set_number_served:
print(f"\n----------ajustando a numero de pessoas servidas----------")
meu_restaurante.set_number_served(998)
meu_restaurante.describe_restaurant()

# incrementando o numero de pessoas atendidas por meio do metodo increment_number_served:
print(f"\n----------incrementando a numero de pessoas servidas----------")
increment = 20
meu_restaurante.increment_number_served(increment)

print(f"Atendemos mais {increment} pessoas. Desta forma o total de pessoas atendidas atualizado é {meu_restaurante.number_served}.\n")

meu_restaurante.describe_restaurant()