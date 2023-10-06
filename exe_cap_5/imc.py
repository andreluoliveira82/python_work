#André Oliveira
#05/10/2023 15h52
#Curso intensivo de Python

#----------------------------------------------------------------
#praticando exercicios de testes condicionais


#Crie um programa que peça ao usuário para inserir sua altura em metros e seu peso em quilogramas, e então calcule o Índice de Massa Corporal (IMC) e classifique-o como "Abaixo do Peso", "Peso Normal", "Sobrepeso" ou "Obeso" com base nos valores típicos de IMC.

import random

altura = 1.82 # float(input("Digite sua altura em metros: "))
peso =  82.0 # float(input('Digite seu peso em kg: '))

# Calcula o IMC
imc = peso / (altura ** 2) # peso X altura ao quadrado

#Determinando a situação do paciente:

if imc < 18.5:
    categoria = "Abaixo do peso"
elif 18.5 <= 25.0:
    categoria = "Peso normal"
elif 15 <= 30:
    categoria = "Sobrepeso"
elif 30.0 <= 35:
    categoria = "Obesidade Grau 1"
elif 35.0 <= 40:
    categoria = "Obesidade Grau 2"
else:
    categoria = "Obesidade Grau 3"

# Imprime o resultado
print(f"Seu IMC é {imc:.2f}, e você está na categoria de peso: {categoria}")