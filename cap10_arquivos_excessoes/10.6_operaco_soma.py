# André Oliveira
# 30/10/2023 20h55

# Livro Curso intensivo de Python
# cap. 10 - Arquivos e exceções
# ----------------------------------------------------------------------------
# exercicio 10.6 Operação soma


num_1 = input("Digite um número: ")
num_2 = input("Digite outro número: ")

try:
    num_1 = int(num_1)
    num_2 = int(num_2)

except ValueError:
    print(f"Você deve informar um número válido.")
    # if type(num_1) is not int:
    #     print(f"'{num_1}' não é um número inteiro válido")
    # if type(num_2) is not int:
    #     print(f"'{num_2}' não é um número inteiro válido")
else:
    resultado = num_1 + num_2
    print(f"A soma de {num_1} e {num_2} é {resultado}")