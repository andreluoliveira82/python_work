#André Oliveira
#06/10/2023-20h37
#Curso intensivo de Python

#----------------------------------------------------------------

# capitulo 6 - dicionarios

# Extrair valores único (sem repetição ) de um dicionario


dic_frutas = {
    'maçã': 5,
    'banana': 3,
    'laranja': 7,
    'uva': 5,
    'morango': 2,
    'pêra': 4,
    'abacaxi': 1,
    'kiwi': 3,
    'manga': 2,
    'pêssego': 4
}
#Extraindo todos os itens (chave-valor) do dicionario
for fruta,valor in dic_frutas.items():
    print(f'{fruta} \t {valor}')

print("")
#Extraindo somente as chaves do dicionario
for f in dic_frutas.keys():
    print(f'{f.title()}')

print("")
#Extraindo somente os valores (todos) do dicionario
for v in dic_frutas.values():
    print(f'{v}')


#Extraindo somente os valores (unicos - sem repetição) do dicionario
print("\nExtraindo somente os valores (unicos - sem repetição) do dicionario")
for v in set(dic_frutas.values()):
    print(f'{v}')