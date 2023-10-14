import sys
import random
from enum import Enum


#Criando a classe RPS com enum para representar cada item do jogo
# Observação: Por tradição, toda constante no Python é nomeada em MAIUSCULAS
class RPS(Enum):
    PEDRA = 1
    PAPEL = 2
    TESOURA = 3

# Somadores de Pontuação
player_points = 0
computer_points = 0
v = 3
e = 1

print("")
print(f'Vai começar a batlha PPT. Prepare-se\n\nDigite ... \n1 para Pedra,\n2 para Papel, ou \n3 para Tesoura:\n\n')

for rodada in range(5):
    print("") #Imprime uma linha em branco para separar um jogo antigo de um novo

   # playerchoice = input(f'Digite ... \n1 para Pedra,\n2 para Papel, ou \n3 para Tesoura:\n\n')
    playerchoice = input('Sua vez: ')
    #Convertendo o numero informado em um inteiro (todo input entra como string)
    player = int(playerchoice)

    #Caso o jogador informe um valor fora da faixa permitida pelo jogo (1, 2 ou 3)
    if player < 1 or player > 3:

        #Caso o cabeçudo do jogador informar qualquer valor inválido para o nosso game,
        # o sistema envia uma mensagem de alerta e aborta o jogo:
        sys.exit("Você deve informar um numero : 1, 2 ou 3.")

    #Instruindo o computador a fazer a escolha aleatória de um numero entre 1,2 ou 3
    computerchoice = random.choice("123")
    #Convertendo a escolha do computador para um inteiro
    computer = int(computerchoice)

    print("")

    #==================================================================================================
    # aqui utilizamos a declaração Enum RPS para informar o valor escolhido pelo player e pelo computer
    # desta maneira a RPS vai devolver o texto relacionado ao valor escolhido para apresentar na na tela
    print("Você escolheu: \t" + str(RPS(player)).replace('RPS.',"").rjust(10) + ".") #substituindo o texto RPS. que aparece na resposta
    print("Python escolheu: " + str(RPS(computer)).replace('RPS.',"").rjust(10) + ".") # idem
    print("")

    #se o player escolheu pedra e o computer escolheu tesoura
    #Pedra é melhor que Tesoura
    if player == 1 and computer == 3:
        print("🍾 Você ganhou!")
        player_points += v
    #se o player escolheu papel e o computer escolheu pedra
    #papel é melhor que Pedra
    elif player == 2 and computer == 1:
        print("🍾 Você ganhou!")
        player_points += v
    #se o player escolheu Tesoura e o computer escolheu Papel
    #Tesoura é melhor que Papel
    elif player == 3 and computer == 2:
        print("🍾 Você ganhou!")
        player_points += v
    # se o player e o computer esolheram a mesma coisa
    elif player == computer:
        print("😲 Deu empate!")
        player_points += e
        computer_points += e
    #Em todas as outras sityações contrárias as condições anteriores, o computer ganha
    else:
        print("🐍 Python ganhou!") 
        computer_points += v
    
    print("-------------------------------------------")


#Fim do Jogo

if player_points > computer_points:
    msg = "Você venceu o jogo. Parabéns!\n🍾🍾🍾🍾🍾 "
elif player_points < computer_points:
    msg = "Python é o grande vencedor!\nNão desista, apenas continue tentando.\n🐍🐍🐍🐍🐍 "
else:
    msg = "Jogo duro! Deu empate.\nVocê pode tentar novamente, se quiser.\n😲😲😲😲😲 "

print("")
print("----------------------------------------------------")
print(f'Pontuação Final:\nVocê:\t{player_points}\nPython:\t{computer_points}\n\n{msg}')
print("====================================================")
print(f'Fim do jogo!')
print("")