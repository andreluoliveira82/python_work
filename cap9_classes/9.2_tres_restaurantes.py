
from minhas_classes.restautante import Restaurant as rt

# criando as instancias de cada restaurante
rest_1 = rt("costela de chão","churrascaria")
rest_2 = rt("Vaca na brasa","churrascaria")
rest_3 = rt("gauchão","lanchonete e churrascaria")


# ===================restaurante 1==================
print("\nRestaurante 1")
nome = rest_1.restaurant_name.title()
tipo_cozinha = rest_1.cuisine_type.title()
print(f"\nNome do restaurante: {nome}.\nTipo cozinha: {tipo_cozinha}.")
rt.describe_restaurant(rest_1)


# ===================restaurante 2==================
print("\nRestaurante 2")
nome = rest_2.restaurant_name.title()
tipo_cozinha = rest_2.cuisine_type.title()
print(f"\nNome do restaurante: {nome}.\nTipo cozinha: {tipo_cozinha}.")
rt.describe_restaurant(rest_2)


# ===================restaurante 3==================
print("\nRestaurante 3")
nome = rest_3.restaurant_name.title()
tipo_cozinha = rest_3.cuisine_type.title()
print(f"\nNome do restaurante: {nome}.\nTipo cozinha: {tipo_cozinha}.")
rt.describe_restaurant(rest_3)