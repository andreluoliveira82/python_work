#André Oliveira
#24/09/23
#Curso intensivo de Python - cap 2 - 
#-------------------------------------------------------------------------------
#exercicio 3.4
#armazenando nomes em uma lista
lst_convidados = ['vó francisca', 'alvercy', 'maria rosa', 'lourdes', 'henrique', 'irmaos', 'cunhados']
print(f'Lista de convidados original: \n{lst_convidados}')

nome = lst_convidados[3].title()
msg =f"\nO nome sorteado foi {nome}."
print(msg)
#-------------------------------------------------------------------------------
#exercicio 3.5
#Removendo um convidado por meio do metodo pop()
nomeRemovido = lst_convidados.pop(0).title()
msg =f"\n{nomeRemovido}, infelizmente não poderá comparecer ao jantar."
print(msg)
print(f'\nNova lista de convidados:\n{lst_convidados}')

#removendo cunhados da list, ou seja, trocando o nome de um convidado na lista
lst_convidados[5]='patricia'

#adicionando um novo convidade à lista
novo_convidado = "zé batista"
msg = f'\n{novo_convidado} é o novo convidado.'
print(msg)

lst_convidados.append(novo_convidado)
msg = f'\nEsta é a lista atualizada de convidados:\n {lst_convidados}'
print(msg)

#enviando convites para outras pessoas
pessoa_convidada=''

pess_1 = "Francisco"
pessoa_convidada=pess_1
convite = f'\nOlá, {pessoa_convidada}, bom dia!\n\tTemos o imenso prazer em enviar-lhe este convite para nosso jantar especial de lançaemento do nosso treinamento de listas no Python'
print(convite)

pess_2 = "Bill Gates"
pessoa_convidada=pess_2
convite = f'\nOlá, {pessoa_convidada}, bom dia!\n\tTemos o imenso prazer em enviar-lhe este convite para nosso jantar especial de lançaemento do nosso treinamento de listas no Python'
print(convite)

pess_3 = "John Wesley"
pessoa_convidada=pess_3
convite = f'\nOlá, {pessoa_convidada}, bom dia!\n\tTemos o imenso prazer em enviar-lhe este convite para nosso jantar especial de lançaemento do nosso treinamento de listas no Python'
print(convite)

#-------------------------------------------------------------------------------
#exercicio 3.6
#informando aos convidados que teremos mais convidados
#adicionando mais convidados e exibindo a lista atualizada

msg='\nTemos a satisfação em informar a todos que encotramos uma mesa maior e, sendo assim, nossa lista de convidados aumentou. \n Segue lista atualizada'
print(msg)

lst_convidados.insert(0,pess_1) #inserindo uma informação no começo da lista (posição 0)
lst_convidados.insert(4,pess_2) #inserindo uma informação no meio da litsa (qualquer posição)
lst_convidados.append(pess_3) #anexando uma informação no final da lista (metodo append)

msg = f'\nEsta é a lista atualizada de convidados:\n {lst_convidados}'
print(msg)

#-------------------------------------------------------------------------------
#exercicio 3.7 - reduzindo a lista de convidados

#Informando ao pessoal que a lista de convidados será reduzida.
msg = f'\nOlá pessoal, infelizmente não temos uma boa notícia! \nRecebemos a informação de que a nossa mesa grande não chegará a tempo de nosso encontro. Sendo assim teremos espaço para apenas dois convidados.\nLogo enviaremos a lista de convidados atualizada. Sentimos muito e pedimos sinceras desculpas'

print(msg)

#removendo alguns convidados da lista

texto_padrao = "lamentamos informá-lo(a) de que você foi removido(a) de nossa lista de convidados em razão da situação mencionada na mensagem enviada anteriormente. Pedimos, mais uma vez, sinceras desculpas pelo ocorrido."

convidado_removido = lst_convidados.pop(0,)
msg = f"\nOi {convidado_removido.title()}, {texto_padrao}"
print(msg)

convidado_removido = lst_convidados.pop(-1,)
msg = f"\nOi {convidado_removido.title()}, {texto_padrao}"
print(msg)

convidado_removido = lst_convidados.pop(4,)
msg = f"\nOi {convidado_removido.title()}, {texto_padrao}"
print(msg)

convidado_removido = lst_convidados.pop(5,)
msg = f"\nOi {convidado_removido.title()}, {texto_padrao}"
print(msg)

convidado_removido = lst_convidados.pop(-1,)
msg = f"\nOi {convidado_removido.title()}, {texto_padrao}"
print(msg)

convidado_removido = lst_convidados.pop(-1,)
msg = f"\nOi {convidado_removido.title()}, {texto_padrao}"
print(msg)

convidado_removido = lst_convidados.pop(-1,)
msg = f"\nOi {convidado_removido.title()}, {texto_padrao}"
print(msg)

convidado_removido = lst_convidados.pop(-1,)
msg = f"\nOi {convidado_removido.title()}, {texto_padrao}"
print(msg)

#exibindo a lista de convidados atualizada após eliminar alguns convidados
print(lst_convidados)

msg = f'\nOlá {lst_convidados[0]}!\n\t Ficamos felizes em informar que você continua em nossa lista de convidados para o jantar...'
print(msg)


msg = f'\nOlá {lst_convidados[1]}!\n\t Ficamos felizes em informar que você continua em nossa lista de convidados para o jantar...'
print(msg)

del lst_convidados[0]
del lst_convidados[0]

print (f'\nLista atual: {lst_convidados}')