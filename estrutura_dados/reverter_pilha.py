
from estruturas_dados import Pilha

p = Pilha()

# p.push("andre")
# print(p.is_empty())

for c in "30andre":
    p.push(c)

print(p.peek())

reverse = ""

for i in range(len(p.items)):
    reverse += p.pop()

print(reverse.title())

