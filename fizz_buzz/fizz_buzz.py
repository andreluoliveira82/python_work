
def fizz_buzz():
    """
    Esta função percorre uma lista de números inteiros e verifica se cada número é divisível por 3, por 5 ou por 3 e 5.
    No caso de divisão exata por 3 imprime 'Fizz'.
    No caso de divisão exata por 5 imprime 'Buzz'.
    No caso de divisão exata por 3 ou 5 imprime 'FizzBuzz'
    caso contário imprime o proprio numero
    """

    for i in range(1,101):
        if i % 15 == 0: #3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fb = fizz_buzz()