# 5- Escreva um programa que peça ao usuário para inserir um ano e verifique se é um ano bissexto ou não. 
# Anos bissextos são divisíveis por 4, mas não por 100, a menos que sejam divisíveis por 400.

# import random

# obtem o ano aleatoreamente por meio da função randint da classe random
# ano_informado = random.randint(1,2023) #int(input('Digite o ano: '))

#definição de lista para armazenar todos os anos bissextos encontrados no intervalo
anos_bissextos=[]


for ano in range(1,2024):
    #Verifica se o resto da divisão (mod) do ano dividido por 4 = 0 e se o ano não é divisivel por 100, a menos que seja por 400
    if  (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        # armazena o ano bissexto encontrado na lista, na última posição 
        anos_bissextos.append(ano)

#imprimindo a mensagem com a quantidade de anos encontradas por meio da função len
# e exibindo o primeiro e o último ano bissextos no periodo por meio das funções min e max
print(f'Foram encontrados {len(anos_bissextos)} anos bissextos entre os anos 1 e 2023.\nO primeiro ano bissexto neste período foi o ano {min(anos_bissextos)} e o último foi o ano {max(anos_bissextos)}')

#imprimindo cada ano bissexto no na lista
for ano in anos_bissextos:
    print(ano)

print(f'\nFim do programa')
print ('\n--------------------------------------------------------------------')
