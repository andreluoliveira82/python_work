
#André Oliveira
#05/10/2023 14h35
#Curso intensivo de Python

#----------------------------------------------------------------
#praticando exercicios de testes condicionais
# Escreva um programa que peça ao usuário para inserir três números e,
# em seguida, verifique se eles podem formar um triângulo. 
# Um triângulo é formado quando a soma de dois lados é maior que o terceiro lado.

#definindo manualmente os numeros que compõe o calculo do triangulo
ladoA =  25
ladoB =  45
ladoC =  20

import random

ladoA = random.randint(1,100)
ladoB = random.randint(1,100)
ladoC = random.randint(1,100)

print(f"\nÉ possível formar um triângulo com os números: {ladoA}, {ladoB}, e {ladoC}?")

# print(ladoA)
# print(ladoB)
# print(ladoC)


if  (ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB + ladoC > ladoA):
    print("\nSim, estes números podem formar um retangulo, pois a soma de dois de seus lados é maior que o terceiro lado")
else:
    print("\nNão, não é possível formar um triangulo com os numeros inseridos")
