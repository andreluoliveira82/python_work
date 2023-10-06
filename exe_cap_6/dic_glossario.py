#André Oliveira
#06/10/2023-15h24
#Curso intensivo de Python
# cap. 6 - Dicionarios
#----------------------------------------------------------------
#Exercicio 6.3 - glossario

#Criando o dicionario glossario

glossario = {
    "tupla":"É um tipo de lista da linguagem Python. Entretanto diferentemente da lista 'normal', a tupla é imutável, isto é, seus valores não podem ser alterados ao longo do programa.",
    "dicionario":"É uma estrutura que armazena informações em pares chamadas 'chave:valor'",
    "indentação":"É o espaçamento definido por uma tabulação, ou 4 espaços",
    "PEP":"Python Enhancement Proposal (Proposta de Aprimoramento do Python). Especificamente, a PEP 8 trata da estilização do código",
    "list comprehension":"É a técnica usada por programadores experientes pra escrever um trecho loop for em uma única linha de código",
}

palavra = "tupla"
significado = glossario[palavra]

print(f'{palavra.upper()}:\n\t{significado.capitalize()}')