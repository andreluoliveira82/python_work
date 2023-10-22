# André Oliveira
# 21/10/2023- 21h20
# Curso intensivo de Python
# cap. 8 - Funções
# ----------------------------------------------------------------------------
# Exercicio 8.9 - passando uma lista com argumeto para os parâmetros de uma função

def print_models(unprinted_designs,completed_models):
    """
    simulando a impressao de cada design até que não reste nenhum na lista
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing Model: {current_design}")
        completed_models.append(current_design)


def show_completed_modles(completed_models):
    """
    exibr todos os modelos concluídos da lista de modelos completados

    """
    print(f"\nOs seguintes modelos foram concluídos:")

    for completed_model in completed_models:
        print(f"{completed_model.title()}")




itens_a_fazer = ["capa celular","chaveiro","caneca","camiseta","fronha"]
itens_feitos = []

# chamando as funçoes para teste

print_models(itens_a_fazer,itens_feitos)

show_completed_modles(sorted(itens_feitos))