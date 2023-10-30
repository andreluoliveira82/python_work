# André Oliveira
# 28/10/2023- 20h38
# Curso intensivo de Python
# cap. 9 - Classes
# ----------------------------------------------------------------------------
# Exercicio 9.13 - Dados

from minhas_classes.dado import Die

# -----------------------------------------------------------------------------
# Criando (instanciando) o primeiro dado com 6 lados
print("\nInstanciando o primeiro dado com 06 lados")
dado = Die() # sem passar parametro pois por default o dado tem 06 lados na classe

# lista para armazenar os numeros sorteados
sorted_numbers = []

# Jogando o dado por 10 vezes como pede o exercício
for n in range(1, 11):
    value_die = dado.roll_die()
    sorted_numbers.append(value_die)
    print(f"Rodada {n}\nDado rolado número {value_die}.\n")

# Ao final de tudo mostra a lista dos numeros sorteados
print(sorted_numbers)
print(sorted(sorted_numbers))

# Dicionário para contar as ocorrências de cada numero
contagem = {}

for numero in sorted_numbers:
    if numero in contagem:
        contagem[numero] += 1 # Incrementa o contador se o número já existe no dicionário
    else:
        contagem[numero] = 1  # Inicializa o contador se o número é encontrado pela primeira vez

# Exibe a contagem de ocorrências
print("")
for numero, ocorrencias in sorted(contagem.items()):
    print(f"O número {numero} foi sorteado {ocorrencias} vezes.")

# -----------------------------------------------------------------------------

# Criando (instanciando) o segundo dado com 10 lados
print("\nInstanciando o segundo dado com 10 lados")
dado = Die(10)

# lista para armazenar os numeros sorteados
sorted_numbers = []

# Jogando o dado por 10 vezes como pede o exercício
for n in range(1, 11):
    value_die = dado.roll_die()
    sorted_numbers.append(value_die)
    print(f"Rodada {n}\nDado rolado número {value_die}.\n")

# Ao final de tudo mostra a lista dos numeros sorteados
print(sorted_numbers)
print(sorted(sorted_numbers))

# Dicionário para contar as ocorrências de cada numero
contagem = {}

for numero in sorted_numbers:
    if numero in contagem:
        contagem[numero] += 1 # Incrementa o contador se o número já existe no dicionário
    else:
        contagem[numero] = 1  # Inicializa o contador se o número é encontrado pela primeira vez

# Exibe a contagem de ocorrências
print("")
for numero, ocorrencias in sorted(contagem.items()):
    print(f"O número {numero} foi sorteado {ocorrencias} vezes.")

# -----------------------------------------------------------------------------


# Criando (instanciando) o segundo dado com 20 lados
print("\nInstanciando o segundo dado com 20 lados")
dado = Die(20)

# lista para armazenar os numeros sorteados
sorted_numbers = []

# Jogando o dado por 10 vezes como pede o exercício
for n in range(1, 11):
    value_die = dado.roll_die()
    sorted_numbers.append(value_die)
    print(f"Rodada {n}\nDado rolado número {value_die}.\n")

# Ao final de tudo mostra a lista dos numeros sorteados
print(sorted_numbers)
print(sorted(sorted_numbers))

# Dicionário para contar as ocorrências de cada numero
contagem = {}

for numero in sorted_numbers:
    if numero in contagem:
        contagem[numero] += 1 # Incrementa o contador se o número já existe no dicionário
    else:
        contagem[numero] = 1  # Inicializa o contador se o número é encontrado pela primeira vez

# Exibe a contagem de ocorrências
print("")
for numero, ocorrencias in sorted(contagem.items()):
    print(f"O número {numero} foi sorteado {ocorrencias} vezes.")

# -----------------------------------------------------------------------------
