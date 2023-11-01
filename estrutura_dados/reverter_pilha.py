
from estruturas_dados import Stack

st = Stack()

st.push("andre")
print(st.is_empty())

# for c in "30andré":
#     st.push(c)

# print(st.peek())

reverse = ""

for i in range(len(st.items)):
    reverse += st.pop()

print(reverse.title())

