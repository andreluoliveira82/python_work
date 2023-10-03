#André Oliveira
#03/10/2023 - 04h30
#Curso intensivo de Python - cap 4 - trabalhando com numeros:

#função range()
#útil para gerar uma série de numeros

#por exemplo, prara gerar uma serie de numeoros de 1 a 100:
print('Lista numérica usando a função range()')
for n in range(0,101): #100 elementos 
    print(n)

print (f'foram gerados {(n)} elementos')

#==========================================================================
#fazendo operação com os valors da lista (do range())
#imprimindo cada valor do conjunto de numeros e seu respectivo quadrado

for n in range(101):
    print(f'{n}² = {n ** 2}')

print(f'\nImprimindo a raiz quadrada de cada numero da lista (intervalo)')
for n in range(2,101,2):
    n = n + 1
    print(f'A raiz quadrada de {n**2} é {n*n / n}')

#===========================================================================
#usando o range() para criar uma lista de valores através da função list()
#quando envolvemos a função list() em torno de range(), chamamos isso de wrapper

print(f'\n * Lista dos números impares entre 1 e 100:')

# armazena a lista dos numeros impares dentro da variavel 'numbers'
numbers = list(range(1,101,2))
print(f'{numbers}\nA lista de números contém {len(numbers)} elementos.')

print(f'\n * Lista dos números pares entre 1 e 100:')

# armazena a lista dos numeros pares dentro da variavel 'numbers'
numbers = list(range(2,101,2))
print(f'{numbers}\nA lista de números contém {len(numbers)} elementos.')

#anexando os 10 primeios numeros quadrados a uma lista
#definindo o nome da lista de qadrados
squares=[]

#loop pelo intervalo de numeros desejados
for n in range(1, 11):
    sq = n**2 # elevando n ao quadrado (n²)
    squares.append(sq) #anexando o resultado à lista de quadrados

#Imprimindo a lista de quadrados
print(f'\nA lista dos números quadrdados contém {len(squares)} elementos:\n{squares}')