#André Oliveira
#24/09/23
#Curso intensivo de Python - cap 2 - 
#-------------------------------------------------------------------------------
#exercicio 3.1
#armazenando nomes em uma lista
list_names  = ['Elizeth Oliveira','Luiz Gabriel', 'Lucas Rafael', "Miguel Henrique"]

#imprimindo cada nome por sua vez
print(list_names[0].title())
print(list_names[1].title())
print(list_names[2].title())
print(list_names[3].title())

#-------------------------------------------------------------------------------
#Exercico 3.2
#cumprimenando cada pessoa da lista de nomes
cumprimento = 'Olá,'
mensagem = f'\n{cumprimento} {list_names[0].title()}, boa tarde!'
print(mensagem)
mensagem = f'\n{cumprimento} {list_names[1].title()}, boa tarde!'
print(mensagem)
mensagem = f'\n{cumprimento} {list_names[2].title()}, boa tarde!'
print(mensagem)
mensagem = f'\n{cumprimento} {list_names[3].title()}, boa tarde!'
print(mensagem)
#-------------------------------------------------------------------------------
#Exercico 3.3
#Criando minha propria lista
car_marks = ['honda','toyota','volkswagen','citroen','ferrari','mercedes']
#selecionando um carro da lista e exibindo uma mensagem na tela
select_car = car_marks[5].title()
nome = list_names[1].title()
msg = f'\nO carro preferido de {nome} é {select_car}.'
print(msg)

#selecionando um carro da lista e exibindo uma mensagem na tela
select_car = car_marks[3].title()
nome=list_names[2].title()
msg = f'\nO carro favorito de {nome} é {select_car}.'
print(msg)