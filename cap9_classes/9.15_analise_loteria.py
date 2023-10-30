# André Oliveira
# 29/10/2023- 20h38
# Curso intensivo de Python
# cap. 9 - Classes
# ----------------------------------------------------------------------------
# Exercicio 9.14 - analise de loteria
# verifica através de um loop quão dificil é a chance de um bilhete ser sorteado
import time as tm

from minhas_classes.dado import Megasena


sorteio = Megasena()

meu_bilhete = [7,8,4,2]
rodada = 0

tempo_incial = tm.time()
tempo_final = 0

while True:
    rodada += 1
    
    print(f"Rodada: {rodada}")
   
    bilhete_sorteado = sorteio.sorteio_bilhete()

    
    if bilhete_sorteado == meu_bilhete:
        print (f"Voce ganhou após {rodada} rodadas")
        break
        
        
    else:
        continue

tempo_final = tm.time()
tempo_decorrido = tempo_final - tempo_incial

print(f"O programa levou {tempo_decorrido:.2f} segundos para sortear seu bilhete.")