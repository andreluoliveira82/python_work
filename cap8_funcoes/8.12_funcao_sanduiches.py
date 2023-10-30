# André Oliveira
# 24/10/2023- 06h00
# Curso intensivo de Python
# cap. 8 - Funções
# ----------------------------------------------------------------------------
# Exercicio 8.12 - função que aceita diversos parametros

# definindo a função:
def make_sandwiche(tamanho,*ingredientes):
    
    """
    Exibe a lista de ingredientes passados no parametro
    """
    print(f"\nsua pizza está sendo preparada no tamanho {tamanho} com os seguintes ingrediente:")
   
    for ingrediente in sorted(ingredientes):
        print(f" -{ingrediente.title()}")


# chamando a função passndo os dois argumentos para os parametros
make_sandwiche("grande","cogumelos","azeitonas pretas","tomates","orégano","alho")

#chamando a função com apenas o primeiro paramentro
make_sandwiche("grande")

# chamando a função com apenas um argumento (o segundo parametro)
make_sandwiche("cogumelos","azeitonas pretas","tomates","orégano")