
# função para somara dois ou mais numeros inteiros

def soma(num1=0, num2=0):
    """soma os algarismos inteiros passados como parametros"""

    if type(num1) is not int or type(num2) is not int:
        return 0
    
    return num1 + num2