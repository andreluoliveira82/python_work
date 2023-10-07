#andre oliveira
#22/09/2023


# texto com vários espaços no inicio e no final
# é muito comum, usuarios fazem esse tipo de cagada em diversos sistemas
# daí a importância de sabermos tratar as saídas de texyos

texto = "      Este é um texto curto com vários espaços no início e no final.     "

#Aqui o texto está sendo mostrado sem tratamento.
print (texto)

#removendo os espaços do inicio
texto_sem_espacos_inicio = texto.lstrip()
print(texto_sem_espacos_inicio)

#removendo espaços no fim do texto
texto_sem_espacos_final = texto.rstrip()
print(texto_sem_espacos_final)

#removendo espaços extras tanto no inicio com no fim do texto
texto_sem_espacos_extras = texto.strip()

#exibindo o texto precedido de uma quebra de linha (\n)
print(f'\n {texto_sem_espacos_extras}')