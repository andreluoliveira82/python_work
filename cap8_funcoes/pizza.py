
# André Oliveira
# 25/10/2023- 09h30
# Curso intensivo de Python
# cap. 8 - Funções

# neste modulo ficarão armazenadas todas as funções para construção de pizzas

# função para montar uma pizza com os inggerdientes passados como parametros:

def make_pizza(tamanho, *ingredientes):
    """sintetiza a pizza que estamos prestes a fazer"""
    print(f"\nFazendo uma pizza {tamanho} com os seguintes ingredientes:")

    for ingrediente in sorted(ingredientes):
        print(f"-{ingrediente.title()}")
    