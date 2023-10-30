# André Oliveira
# 22/10/2023- 06h00
# Curso intensivo de Python
# cap. 8 - Funções
# ----------------------------------------------------------------------------
# Exercicio 8.9 - passando uma lista com argumeto para os parâmetros de uma função

# definindo a função:
def show_messages(messages):
    """
    Exibindo cada mensagem da lista até que não reste nehnhuma
    """
    while messages:
        current_message = messages.pop()
        print(f"{current_message.upper()}")

lista_mensagens = ["bom dia!","olá","boa tarde", "boa noite"]

show_messages(lista_mensagens)