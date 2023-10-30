
class Car:
    """simples tentativa de representar um objeto carro"""

    def __init__(self, make, model, year, color):
        """Inicializa os atributos para descrever um carro"""
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.odometer_reading = 0
        self.capacity_combust_tank = 55.0
    
    def get_descriptive_name(self):
        """Retorna um nome descriptivo, formatado elegantemente"""
        long_name = f"{self.year} - {self.make} {self.model} {self.color}"
        return long_name.title()
    
    def read_odometer(self):
        """Exibe uma frase monstrando a kilometragem do carro em KM"""
        # print(f"Este veículo tem {self.odometer_reading} km rodados.")
        km = self.odometer_reading
        return km

    def update_odometer(self, km):
        """Define (atualiza) o odometro de um carro por meio do valor fornecedido"""

        if km >= int(self.odometer_reading):
            self.odometer_reading = km
        else:
            print(f"Você não pode inserir um km menor que o km atual ({self.odometer_reading})")

    def increment_odometer(self, km_increment):
        """Incrementa o odometro existente acrescentando o km passado no parametro"""

        # verifica se valor informado é um numero inteiro válido e maior que 0
        if  type(km_increment) is not int or km_increment <= 0:
            print(f"Você deve inserir um número inteiro positivo e maior que 0 (zero) para incrementar o odômetro")

        else:
            self.odometer_reading += km_increment
    
    def fill_gas_tank_description(self):
        """Informações sobre o tanque de combustível"""

        msg = (f"O tanque deste carro comporta {self.capacity_combust_tank} litros de combustível")

        return msg