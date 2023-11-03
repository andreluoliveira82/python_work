
from estruturas import Queue

pacientes = ["luiz gabriel","lucas rafael","miguel henrique","joão pedro"]

q = Queue()

# enfileirando os pacientes e exibindo a quantidade
for p in pacientes:
    q.enqueue(p)

print(f"Há atualmente {q.size()} elementos na fila")

# exibindo mas nao removendo o próximo item da fila
print (f"\nExibindo mas nao removendo o próximo item da fila")
print(f"Próximo da fila: {q.peek().title()}")

# extrair os elementos da fila
print("\n-----Exibir os elementos da fila na ordem em que entraram sem removê-los-----")

pessoas_cadastradas = q.items
i = q.size()

while i > 0:  
    pessoa = pessoas_cadastradas[i-1]
    print(pessoa.title())
    i-=1

# mostrando que os elementos continuam na fila original
print(f"\nHá atualmente {q.size()} elementos na fila")

# finalmente exibindo mas nao removendo o próximo item da fila
print (f"\nFinalmente exibindo e removendo cada item da fila")

while q.items:
    print(q.dequeue().title())

# mostrando que os elementos foram removidos da fila original
print(f"\nHá atualmente {q.size()} elementos na fila")