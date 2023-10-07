#André Oliveira
#07/10/2023- 10h30
#Curso intensivo de Python
# cap. 6 - Dicionarios
#----------------------------------------------------------------
#exercicio 6.7 - pessoa 2

#Criando os dicionario 'pessoa'
pessoa_0 = {
    'nome':'mario',
    'sobrenome':'quintana',
    'idade':'87',
    'estado_civil':'casado',
    'sexo':'m',
    'profissao':'poeta',
    'tem_filhos':'sim',
    'quantidade_filhos':'7'
}
pessoa_1 = {
    'nome':'elizeth',
    'sobrenome':'oliveira',
    'idade':'35',
    'estado_civil':'casada',
    'sexo':'f',
    'profissao':'psicologa',
    'tem_filhos':'sim',
    'quantidade_filhos':'3'
}

pessoa_2 = {
    'nome':'mario jorge',
    'sobrenome':'zaggalo',
    'idade':'97',
    'estado_civil':'casado',
    'sexo':'m',
    'profissao':'treinador de futebol',
    'tem_filhos':'sim',
    'quantidade_filhos':'3'
}

#armazenando os dicionarios em uma lista:
pessoas = [pessoa_0,pessoa_1,pessoa_2]

# exibindo informações de cada pessoa cujos dicionarios estão contidos na lista pessoa:

# Extrai o dicionario completo de cada pessoa (p) na lista pessoas
for p in pessoas:
    print(f'\n{p}')
