#André Oliveira
#05/10/2023 11h34
#Curso intensivo de Python

#----------------------------------------------------------------
#praticando exercicios de testes condicionais

print(f'----------------------------------------------------------------\n')
print(f'Exercícios para prática de testes condicionais\n')

# 7 - Crie um programa que solicite a nota de um aluno em um exame e, em seguida, 
# determine se a nota é A (90-100), B (80-89), C (70-79), D (60-69) ou F (abaixo de 60) e imprima a nota correspondente.

import random

media = random.randint(0,100)
nota = "A"

if media >= 90:
    nota="A"
    cumprimentos = "Parabéns. Bela nota!"
elif media >= 80:
    nota="B"
    cumprimentos = "Parabéns. Uma ótima nota!"
elif media >70:
    nota="C"
    cumprimentos = "Parabéns. boa nota!"
elif media >=60:
    nota="D"
    cumprimentos = "Parabéns. você está aprovado!"
else:
    nota="F"
    cumprimentos = "Que pena!. Poderia ter se esforçado mais!"

print(f'\nSua média é {media}\nSua nota é {nota} \n{cumprimentos}')

