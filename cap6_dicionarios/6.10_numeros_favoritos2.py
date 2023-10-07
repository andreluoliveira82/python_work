import random

#André Oliveira
#07/10/2023- 14h39
#Curso intensivo de Python
# cap. 6 - dicionarios
#----------------------------------------------------------------
#exercicio 6.10 - numeros favoritos 2

# Definindo a função que gera 03 numeros aleatorios
def criar_numeros_aleatorios():
    minimo = 1
    maximo = 100
    return [random.randint(minimo,maximo),random.randint(minimo,maximo),random.randint(minimo,maximo)]

#Criando o dicionario num_favoritos
num_favoritos = {
    'andre':criar_numeros_aleatorios(),
    'elizeth':criar_numeros_aleatorios(),
    'joao':criar_numeros_aleatorios(),
    'jordana':criar_numeros_aleatorios(),
    'mercia':criar_numeros_aleatorios(),
    'paulo':criar_numeros_aleatorios(),
    'lucas':criar_numeros_aleatorios(),
    'pedro':criar_numeros_aleatorios(),
    'poliana':criar_numeros_aleatorios(),
    'luana':criar_numeros_aleatorios(),
    'geraldo':criar_numeros_aleatorios(),
}

for name, numbers in num_favoritos.items():

    print(f'Numeros favoritos de {name.title()}')
    for numero in sorted(numbers):   
    
        print(numero)