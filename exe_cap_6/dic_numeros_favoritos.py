#André Oliveira
#06/10/2023-14h26
#Curso intensivo de Python
# cap. 6 - Dicionarios
#----------------------------------------------------------------
#Exercicio 6.2 - numeros favoritos

#Criando o dicionario num_favoritos
num_favoritos = {
    'andre':'1982',
    'elzizeth':'28',
    'joao':'7',
    'jordana':'15',
    'mercia':'10',
    'paulo':'1854',
    'lucas':'02',
    'pedro':'21',
    'poliana':'30',
    'luana':'7',
    'geraldo':'14',
}

print(len(num_favoritos))

nome = 'mercia'
num_fav = num_favoritos[nome]
print(f'O número favorito de {nome.title()} é {num_fav}.')

# usando loop for para percorrer todos os pares chave-valor (items) do dicionario
# e exibir cada chave e seu respectivo valor:

# loop for percorrendo cada chave e valor do dicionario
# neste caso ainda usei a função sorted para deixar os nomes em ordem alfabética
for nome, valor in sorted(num_favoritos.items()):
    #imprime cada nome (chave) e seu respectivo valor
    print(f'O número favorito de {nome.title()} é {valor}.\n')