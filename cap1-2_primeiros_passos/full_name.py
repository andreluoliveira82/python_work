#adicionando o primeiro nome a uma variavel
first_name = "andre"

#Adicionando o ultimo nome a uma variavel
last_name = "oliveira"

#Obtendo o nome completo por meio da junção das duas variaveis
# a letra f imediatamente antes da aspa inicial permite inserir as variaveis dentro de uma string e 
full_name = f"{first_name} {last_name}" #o f é de 'FORMATO' 

# Ao imprimir a variavel o pyton irá substituir as variaveis pelos valores armazenados nelas.
print (full_name)

#explorando mais os formatos de strings com o f
message= (f"Olá, {full_name.title()}!")

print(message)

#formatando a mensagem para inserir um espaço em branco por meio 
message= (f"Olá,\t{full_name.title()}!")
print (message)