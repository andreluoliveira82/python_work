

#Se o nome do carro da lista de carros for de 3 letras, imprimir o nome com todas
# as letras em maiúculas, caso contrário, apenas a primeira letra de cada nome deve
# estar em maiúsculas:

# Definindo a lista de carros
carros = ['toyota','bmw','honda','ford','vwg']

for car in carros:
    #Verifica se o carro atual tem menos de 4 letras
    if len(car)<=3:
        print(car.upper()) #se o carro tiver 3 letras ou menos coloca tudo em maiúscula
    else:
        print(car.title()) #caso contrário impime apenas a primeira lerta em maiuscula

#---------------------------------------------
#EXERCÍCIO 5.1 - TESTES CONDICIONAIS

idade = 41
print('A idade é == 41? Você acertou.')
print(idade==41)