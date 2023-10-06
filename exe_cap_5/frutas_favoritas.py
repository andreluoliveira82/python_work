#André Oliveira
#05/10/2023 22h19
#Curso intensivo de Python

#----------------------------------------------------------------
#praticando exercicios de testes condicionais
# 5.7 Frutas favoritas:

frutas_favoritas = ['banana', 'abacate','abacaxi','laranja', 'mamao','graviola','melancia','gioaba','morango','maçã','manga','jaboticaba','mexirica']

for fruta in frutas_favoritas:

    if (fruta,1) == 'm':
        print(f'{fruta.title()}')
