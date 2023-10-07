#André Oliveira
#06/10/2023-21h52
#Curso intensivo de Python
# cap. 6 - Dicionarios
#----------------------------------------------------------------
#Exercicio 6.5 - Dicionário de Rios;

rios = {
    'sao francisco':'o rio são francisco é um dos mais importantes do Brasil.',
    'amazonas':'Um grande rio do norte do Brasil',
    'negro':'um rio cujas águas são pretas.'
}

#Extraindo somente os nomes dos rios do dicionario
for rio in rios.keys():
    print(f'Rio {rio.title()}')
