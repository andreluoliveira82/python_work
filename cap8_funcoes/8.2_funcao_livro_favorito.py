# André Oliveira
# 14/10/2023- 10h30
# Curso intensivo de Python
# cap. 8 - Funções
# ----------------------------------------------------------------------
# Exercicio 8.2 - livro favorito

def favorite_book(title, autor):
    """Exibe uma mensagem sobre o livro favorito passado como parametro da função"""

    # configurando a mensagem a ser exibida
    mensagem = f"\nUm dos meus livros favoritos é: {title.title()} de {autor.title()}.\n"

    #exibindo a mensagem
    print(mensagem)

# exemplo de chamada da função:
favorite_book("Curso Intensivo de Python 3 Edição",'Eric Matthes')