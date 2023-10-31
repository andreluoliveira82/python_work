# André Oliveira
# 30/10/2023 20h55

# Livro Curso intensivo de Python
# cap. 10 - Arquivos e exceções
# ----------------------------------------------------------------------------
# exercicio 10.7 Calculadora de soma

from pathlib import Path

print("Digite os numeros a serem somados:\nQuando quiser finalizar o programa, digite 'q' \nDigite um número e tecle 'Enter': ")

num = ""
soma = 0
produto = 1
media = 0
menor = 0
maior = 0

numeros = []

while True:

    # finaliza o programa
    if str(num).lower() == 'q': 
        break 
    
    # recebe o valor inputado pelo user
    num = input("Número: ")
    
    try:
        num = int(num)
    
    except ValueError:
        # print(f"Você deve informar um número válido.")        
        pass # ignora qualquer erro e segue o codigo
    else:
        numeros.append(num)

        soma += num
        produto = produto * num
        media = soma / len(numeros)
        menor = min(numeros)
        maior = max(numeros)
        # print (f"Soma: {soma}")
        
# no final exibe a soma de todos os numeros inputados
print(f"Você digitou {len(numeros)} números válidos.")
print(f"A soma total dos números digitados é {soma}.\n")
print(f"O produto dos números digitados é {produto}.\n")
print(f"A média dos números digitados é {media:2}.\n")
print(f"O menor número digitado é {menor}.\n")
print(f"O maior número digitado é {maior}.\n")


# Salva o resultado em um arquivo txt
texto_result = (
    f"""
    Sistema de soma de valores\n
    Os números digitados foram {numeros}\n
    Soma: {soma}.
    Produto {produto}.
    Média: {media:2f} 
    menor: {menor} (posição {numeros.index(menor)})
    maior: {maior} (posição {numeros.index(maior)})
    """)

arq = Path("resultado.txt")
arq.write_text(texto_result,"utf-8")
