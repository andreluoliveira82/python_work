
from estruturas_dados import Pilha

p = Pilha()

print(f"A pilha (lista) está vazia? {p.is_empty()}")

# adicionando um item na pilha
p.push("Feijão")
print(f"A pilha (lista) está vazia? {p.is_empty()}")
print(f"Quantidade de itens na pilha: {p.size()}")

# removendo um item na pilha
item_atual = p.pop()
print(f"Item atual removido: {item_atual}")
print(f"A pilha (lista) está vazia? {p.is_empty()}")

# adicionando varios itens à pilha
for i in range(25):
    p.push("produto "+ str(i))

print("Exibindo cada item da pilha:")
i=0
for item in p.items:
    try:
        print(p.items[i])
        i+=1
    except:
        pass

print(f"A pilha (lista) está vazia? {p.is_empty()}")
print(f"Quantidade de itens na pilha: {p.size()}")

# exibindo mas nao removendo cada item da pilha
print (f"\nexibindo mas nao removendo cada item da pilha")
for i in p.items:
    print(p.peek())

# exibindo e removendo cada item da pilha
print (f"\nexibindo e removendo cada item da pilha")
while p.items:
    item_atual = p.pop()
    print(item_atual)

print(f"A pilha (lista) está vazia? {p.is_empty()}")
print(f"Quantidade de itens na pilha: {p.size()}")
