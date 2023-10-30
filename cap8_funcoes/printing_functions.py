
# função para imprimir modelos

def imprimir_modelos(pendentes, concluidos):

    #simula a impressao de cada modelo ate que não reste nenhum modelo na lista pedndentes:
    while pendentes:
        modelo_atual = pendentes.pop()

        print(f"Imprimindo modelo: {modelo_atual.title()}")
        
        concluidos.append(modelo_atual)

# função para mostrar os modelos concluidos:
def exibir_modelos_concluidos(modelos_concluidos):
    # exibe uma listagem com todos os modelos concluídos:
    print(f"\nOs seguintes modelos já foram finalizados:")

    for modelo in modelos_concluidos:
        print(f" -{modelo.title()}")
        