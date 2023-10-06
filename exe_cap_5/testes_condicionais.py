#André Oliveira
#05/10/2023 08h56
#Curso intensivo de Python

#----------------------------------------------------------------
#praticando exercicios de testes condicionais
import random

print(f'----------------------------------------------------------------\n')
print(f'Exercicio exercícios para prática de testes condicionais\n')

# 1 - Este programa veridica a faixa etária da pessoa e imprime uma mensagem de acordo com a idade informada

idade_informada = 17

if idade_informada < 18:
    print(f'Infelizmente você não está autorizado!')
elif idade_informada <=30:
    print(f'\nVocê pertence ao grupo de pessoas até 30 anos')
elif idade_informada <=60:
    print(f'\nVocê está no grupo de pessoas com mais de 30 anos e até 60 anos')
else:
    print(f'\nVocê já atingiu a idade para aposentadoria')


print(f'\nFim do programa')
print ('\n--------------------------------------------------------------------')

# 2 - Este programa veridica se o número informado é positivo, megativo ou zero

num_info = -0

if num_info < 0:
    print(f'\nO número informado é um número negativo.')
elif num_info >0:
    print(f'\n O número informado é um número positivo.')
else:
    print(f'O numero informado não é nem positivo, nem negativo. É 0 (zero).')

print(f'\nFim do programa')
print ('\n--------------------------------------------------------------------')

# 3- Faça um programa que solicite o nome do usuário e, em seguida, verifique se o nome é "Alice" ou "Bob".,
# Se for, imprima uma mensagem de boas-vindas; caso contrário, diga que o nome não é reconhecido.

# nome informado pelo usuario ao acessar o sistema
nome_informado = 'bob'

# tupla (lista) dos nomes validos para acessar o sistema
nomes_cadastrados = ('bob','alice','andre','joao','pedro','tiago','judas','simao zelote','judas iscariotes','tiago o menor','mateus')

# formata o nome informado
nome = nome_informado.title()

# verifica se o nome informado existe no cadastro do sitema
if nome_informado not in(nomes_cadastrados):
    print(f'O nome "{nome_informado.title()}" não está cadastrado em nosso sistema.\nVerifique se digitou corretamente ou faça seu cadastro.')
else:
    print(f'Olá {nome_informado.title()}\n\tSeja bem vindo. Tenha um ótimo dia!')

print(f'\nFim do programa')
print ('\n--------------------------------------------------------------------')
    

# 4- Crie um programa que peça ao usuário para inserir dois números e, em seguida,
# determine qual deles é o maior e imprima o resultado.

num1 = 15
num2 = 4
resultado=0

if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num1 < num2:
    print(f'{num1} é menor que {num2}')
else:
    print(f'{num1} é igual que {num2}')

# somando os numeros informados:
resultado = num1 + num2
print(f'\nA soma de {num1} e {num2} = {resultado}')

# subtraindo os numeros informados:
resultado = num1 - num2
print(f'\nA diferença entre {num1} e {num2} = {resultado}')

# multiplicando os numeros informados:
resultado = num1 * num2
print(f'\nO produto entre {num1} e {num2} = {resultado}')

# Dividindo os numeros informados:
resultado = num1 / num2
print(f'\nA divisão de {num1} por {num2} = {resultado}')

# potência dos numeros informados:
resultado = num1 ** num2
print(f'\nA potência de {num1} elevado a {num2} = {resultado}')

# a parte inteira da divisão dos numeros informados:
resultado = num1 // num2
print(f'\nO inteiro da divisão de {num1} por a {num2} = {resultado}')

# o resto da divisão dos numeros informados:
resultado = num1 % num2
print(f'\nO resto da divisão de {num1} por a {num2} = {resultado}')

print(f'\nFim do programa')
print ('\n--------------------------------------------------------------------')

# 5- Escreva um programa que peça ao usuário para inserir um ano e verifique se é um ano bissexto ou não. 
# Anos bissextos são divisíveis por 4, mas não por 100, a menos que sejam divisíveis por 400.

ano_informado = random.randint(1,2023) #int(input('Digite o ano: '))

#Verifica se o resto da divisão (mod) do ano dividido por 4 = 0 e se o ano não é divisivel por 100, a menos que seja por 400
if  (ano_informado % 4 == 0 and ano_informado % 100 != 0) or (ano_informado % 400 == 0):
    print(f"{ano_informado} é um ano bissexto.")
else:
    print(f"{ano_informado} não é um ano bissexto.")


print(f'\nFim do programa')
print ('\n--------------------------------------------------------------------')

# 6- Faça um programa que peça ao usuário para inserir um número e,
# em seguida, verifique se o número é par ou ímpar.

num_informado = random.randint(1,2023)  # int(input('Digite o número: '))

#Verifica se o resto da divisão (mod) do numero por 2 = 0 
# se for considera o numero como sendo par, caso contrário é impar

if  num_informado % 2 == 0 :
    print(f"{num_informado} é um número par.")
else:
    print(f"{num_informado} é um número impar.")


print(f'\nFim do programa')
print ('\n--------------------------------------------------------------------')
