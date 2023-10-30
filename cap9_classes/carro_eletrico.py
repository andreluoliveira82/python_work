# Criando um programa que exibe informações de qualquer veiculo com características de um carro eletrico representadas na classe EletricCar

# importantdo a classe eletric_car
from minhas_classes.eletric_car import EletricCar as ec

# instanciando o primeiro objeto eletric_car
my_car = ec("nissam","leaf",2024,"prata")

# exibe descrição detalhada do carro
print(f"Descrição Detalhada do {my_car.make.title()} {my_car.model.title()}\n")
print(my_car.get_descriptive_name())

# exibe descrição de detalhes da bateria do carro
my_car.battery.describe_battery()

# obtendo informações sonbre a distancia que a bateria do veiculo em questão pode percorrer com uma carga completa
distancia_bateria = my_car.battery.get_range()
print(distancia_bateria)


# simula alteração na bateria e exibe alterações
my_car.battery.update_battery(65)
print(f"\nA bateria do {my_car.model.title()} foi alterada para {my_car.battery.battery_size} amperes")
my_car.battery.batery_size = 65
my_car.battery.describe_battery()

# obtendo informações sonbre a distancia que a bateria do veiculo em questão pode percorrer com uma carga completa
distancia_bateria = my_car.battery.get_range()
print(distancia_bateria)

# mostrando o metodo que sobrescreve o metodo da classe-pai
tank_capacity_info = my_car.fill_gas_tank_description()
print(tank_capacity_info)
print("------------------------------------------------------------------")