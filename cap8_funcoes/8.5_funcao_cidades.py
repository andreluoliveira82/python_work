# André Oliveira
# 14/10/2023- 10h30
# Curso intensivo de Python
# cap. 8 - Funções
# ----------------------------------------------------------------------
# Exercicio 8.5 - cidades

def describe_city(ctity_name, country_name="brasil"):

    """Descreve o nome da cidade e seu respectivo país
       Esta função trás o segundo argumento com o valor padrão como 'brasil'
       uma vez que na maioria dos casos as cidades serão deste país"""

    msg = (f"\n{ctity_name.title()} fica em {country_name.title()}\n")

    print(msg)


#chamada da função passando apenas o argumento sem valor padrão
describe_city('rio de janeiro')

#chamada da função passando todos os argumentos
describe_city('New York',"E.U.A")

#chamada da função passando apenas o argumento sem valor padrão
describe_city('são paulo')

#chamada da função passando todos os argumentos
describe_city('Johannesburgo',"africa do sul")