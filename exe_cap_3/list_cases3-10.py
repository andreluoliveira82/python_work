#André Oliveira
#25/09/23
#Curso intensivo de Python - cap 2 - 
#-------------------------------------------------------------------------------
#exercicio 3.10
#Lista de rios
rios = ['Nilo', 'Amazonas', 'Yangtze', 'Mississippi', 'Ienissei', 'Amarelo', 'Ob', 'Prata', 'Congo', 'Volga']
msg = f'\nLista original de rios:\n{rios}'

print(msg)

#inserindo um valor na lista
rios.insert(4,'Sao Francisco')
msg = f'\ninserindo um valor na lista\nLista atualizada de rios:\n{rios}'
print(msg)

#removendo um valor na lista
rios.remove('Ob')
msg = f'\nremovendo um valor na lista\nLista atualizada de rios:\n{rios}'
print(msg)

#removendo o ultimo valor da lista

rios.pop()
msg = f'\nremovendo o ultimo valor da lista\nLista atualizada de rios:\n{rios}'
print(msg)

#anexando um valor à lista

rios.append('Paranapiacaba')
msg = f'\nanexando um valor à lista\nLista atualizada de rios:\n{rios}'
print(msg)

#alterando/atualizando um valor da lista

rios[4] ='Doce'
msg = f'\nalterando/atualizando um valor da lista\nLista atualizada de rios:\n{rios}'
print(msg)

#Ordenando a lista de rios em ordem alfabética

rios.sort()
msg = f'\nOrdenando a lista de rios em ordem alfabética\nLista atualizada de rios:\n{rios}'
print(msg)

#lista de rios em ordem alfabética decrescente

rios.sort(reverse =True)
msg = f'\nlista de rios em ordem alfabética decrescente\nLista atualizada de rios:\n{rios}'
print(msg)

#exibindo a lista de rios em ordem iversa:
rios.reverse()
print(f'\nLista de rios em ordem iversa:\n{rios}')

#-------------------------------------------------------------------------------

#Criando uma lista de tuplas
