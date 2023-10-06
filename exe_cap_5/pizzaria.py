#André Oliveira
#06/10/2023-06h20
#Curso intensivo de Python

#----------------------------------------------------------------
#praticando exercicios de testes condicionais

# Verificando se uma lista NÃO está vazia antes de seguir com o loop

# Definindo a lista de ingredientes a serem acrescentados ao pedido do cliente (neste caso vazia)
ingredintes_disponiveis = ['pimentão vermelho','queijo extra','azeitonas','ovos','sardinha']
ingredientes_acrescidos = []
ingredientes_excluidos = ["sardinha","azeitonas"]

print(f'Pizzaria Cekimanda\n Aqui quem manda é você!!!')
#Verificando se a lista contem algum elemento.
if ingredientes_acrescidos:      #retorna True se a lista NÃO for vazia
    print(' \nItens Acrescentados:')
    #para cada ingrediente acrescentado:
    for ingrediente in ingredientes_acrescidos:
        #Verifica se o ingrediente consta na lista de ingredientes disponíveis
        if ingrediente in ingredintes_disponiveis:
            #mostra que o ingrediente foi acrescentado:
            print(f'\t{ingrediente.title()}.')

        else: #Mostra que o ingrediente NÃO está disponível
            print(f"Sorry, we don't {ingrediente.title()}")

else: # Se o cliente não acrescentou nenhum item extra,sugere que ele acrescente
    #se a lista estiver vazia executa este trecho do codigo
    print(f'\nVocê realmente quer uma pizza normal? Não gostaria de acrescentar nada, como "Cogumelos","Pimentão Verde", ou "Picles"?\n')
    
if ingredientes_excluidos:    #retorna True se a lista NÃO for vazia
    print(' \nItens Removidos:')
    for ingrediente in ingredientes_excluidos:
        print(f'\t{ingrediente.title()}')

#informa ao cliente que o pedido foi concluído:
print(f'\nSeu pedido foi concluído. Sua pizza já está sendo preparada!')
