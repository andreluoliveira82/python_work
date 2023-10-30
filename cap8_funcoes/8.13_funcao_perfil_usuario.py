# André Oliveira
# 25/10/2023- 08h49
# Curso intensivo de Python
# cap. 8 - Funções
# ----------------------------------------------------------------------------
# Exercicio 8.13 - função que aceita diversos parametros

# definindo a função:
def build_profile(firstname,lastname,**info_profile):
    
    """
    cria um dicionario contendo tudo o que sabemos sobre o usuario
    """
    info_profile['first_name'] = firstname
    info_profile['last_name'] = lastname

    #retorna o dicionario na chamada da função
    return info_profile


# chamando a função
my_perfil = build_profile('André','Oliveira',funcao='programador',local='guarulhos')

# exibindo o resultado da chamada da função
print(my_perfil)