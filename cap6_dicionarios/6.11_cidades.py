#André Oliveira
#07/10/2023- 20h52
#Curso intensivo de Python
# cap. 6 - dicionarios
#----------------------------------------------------------------
#exercicio 6.11 - cidades
cities = {
    'rio de janeiro':{
        'uf':'rj','populacao':6211423,'fato':'capital do estado do rio de janeiro','curiosidade':'a cidade sediou os jogos olímpicos de 2016'},

    'belo horizonte':{
        'uf':'mg','populacao':2315560,'fato':'capital do estado do minas gerais','curiosidade':'é a terceira cidade mais arborizada do Brasil'},

    'sao paulo':{
        'uf':'sp','populacao':11451245,'fato':'capital do estado de sao paulo','curiosidade':'é a cidade com o maior número de helicópteros particulares do mundo.'},
}

#Extrai cada cidade do dicionario principal (cities) e suas respectivas informações que estão em um outro dicionario 'filho' que será representado aqui pela variável city_info
for city, city_info in cities.items():
    print(f'\nCidade:{city.upper()}')

    #extrai as informaçõs do dicionario contido em cada cidade do dicionario pricipal (cities)
    estado = f'{city_info["uf"]}'
    populacao = f'{city_info["populacao"]}'
    fato = f'{city_info["fato"]}'
    curiosidade = f'{city_info["curiosidade"]}'

    print(f'\tUF: {estado.upper()}')
    print(f'\tPopulação: {populacao}')
    print(f'\tFato: {fato.title()}')
    print(f'\tCuriosidade: {curiosidade}')

print("---------------------------------------------------")
print ("Fim do programa\n")
