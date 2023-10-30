
import printing_functions as pf


itens_pendentes = [
    "caneca","garrafa","bule","prato","brinquedo","relogio","phone case","bandeja","caixa de papelao"
    ]

itens_concluidos = [

]

#chamando as funções do modulo printing_functions:
pf.imprimir_modelos(itens_pendentes,itens_concluidos)

pf.exibir_modelos_concluidos(sorted(itens_concluidos))

print(f"\npendentes: {itens_pendentes}")
print(f"concluídos: {itens_concluidos}")