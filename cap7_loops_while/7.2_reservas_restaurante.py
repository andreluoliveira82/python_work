# André Oliveira
# 08/10/2023- 16h30
# Curso intensivo de Python
# cap. 7 - Loops While
#----------------------------------------------------------------
#exercicio 7.2 - Reservas de mesa em Restaurante

# Definindo o texto do prompt
prompt = (f'\nQual a quantidade de mesas desejadas? \n')

# recebdeno a resposta do usuario por meio do prompr e armazenando em uma variavel, já convertendo o numero para um inteiro válido
qtde_mesa = int(input(prompt))

# Verificando se a quantidade solicitada está disponível
if qtde_mesa > 8 :
    print (f"\nInfelizmente não temos {qtde_mesa} mesas disponíveis.\nPor favor, aguarde a liberação e nós avisaremos assim que for possível.\n\n")
else:
    print(f'Ok caro cliente. Estamos reservando {qtde_mesa} mesas conforme solicitado.\n\n')
