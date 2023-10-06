#André Oliveira
#06/10/2023-14h26
#Curso intensivo de Python
# cap. 6 - Dicionarios
#----------------------------------------------------------------
#exercicio 6.1 - pessoa

#Criando o dicionario 'pessoa'
pessoa = {
    'nome':'elizeth',
    'sobrenome':'oliveira',
    'idade':'35',
    'estado_civil':'casada',
    'sexo':'feminino',
    'profissao':'psicologa',
    'tem_filhos':'sim',
    'quantidade_filhos':'3'
}

#acessando informações do dicionario:

print(pessoa['nome'].title(),
      pessoa['sobrenome'].title(),
      pessoa['estado_civil']
      )