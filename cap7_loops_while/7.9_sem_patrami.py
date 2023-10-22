# André Oliveira
# 14/10/2023- 06h52
# Curso intensivo de Python
# cap. 7 - Loops While
# ----------------------------------------------------------------------
# preenchendo listas de sanduiches SEM PASTRAMI

# Lista de pedidos em espera
sandwich_orders =['pastrami','hamburguer tradicional','pizza de atum', 'salgados','pastrami','pastrami','xbacon','pizza 4 queijos','hamburguer com pastrami', 'pizza argentina','pastrami']

finished_sandwiches = []

# informando que a lanchonete está sem pastrami
print(f"\nlamentamos informar que estamos sem 'pastrami' em nossa lanchinete\n")

# removendo todas as ocorrencias de pastrami da lista original
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(f"Lista atualizada de sanduiches na fila de espera:\n{sandwich_orders}")

# Imprimindo a lista de pedidos finalizados: 
print(f"\n--------PEDIDOS FINALIZADOS--------")
while sandwich_orders:
    # remove o primeiro pedido que entrou na lista
    current_order = sandwich_orders.pop(0)
    print(f"\nSeu pedido de {current_order} está pronto")

    # adiciona o lanche finalizado à lista de pedidos finalizados
    finished_sandwiches.append(current_order)

# enumerando cada pedido finalizado:
num_pedido = 0
print(f"\n--------ENUMERANDO OS LANCHES--------\n")
for sandwuich in finished_sandwiches:
    num_pedido += 1
    print(f"Pedido {num_pedido:2} - {sandwuich.title()}")