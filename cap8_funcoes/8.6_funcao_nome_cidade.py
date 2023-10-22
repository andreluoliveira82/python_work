# André Oliveira
# 14/10/2023- 10h30
# Curso intensivo de Python
# cap. 8 - Funções
# ----------------------------------------------------------------------------
# Exercicio 8.6 - Função para retornar o nome da cidade e country
#=============================================================================
def describe_city_2(city_name, country_name="brasil"):

    """Descreve o nome da cidade e seu respectivo país
       Esta função trás o segundo argumento com o valor padrão como 'brasil'
       uma vez que na maioria dos casos as cidades serão deste país"""

    localidade =f"{city_name}, {country_name}"
    return localidade.title()

#==============================================================================

#chamada da função passando apenas o argumento sem valor padrão
print(describe_city_2('rio de janeiro'))

#chamada da função passando todos os argumentos
localidade = describe_city_2('New York',"E.U.A")
print(localidade)

#chamada da função passando apenas o argumento sem valor padrão
print(describe_city_2('são paulo'))

#chamada da função passando todos os argumentos
print(describe_city_2('Johannesburgo',"africa do sul"))