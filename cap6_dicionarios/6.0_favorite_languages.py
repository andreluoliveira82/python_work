#André Oliveira
#06/10/2023-14h26
#Curso intensivo de Python

#----------------------------------------------------------------

# capitulo 6 - dicionarios

favorite_languages = {
    'andre':'python',
    'jonas':'csharp',
    'marcos':'c:',
    'lionel':'php',
    'marcio':'java script'
}

# imprimindo cada chave e seu respectivo valor por meio do loop for
for n, l in favorite_languages.items():

    print(f'A linguagem de programação favorita de {n.title()} é {l.upper()}')

print('Uhuuuu!\nEscrevi meu primeiro dicionário em Python!')