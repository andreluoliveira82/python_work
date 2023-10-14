# André Oliveira
# 09/10/2023- 05h18
# Curso intensivo de Python
# cap. 7 - Loops While
#----------------------------------------------------------------
# exercicio 7.4 - Loop Cases:

meses = ('jan', 'fev', 'mar', 'abr','mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov','dez')

current_number = 0

while current_number <= 11 :
    current_number += 1
    if current_number == 0 or current_number % 2 == 0 :
        print(meses[current_number-1].title())

    
print("")

#---------------------------------------------
current_number = 0

while current_number < 12 :
    current_number += 1

    if current_number % 2 == 0 :
        continue
    
    print(meses[current_number].title())
