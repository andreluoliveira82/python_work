#André Oliveira
#07/10/2023- 14h39
#Curso intensivo de Python
# cap. 6 - dicionarios
#----------------------------------------------------------------
#exercicio 6.9 - Lugares favoritos

#Criando o dicionario favorite_places
# dicionario contendo uma lista de lugares para cada pessoa
favorite_places = {
    'andre':['praga','grecia','tokio','texas'],
    'livia':['manaus','vitória','teresina'],
    'kaio':['nova iorque','atenas','sidney'],
    'luiz gabriel':['guarulhos','roma','paris'],
    'luiz gabriel':['guarulhos','roma','paris']
}

#loop for pelo dicionario retornando cada pessoa e a respectiva lista de lugares de cada pessoa no dicionario:
for nome, lugares in favorite_places.items():
    # Imprime o texto seguido do nome de cada pessoa
    print(f'\nLugares favoritos de {nome.title()}:')

    # loop imprime cada lugar da lista de lugares de cada pessoa no dicionario:
    for lugar in lugares:
        print(f'\t{lugar.title()}')