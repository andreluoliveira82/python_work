#André Oliveira
#02/10/2023
#Curso intensivo de Python - cap 4 - trabalhando com listas
#-------------------------------------------------------------------------------
#loop for

#Lista de rios
rios = ['Nilo', 'Amazonas', 'Yangtze', 'Mississippi', 'Ienissei', 'Amarelo', 'Ob', 'Prata', 'Congo', 'Volga']

for rio in rios:
    msg = f'\nRio {rio.upper()} - {len(rio)} letras'
    print (msg)

#02/10/2023 - 20:54
#Curso intensivo de Python - cap 4 - trabalhando com listas
#-------------------------------------------------------------------------------
#Exercicio 4.1 pizzas
#Lista de pizzas
pizzas = ['frango com requeijão','salaminho','queijo','com azeitonas']

print("--------------------------------------------------------")
for pizza in pizzas:
    msg = f'\nGosto de pizza de {pizza.title()}.'
    print (msg)

print(f'\nTodas estas pizzas são delicioas.')

print('--------------------------------------------------------------------')
#exercicio 4.2 

#definindo a lsita de animais
animals = ['gato','cachorro','papagaio','cavalo',]

#fazendo um loop por cada valor da lista e exibindo uma mensagem personalizda.
for animal in animals:
    msg = f'\nO {animal} é uma ótima companhia para o homem'
    print (msg)

#Exibindo uma mensagem comum a todos os itens da lista
print(f'Todos estes animais {animals} são, além de boas companhias, muito úteis ao homem!')
print('-------------------------------------------------------------------------------------\n')

