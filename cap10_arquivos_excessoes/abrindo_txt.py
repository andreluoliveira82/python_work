
from pathlib import Path

# arq = Path("//172.16.0.15/dadosh/T.I/CONVERSA  rODRIGO, DEVOLUÇÃO.txt")

# arq = Path("//172.16.0.15/dadosh/MARIA/conversa.txt")

arq = Path("cap10_arquivos_excessoes/aprendendo_python.txt")

try:
    contents = arq.read_text("utf-8")
 
except FileNotFoundError:
    print("Arquivo não localizado.")
else:
    # criando uma lista de palavras do conteúdo:
    words = contents.split()# por padrão o metodo split separa cada termo seguido de um espaço em obrigado (" ")

    # conta a quantidade de palavras na lista
    words_total = len(words) 

    # exibe o conteúdo do arquivo e na sequencia exibe a quantidade de palavras
    print(f"{contents}  \n\n este texto contém aprox. {words_total} palavras.")
