
# André Oliveira
# 28/10/2023- 16h45
# Curso intensivo de Python
# cap. 9 - Classes
# ----------------------------------------------------------------------------
# Exercicio 9.6 - escrever uma classe-filha para modelar uma sorveteria

from minhas_classes.sorveteria import IceCreamStand as sorv

# criando a primeira instancia de IceCreamStand:
sorveteria_1 = sorv("ártico sorveteria","sorveteria")
sorveteria_1.set_number_served(354)

descripting_sorvet = sorveteria_1.describe_restaurant()
flavors_list = sorveteria_1.describe_ice_cream_flavors()

print(descripting_sorvet)

print (flavors_list)

# acrescentando sabores e reexibindo a lista:
sorveteria_1.include_flavor("abacate")
sorveteria_1.include_flavor("abacaxi")
sorveteria_1.include_flavor("maracujá")
sorveteria_1.include_flavor("kiwi")

flavors_list = sorveteria_1.describe_ice_cream_flavors()

print(f"Nossa lista de sabores foi atualizada {flavors_list}")

