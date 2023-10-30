
from minhas_classes.dog import Dog as dg

my_dog = dg("paquito",10)
nome = my_dog.name.title()
idade = my_dog.age

print(f"\nO nome do meu cachorro é {nome}")
print(f"{nome} tem  {idade} anos de idade.")

my_dog.sentar()
my_dog.rolar()