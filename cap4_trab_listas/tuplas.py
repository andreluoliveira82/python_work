#André Oliveira
#04/10/2023 19h30
#Curso intensivo de Python

#----------------------------------------------------------------
#Trabalhando com tuplas

# Uma Tupla é uma lista cujos valores permanecem imutáveis.
# A tupla é definida exatament como a lista, exceto pelo que se usa os parenteses ao invés dos colchetes

print(f'----------------------------------------------------------------\n')
print(f'Trabalhando Com Tuplas\n')

#Definindo uma tupla
dimensions = (200,50)
i=0

#imprimindo o valor de cada elemento da tupla
for dim in dimensions:
    i=i+1 
    print(f'dimensão {i} = {dim}')


# Exercicio 4.13 - Buffet

cardapio = ('peixe frito','frango caipira','costela assada','coelho','tilapia sem espinhos')
dias_semana = ('segunda','terça','quarta','quinta','sexta')
i = 0

print('Exercicio 4.13 - Buffet')

#imprimindo cada elemento do cardápio:
print('Cardápio da Semana:\n')

for prato in cardapio:
    print(f'{dias_semana[i].title()}:\n\t{prato.title()}')
    i=i+1

#Reformulando o cardápio (alterando a tupla)
cardapio = ('salada fria','frango caipira','feijoada','coelho','tilapia sem espinhos')

print("------------------------------------------------------------------------")
#imprimindo cada elemento do cardápio:
print('Cardápio da Semana reformulado:\n')
i = 0

for prato in cardapio:
    print(f'{dias_semana[i].title()}:\n\t{prato.title()}')
    i = i + 1