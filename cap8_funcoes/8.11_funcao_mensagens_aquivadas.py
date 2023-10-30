# André Oliveira
# 22/10/2023- 06h00
# Curso intensivo de Python
# cap. 8 - Funções
# ----------------------------------------------------------------------------
# Exercicio 8.11 - passando uma CÓPIA da lista com argumento para os parâmetros de uma função

# definindo a função:
def sent_messages(original_messages, sent_messages):
    """
    Exibindo cada mensagem da lista até que não reste nehnhuma
    """
    while original_messages:
        # remove a mensagem da lista original
        current_message = original_messages.pop()

        # Adiciona a mensagem à lista de mensagens enviadas
        mensagens_enviadas.append(current_message)

        print(f"{current_message.upper()}")


def show_messages(mensagens_enviadas):
    """
    imprimindo uma serie de mensagens da lista
    """
    print(f"\nAs seguintes mensagens foram emitidas:")

    for msg in mensagens_enviadas:
        print(msg.title())


lista_mensagens = ["bom dia!","olá","boa tarde", "boa noite"]
mensagens_enviadas = []

# passando a CÓPIA da lista de mensagens
sent_messages(lista_mensagens[:],mensagens_enviadas)
show_messages(mensagens_enviadas)

# exibindo as duas listas conforme pede o exercicio para verificar o estado das listas:
print(f"\nLista Original:\n{lista_mensagens}")
print(f"\nLista de mensagens conlcuídas:\n{mensagens_enviadas}")
