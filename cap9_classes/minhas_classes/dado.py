
# classe para o exercicio 9.13

from random import randint as rd

class Die:
    """
    Simples tentativa de modelar um dado para jogo de dados
    """
    def __init__(self, sides=6):
        """Inicializa os atributos da classe Die"""
        self.lados = sides

    def roll_die(self):
        """
        Exibe um numero aleatório entre 1 e 6 (numeros que o objeto 'dado' possui)
        """
        # sorteia um número aleatório entre 1 e o numeor de lados do dado
        sorted_num = rd(1,self.lados)

        return sorted_num

# ------------------classe da megasena--------------
class Megasena:
    """
    Simples tentativa de modelar um jogo da megasena
    """
    def __init__(self, values=60):
        """Inicializa os atributos da classe Die"""
        self.values = values
        self.nums = list(range(1, 11))
        self.letras = [
            "a","b","c","d","e",
            "f","g","h","i","j",
            "k","l","m","n","o",
            "p","q","r","s","t",
            "u","v","x","y","w","z"]

    def roll_megasena(self):
        """
        Exibe um numero aleatório entre 1 e 60
        """
        n = 0

        numeros_sorteados = []

        while n < 6:
            # sorteia um número aleatório entre 1 e o 60
            sorted_num = rd(1,self.values) 

            # print(sorted_num)       

            # se o numero sorteado já tiver saído
            if sorted_num not in numeros_sorteados:
                numeros_sorteados.append(sorted_num)
                n += 1
            else:
                continue

        print(sorted(numeros_sorteados))
        return numeros_sorteados
    
    def sorteio_bilhete(self):
        """Gera um sorteio aleatório de letras e numeros"""

        lista_alfa_num = []
        i=0
        c=0
        self.nums_sort = []

        while i < 10:
            lista_alfa_num.append(rd(1,9))
            i += 1

        while c < 5:
            lista_alfa_num.append(self.letras[rd(1,24)])
            c += 1
        

        i = 0
        
        while i < 4:
            self.nums_sort.append(lista_alfa_num[rd(1, 14)])
            i += 1
        print(f"{self.nums_sort}")
        return self.nums_sort
    