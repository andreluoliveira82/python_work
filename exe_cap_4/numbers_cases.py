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

#-------------------------------------------------------------------------------
# Estatísticas simples com uma lista de numeros:

numbers = list(range(0,1000001,10))
print(f'\nEstatísticas simples com uma lista de numeros:')
print(f'\nA lista contém {len(numbers)} elementos\n')
#print(numbers)
print(f'Mínimo: {min(numbers)}')
print(f'Máximo: {max(numbers)}')
print(f'Soma: {sum  (numbers)}')

#-------------------------------------------------------------------------------
#André Oliveira
#03-10-2023 noite
#Enquanto assistia a Corinthians e Fortaleza jogando pela Copa Sulamericana valendo um vaga na final
#----------------------------------------------------------------------------------------------------
#Exercicio 4.3 - contando de 1 a 20
numeros =[]
for n in range(1,21):
    numeros.append(n)

#exibindo o resultado
print(f'\nExercicio 4.3 - Lista dos números de 1 a 20:\n{numeros}') 

#----------------------------------------------------------------------------------------------------
#Exercicio 4.4 - Lista dos numeros de 1 a 1000000

#Criando a lista de numeros de 1 a 1000000
lista_milhao = list(range(1,1000001))

#Imprimindo cada numero da lista por meio do loop for
#for n in lista_milhao:
    #print(n)

#exibindo uma mensagem commum a todos os elementos
print(f'\nExercicio 4.4\nA lista do milhão contém {len(lista_milhao)} elementos')

#----------------------------------------------------------------------------------------------------
#Exercicio 4.5 - somando um milhão
#Criando a lista de numeros de 1 a 1000000
print('\nExercicio 4.5 - somando um milhão')
print(f'Mínimo: {min(lista_milhao)}')
print(f'Máximo: {max(lista_milhao)}')
print(f'Soma dos elementos: {sum(lista_milhao)}')

#----------------------------------------------------------------------------------------------------
#Exercicio 4.6 - Números Impres até 20
impares = list(range(1,20,2))

print('\nExercicio 4.6 - Números Impres até 20')
#imprimindo a lsita 
print(f'Lista dos numeros impares entre um 1 e 20\n{impares}')

#----------------------------------------------------------------------------------------------------
#Exercicio 4.7 - Múltiplos dos números de 3, entre 3 e 30
multiplos_tres = list(range(3,31,3))

print('\nExercicio 4.7 - Múltiplos dos números de 3, entre 3 e 30\n')

for n in multiplos_tres:
    print(n)

#imprimindo a uma mensagem comum a toda a lista
print(f'Lista dos numeros múltiplos de tres entre um 3 e 30\n{multiplos_tres}\n Contém {len(multiplos_tres)} elementos')

#----------------------------------------------------------------------------------------------------
#Exercicio 4.8 - Cubos dos 10 primeiros numeros

cubos_dez = []
soma_cubos=0

print('\nExercicio 4.8 - Cubos dos 10 primeiros numeros\n')

#Exibindo o valor cubo de cada numero
for n in range(1,11):
    
    print(f'{n}³ = {n**3}')
    cubos_dez.append({n ** 3}) #\gurdando os cubos em uma lista para usar depois / isto não fazia parte do execicio.
    soma_cubos = soma_cubos + (n ** 3) # Somando os cubos

#usando os cubos guardados em memoria
print(f'A soma dos cubos dos 10 primeiros numeros inteiros positivos é:\n {soma_cubos}')

#----------------------------------------------------------------------------------------------------
#Exercicio 4.9 - Cube Comprehension
cubos_dez = [n ** 3  for n in range(1,10)]

print(f'\n List Comprehension dos cubos:\n{cubos_dez}')