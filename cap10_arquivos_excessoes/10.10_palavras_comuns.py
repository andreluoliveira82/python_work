# André Oliveira
# 02/11/2023 20h55

# Livro Curso intensivo de Python
# cap. 10 - Arquivos e exceções
# ----------------------------------------------------------------------------
# exercicio 10.10 Palavras comuns

import sys
sys.path.append("C:\GitHub\python_work")

from estrutura_dados.palavras import Palavra as p

# lendo (carregando) o texto
texto = p.abrir_arquivo_txt("gnews_br.txt")

# tratando o texto
texto = p.remover_caracteres_especiais(texto)

# print(texto)


word = "mortos"

contagem = 0
vezes = ""

# sem separa o texto
# contagem = texto.lower().count(word.lower())

# separando o texto em linhas
# linhas = texto.splitlines()
# for lin in linhas:
#     contagem += lin.lower().count(word.lower())

# separando o texto em palavras
palavras = texto.split()
print(f"\nHá {len(palavras)} palavras no texto")

dic_words = {}

for palavra in palavras:

    # quero somente palavras com mais de 03 caracteres
    if len(palavra) > 3 and not palavra.isdigit():
        contagem = texto.lower().count(word.lower())
        
        # inserir cada palavra dicionario
        if palavra.lower() in dic_words:
            dic_words[palavra.lower()] += 1
        else:
            dic_words[palavra.lower()] = 1


# -------------------------------------------------------------------
word = word.upper()

if contagem > 1:
    vezes = "vezes"
    print(f"A palavra '{word}' aparece {contagem} {vezes} no texto.")
elif contagem == 1:
    vezes = "vez"
    print(f"A palavra '{word}' aparece {contagem} {vezes} no texto.")
else:
    print(f"A palavra '{word}' não aparece no texto.")

print("\n-------------------------------------------------------------")
# print(dic_words)

# exibe os pares chaves:valores ordenados por ordem decrescente de valor
for k, v in sorted(dic_words.items(),key=lambda item: item[1], reverse=True):
    # exibe na tela a chave e o valor de cada item do dicionario
    print(f"{k.upper()} ({v})")

# for lin in linhas:
#  print(lin)