
from minhas_classes.car import Car as c

# chamando metodos e propriedades de car

# ==========================================================================
# instanciando um novo objeto com a classe car representada por c
my_car = c("volkswagen","voyage",2010,"preto")

# só para mostrar que a propriedade já inicia com o valor 0, estou comentando a linha abaixo que definiria o valor inicial para 0
# my_car.odometer_reading = 0

car_descripting = my_car.get_descriptive_name()
km_inicial = my_car.read_odometer()

# atualizano o odometro pelo metodo update_odometro
my_car.update_odometer(53000) 
km_atualizado = my_car.read_odometer()

# incrementando o odometro pelo metodo increment_odometer
my_car.increment_odometer(1653)
km_acrescentado = my_car.read_odometer()

print(f"Descrição completa:\n- {car_descripting.upper()}.")
print(f"Km inicial: {km_inicial}.")
print(f"Km atualizado: {km_atualizado}.")
print(f"Km incrementado: {km_acrescentado}.")
print("-------------------------------------------")

# ==========================================================================
# instanciando um novo objeto com a classe car representada por c
my_car = c("volkswagen","fusca",1989,"verde")

# obtendo a descrição completa do objeto elegantemente formatada
car_descripting = my_car.get_descriptive_name() 

# definidno o odometro (atributo) inicial de forma direta (atibuição)
my_car.odometer_reading = 49525
km_inicial = my_car.read_odometer()

# atualizando o odometro inicial por meio do metodo update_odometer
my_car.update_odometer(50002)
km_atualizado = my_car.read_odometer()


print(car_descripting.upper())
print(f"Odometro inicial: {km_inicial}")
print(f"km atualizado para: {km_atualizado}.")

# pintando o carro de outra cor
color_change = "laranja"
ano_change = 1999

my_car.year = ano_change # alterando o ano do carro
my_car.color=color_change # mudando a cor do carro

car_descripting = my_car.get_descriptive_name()
print(f"\nAno de {ano_change} Carro pintado na cor {color_change.upper()}\n{car_descripting.upper()}")
print("-------------------------------------------")

# ==========================================================================
# instanciando um novo objeto com a classe car representada por c
my_car = c("toyota","corolla",2017,"prata")

# alterando o odometro (km) inicial de forma direta (atribuição)
my_car.odometer_reading = 55000

# obtendo a descrição completa do objeto elegantemente formatada
car_descripting = c.get_descriptive_name(my_car)

# obtendo o odometro inicial por meio do metodo read_odometer
km_inicial = my_car.read_odometer()

# atualizando o odometro por meio do metodo update_odometer
my_car.update_odometer(55650)
km_atualizado = my_car.read_odometer()

print(car_descripting)
print(f"Odometro inicial: {km_inicial}")
print(f"Odômetro atualizado: {km_atualizado}")
print("-------------------------------------------")

# ==========================================================================
# instanciando um novo objeto com a classe car representada por c
my_car = c("renault","megane",2014,"azul")

# obtendo a descrição completa do objeto elegantemente formatada
car_descripting = c.get_descriptive_name(my_car)

# alterando o odometro (km) inicial de forma direta (atribuição)
my_car.odometer_reading="62000"
km_inicial = my_car.read_odometer()

# atualizando o odometro por meio do metodo update_odometer
my_car.update_odometer(62500)
km_atualizado = my_car.read_odometer()

# incrementando o odometro pelo metodo increment_odometer
my_car.increment_odometer(0)
km_acrescentado = my_car.read_odometer()

print(car_descripting)
print(f"Odometro inicial:{km_inicial}")
print(f"Odômetro atualizado: {km_atualizado}")
print(f"Km incrementado: {km_acrescentado}.")
print("-------------------------------------------")

# ==========================================================================