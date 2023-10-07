#André Oliveira
#07/10/2023- 10h50
#Curso intensivo de Python
# cap. 6 - dicionarios
#----------------------------------------------------------------
#exercicio 6.8 - animal de estimação

#Criando os dicionarios
animal_0 = {
    'tipo':'cao',
    'raca':'pitibull',
    'nome':'plutão',
    'nome_dono':'Jodiel',
}

animal_1 = {
    'tipo':'gato',
    'raca':'ciames',
    'nome':'nice',
    'nome_dono':'andre',
}

animal_2 = {
    'tipo':'passaro',
    'raca':'n/a',
    'nome':'bicudo',
    'nome_dono':'celso',
}

#armazenando os dicionarios de animais na lista pets
pets = [animal_0,animal_1,animal_2]

# for para cada elemento (dicionario) contido em lista pets
for p in pets:
    print("")
    #loop for por cada atibuto de cada elemento (p) 
    for key,valor in p.items():
        #Extrai o par chave-valor de cada elemento do dicionario representado em 'p' (pets)
        print(F'{key.rjust(10)}:\t{valor.title()}')
 