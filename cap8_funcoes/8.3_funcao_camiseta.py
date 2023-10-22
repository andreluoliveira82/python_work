# André Oliveira
# 14/10/2023- 10h30
# Curso intensivo de Python
# cap. 8 - Funções
# ----------------------------------------------------------------------
# Exercicio 8.3 - camiseta

def make_shirt(tamanho, estampa):
    """Define o tamanho da camiseta e a estampa"""

    msg = f"Sua camiseta será do tamanho {tamanho} com seguinte estampa:\n{estampa}\n"

    print(msg)

# chamando a função passando argumentos posicionais
make_shirt(3,"pythonista.com")

# chamando a função passando argumentos nomeados
make_shirt(tamanho=4,estampa="sou + python")

# chamando a função passando argumentos nomeados invertidamente
# o resultado deve ser o mesmo que o apresentado na chamada anterior
make_shirt(estampa="sou + python",tamanho=4)