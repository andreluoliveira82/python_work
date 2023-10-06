#André Oliveira
#04/10/2023 16h12
#Curso intensivo de Python

#----------------------------------------------------------------
#exercicio 4.10 - Fatias

print(f'----------------------------------------------------------------\n')
print(f'Exercicio 4.10 - Trabalhando com fatias (slices) de listas\n')


#Lista de nomes biblicos
nomes_biblicos = ["Davi", "Sara", "Samuel", "Ana", "Abraão", "Ester", "Moisés", "Lia", "Jacó", "Rute", "Isaque", "Raquel", "Gideão", "Débora", "Elias", "Miriam", "Josué", "Noé", "Maria", "Salomão"]

#imprimindo a lista completa de nomes biblicos
print(nomes_biblicos)

qtde_nomes = len(nomes_biblicos)
print(f'\nHá {qtde_nomes} nomes na lista.')

top_3 =[nomes_biblicos[:3]]
print(f'\nO tres primeiros nomes são {top_3[:]}')

last_3 =[nomes_biblicos[-3:]]
print(f'\nOs três últimos nomes da lista são: {last_3[:]}')

nomes_meio = nomes_biblicos[11:16]
print(f'\nAlguns nomes do meio da lista {nomes_meio}')

#----------------------------------------------------------------
#4.11 - Minhas Pizzas

print(f'----------------------------------------------------------------\n')
print(f'Exercicio 4.11 - Minhas Pizzas')

my_pizzas = ["Margherita", "Pepperoni", "Quatro Queijos", "Calabresa", "Frango com Catupiry"]
friends_pizzas =my_pizzas[:]

#adicionando pizzas a lista de friends:
friends_pizzas.append("Portuguesa")

# modificando my_pizzas:
my_pizzas.append("Salmão")


print(f'\nMinhas pizzas favoritas são:\n')
for pizza in my_pizzas:
    print(pizza.title())

print(f'\nAs pizzas favoritas de meus amigos são:\n')
for pizza in friends_pizzas:
    print(pizza.title())

#----------------------------------------------------------------
#4.12 - mais loops

print(f'----------------------------------------------------------------\n')
print(f'Exercicio 4.12 - Mais Loops')

print(f'\nImprimindo cada nome da lista top 3:')
for nome in nomes_biblicos[:3]:
    print(f'\t{nome.title()}')

print(f'\nOs tres últimos nomes da lista são:\n')
for nome in nomes_biblicos[-3:]:
    print(f'\t{nome.title()}')