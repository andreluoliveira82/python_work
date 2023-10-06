#André Oliveira
#05/10/2023 22h19
#Curso intensivo de Python

#----------------------------------------------------------------
#praticando exercicios de testes condicionais
# 5.7 Frutas favoritas:

frutas_favoritas = ['banana', 'abacate','abacaxi','laranja', 'mamao','graviola','melancia','gioaba','morango','maçã','manga','jaboticaba','mexirica','']

# Para cada fruta na lista de frutas ordenada (assim o resultado será apresentado em ordem alfabética)
for fruta in sorted(frutas_favoritas):
    # Verifica se a fruta começa com uma determinada letra
    if fruta[:1] == 'm': # se o 1º caractere da palavra for = 'm'
        print(f'{fruta.title()}') # Imprime a palavra com as iniciais maiúsculas


# Para extrair o primeiro (ou qualquer outro) caractere de cada palavra em uma lista:

# Para obter o primeiro caractere de uma palavra em uma lista em Python, você pode usar indexação. Em Python, as strings são indexadas como listas de caracteres, então você pode acessar o primeiro caractere de uma palavra usando [0].

## Uma lista de palavras
# palavras = ["Python", "Programação", "Exemplo"]
# 
# # Obtenha o primeiro caractere de cada palavra na lista
# primeiros_caracteres = [palavra[0] for palavra in palavras]
# 
# # Imprima os primeiros caracteres
# print(primeiros_caracteres)
# 