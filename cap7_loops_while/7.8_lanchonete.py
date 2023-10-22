# André Oliveira
# 14/10/2023- 06h52
# Curso intensivo de Python
# cap. 7 - Loops While
# ----------------------------------------------------------------------
# preenchendo listas de sanduiches

# Lista de pedidos em espera
sandwich_orders =['hamburguer tradicional','pizza de atum', 'salgados','xbacon','pizza 4 queijos', 'pizza argentina']

finished_sandwiches = []

# mostrando a lista dos pedidos finalizados:
print("--------PEDIDOS FINALIZADOS--------")
while sandwich_orders:
    # remove o primeiro pedido que entrou na lista
    current_order = sandwich_orders.pop(0)
    print(f"\nSeu pedido de {current_order} está pronto")

    # adiciona o lanche finalizado à lista de pedidos finalizados
    finished_sandwiches.append(current_order)

# enumerando cada pedido da lista de pedidos finalizados
num_pedido = 0
print(f"\n--------ENUMERANDO OS LANCHES--------\n")
for sandwuich in finished_sandwiches:
    num_pedido += 1
    print(f"Pedido {num_pedido:2} - {sandwuich.title()}")
