# André Oliveira
# 14/10/2023- 10h30
# Curso intensivo de Python
# cap. 8 - Funções
# ----------------------------------------------------------------------
# Exercicio 8.4 - camisetas grandes

def make_shirt(tamanho="grande", estampa = "eu amo python"):
    """Define o tamanho da camiseta e a estampa
       Esta função já passa valores padrões nos dois argumentos"""

    msg = f"Sua camiseta será do tamanho {tamanho} com seguinte estampa:\n{estampa}\n"

    print(msg)

# chamando a função passando apenas um argumento
make_shirt("média")

# chamando a função sem passar nenhum argumento
make_shirt()

# chamando a função passando argumentos nomeados invertidamente
# o resultado deve ser o mesmo que o apresentado na chamada anterior
make_shirt(estampa="python é demais!",tamanho="extra grande")
