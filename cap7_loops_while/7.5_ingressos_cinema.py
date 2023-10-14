# André Oliveira
# 13/10/2023- 18h00
# Curso intensivo de Python
# cap. 7 - Loops While
#----------------------------------------------------------------
#exercicio 7.5 - Ingressos de cinema

print (f"Digite sua idade para saber o valor do ingresso.\nPara sair do programa digite 'q'\n")


preco_ingresso = 0.00

value = ""
qtde_consultas = 0
valor_consultado =0

while value.lower() != 'q':

    value = input(f"\nInforme sua idade: ")

    if value.lower() == 'q':
        print(f"\nObrigado por usar nosso sitema.\nPor favor deixe sua avaliação. Isto é muito importante para nós, pois assim podemos melhorar ainda mais nossas ferramentas para melhor atendê-los.\n\nVisiste nossa pagina na web: www.precodocinema.com")

        continue

    qtde_consultas += 1
    
    if value.lower() != 'q':
        idade = int(value)

    if idade < 3 :
        preco_ingresso = 0
        

        print("Ingresso gratuito.")
    elif idade <= 12 :
        preco_ingresso = 12.75
    else:
        preco_ingresso = 15.00
    
    # acumula o valor_consultado para, no final, saber-se qual a previsão de receita, caso se concretize as vendas de todas as consultas.
    valor_consultado +=preco_ingresso

    print(f"O ingresso para pessoas da sua idade custa ${preco_ingresso:.2f}\n")

print(f"\nA previsão de receita com base nos valores consultados é de {valor_consultado:.2f}.\n")

print(f"A quantidade de consultas foi de : {qtde_consultas}\n")

print(f'O valor médio dos ingressos por pessoa é {valor_consultado / qtde_consultas:.2f}\n\n')


