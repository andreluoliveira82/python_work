
# importa a classe Restaurant
from minhas_classes.restautante import Restaurant as rt

# define o nome do restaurante e o tipo de comida
meu_restaurante = rt("coelhão","mineira")

nome = meu_restaurante.restaurant_name.title()
tipo_cozinha = meu_restaurante.cuisine_type.title()

print(f"\nNome do restaurante: {nome}.\nCozinha tipo: {tipo_cozinha}.")

# descreve o restaurante
print(f"\n{rt.describe_restaurant(meu_restaurante)}")

# informa que o restaurante está aberto
print(f"{rt.open_restaurant(meu_restaurante)}")