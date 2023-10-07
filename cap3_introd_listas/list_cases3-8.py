#André Oliveira
#25/09/23
#Curso intensivo de Python - cap 2 - 
#-------------------------------------------------------------------------------
#exercicio 3.8
#armazenando lugares em uma lista:
lugares =['lorena','sao luis','paris','gramado','foz do iguaçu','fernando de noronha','aguas de lindoia','bahrein','amsterdam','praga']

#Imprimind  lista na ordem original
print(f'Lista de lugares na ordem original em que fora criada:\n{lugares}') 

#exibindo a lista de lugares na ordem alfabética. 
#A função SORTED não altera a ordem da lista original
print(f'\nLista de lugares em ordem alfabética:\n{sorted(lugares)}')

#criando uma lista ordenada
lugares_ordem_dec = sorted(lugares,reverse=True)
print(f'\nLista de lugares em ordem decrescente:\n{lugares_ordem_dec}')

#demonstrando que a lista original ainda está na mesma ordem
print(f'\nDemonstrando que a lista original ainda está na mesma ordem:\n{lugares}')

'Ordenando a lista pelo metodo sort, de modo que agora a lista originl é alterada de modo permanenente'
lugares.sort()
print(f'\nLista ordenada agora pleo método sort\n{lugares}')

#Ordenando a lista pelo metodo sort com o argumento reverse, de modo que agora 
#a lista originl é alterada de modo permanente na ordem inversa (decrescente)

lugares.sort(reverse=True)
print(f'\nLista ordenada agora pleo método sort, com o argumento reverse=true:\n{lugares}')

#revertendo a ordem da lista

lugares.reverse()
print(f'\nLista invertida agora pleo método reverse:\n{lugares}')


#exercicio 3.9
#armazenando lugares em uma lista:
#descobrindo o tamanho da lista
qtde_iten_lista  = len(lugares)

print(f'\nQuantidade de itens na lista: {qtde_iten_lista}')

#-------------------------------------------------------------------------------
#exercicio 3.9
#usando a função len para descobrir o tamanho da ista de convidades para o jantar

