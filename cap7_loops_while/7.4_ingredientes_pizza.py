
# André Oliveira
# 08/10/2023- 16h30
# Curso intensivo de Python
# cap. 7 - Loops While
#----------------------------------------------------------------
#exercicio 7.4 - Ingredientes de Pizza

ingredientes = []

prompt = "\Preencha os ingredientes desejados:\nQuando terminar digite 'quit'.\n"
value = ""

print(f'{prompt}:\n')

# loop while enquanto o cliente não digitar 'quit'
while value != 'quit':

    value = input(" \n")
    ingredientes.append(value.lower())

#Imprime a lista em ordem alfabética
print(f'Aqui está a lista de seus ingredientes: \n\n{sorted(ingredientes)}\n\n')