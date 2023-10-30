
# escrevendo em um arquivo de texto

from pathlib import Path

# definindo o arquivo (neste caso sem um caminho absoluto, o arquivo será criado no mesmo local deste programa, caso ainda não exista.)
meu_arquivo = Path("arquivo_1.txt")

# escrevendo multiplas linhas para salvar em um arquivo de texto
texto = "No capítulo 10 estou aprendendo a manipular arquivos de texto com o Python. Isto é muito legal!\n\n"

texto += "Eu amo programar!\n"
texto += "Eu amo criar novos jogos!\n"
texto += "E também amo trabalhar com dados.\n"

# escrevendo no arquivo. O python abre, escreve e fecha adequadamente o arquivo
meu_arquivo.write_text(texto,encoding="utf-8")