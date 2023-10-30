# André Oliveira
# 25/10/2023- 09h30
# Curso intensivo de Python
# cap. 8 - Funções
# ----------------------------------------------------------------------------
# Exercicio 8.14 - função que aceita diversos parametros

# definindo a função:
def make_carros(marca,modelo,cor,ano, **info_carro):
    """cria um dicionario contendo informações sobre um carro"""

    info_carro ["marca"] = marca
    info_carro["modelo"] =modelo
    info_carro["cor"] = cor
    info_carro["ano"] = ano

    return info_carro

# chamando a funcao para testar
new_car = make_carros(
        "honda",
        "civic",
        "preto",
        "2023",
        bancos="couro",
        cambio="automatico",
        retrovisores="eletricos")

print(f"\n{new_car}")
