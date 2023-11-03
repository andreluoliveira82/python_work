
from palavras import Palavra

# --------------------------------------------------------------------------
testes = Palavra

# obtém um texto por meio da função abrir_arquivo_txt
texto = testes.abrir_arquivo_txt("gnews_world.txt") 
                         #noticias_google #gnews_br #gnews_world

# Remove os caracteres especiais do texto
texto_limpo = testes.remover_caracteres_especiais(texto)

# Exibe o texto sem os caracteres especiais
# print(texto_limpo.upper())
# print(texto_limpo)

lista_palavras = testes.lista_palavras_sem_repeticao(texto_limpo)

print("--------------------------------------------------")
print(f"Há {len(lista_palavras)} palavras que não se repetem na lista\n")

# # exibindo cada palavra na lista de palavras
# for palavra in sorted(palavras):
#     print(palavra.upper())

# ======================================================================
# muito louco esta lógica que fiz sozinho.
# compara cada palavra da lista de palavras com a proxima palavra
# eu fiz isso pq quero brincar com a função 'anagram' que verifica se duas palavras são anagramas. Daí pra deixar tudo mais interessante, fiz esta lógica que pega um arquivo de texto qualquer e extrai uma lista de palavras únicas e compara cada palavra com a a outra passando as duas para a função anagram.


j = 1
anagrams_count = 0
palindroms_count = 0
anagramas = []
palindromos = []

while lista_palavras:
    
    try:
        palavra1 = lista_palavras[0]

        for palavra in lista_palavras:
            try:
                palavra2 = lista_palavras[j]
            except:
                pass
            else:
                # # exibe as palvaras comparadas lado a lado
                # print(f"{palavra1} - {palavra2}")
                
                # verifica se as palavras comparadas são anagramas
                if palavra1.lower() != palavra2.lower() and testes.is_anagram(palavra1, palavra2):
                    # print(f"{palavra1} - {palavra2}")
                    anagramas.append(
                        str(palavra1.upper()) + " = " + str(palavra2).upper()
                        )
                    anagrams_count += 1
                j += 1

        # print(f"------{i}---------")
        # verificar se a palavra1 é um palindromo
        
        if testes.is_palindromo(palavra1):
            palindromos.append(palavra1.upper())
            palindroms_count =+ 1
        lista_palavras.remove(palavra1)

        j = 1

    except:
        #pass
        print(f"Erro: ")
    else:
        continue

print ("\n--------------------------------------------------------")

if anagrams_count == 0:
    print("\nNenhuma anagrama foi encontrado nas palavras deste texto")
else:
    print(f"foram localizadas {anagrams_count} anagramas:\n{anagramas}")

if palindroms_count > 0:
    print(f"\nForam localizadas {palindroms_count} palindromos:\n{palindromos}")
else:
    print("\nNenhum palindromo foi encontrado nas palavras deste texto")

print("\n-----Fim do Programa-----\n")
