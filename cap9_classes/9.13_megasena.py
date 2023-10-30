
# Aproveitando oexercicio dos dados para simular a megasena
from minhas_classes.dado import Megasena
print("\nInstanciando a megasena com 60 numeros\n")
cartela = Megasena(60)

# cria uma cartela com 10 jogos
jogos = list(range(1,11))

# simulando os jogos

for jogo in jogos:
    print(f"Jogo {jogo}:")
    cartela.roll_megasena()
    print("\n")