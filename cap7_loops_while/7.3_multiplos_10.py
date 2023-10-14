# André Oliveira
# 08/10/2023- 16h30
# Curso intensivo de Python
# cap. 7 - Loops While
#----------------------------------------------------------------
#exercicio 7.3 - Múltiplos de 10

# Definindo o texto do prompt
prompt = "\nInforme um número inteiro:\n"

#Recebendo a resposta pelo prompt
num = input(prompt)
#Convertendo a resposta em um inteiro
num = int(num)

# Verificando se o o numero é multiplo de 10.
# Numa divisão de qualqur numero por 10 cujo resto seja = 0
if num % 10 == 0 :

    print(f'\n{num} é múltiplo de 10.\n')
    print(f'{num}/10  = {int(num/10)}\n')

else:

    print(f'\n{num} não é multiplo de 10.\n')


