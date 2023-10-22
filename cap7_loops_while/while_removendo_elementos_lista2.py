# André Oliveira
# 14/10/2023- 06h00
# Curso intensivo de Python
# cap. 7 - Loops While
# ----------------------------------------------------------------------

# usando loop while para remover elementos de uma lista ou dicionario
# NÃO DEVEMOS MODIFICAR UMA LISTA DENTRO DE UM LOOP FOR. PAG. 169

# ----------------------------------------------------------------------
# removendo TODAS AS INSTANCIAS de um valor específico de uma lista
# começa com uma lista de pets onde varios elementos são repetidos.
# os cats devem ser removidos da lista'
#
pets = ['cat', 'dog',
                     'fish', 'cat', 'cat', 'dog']

print(f"\nLista Original:\n{pets}")
# removendo todas as instancias 'cat' da lista pets
while 'cat' in pets:
    pets.remove('cat')

# imprimindo a lista atualizada para confirmar que os cats foram removidos:
print(f"\nLista atualizada:\n{pets}")