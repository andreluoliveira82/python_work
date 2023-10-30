
# modelando um classe filha, que herdará metodos e atributos da classe-pai 'Car'

# importando a classe-pai existente
from minhas_classes.car import Car

# defininco a classe filha específica para carros eletricos
class EletricCar(Car):
    """
    Representa aspectos de um carro, específicos para veículos eletricos
    """

    def __init__(self, make, model, year, color):
        """
        Inicializa os atributos da classe-pai.
        Em seguida inicializa os atributos e métodos específicos para um carro eletrico

        """
        super().__init__(make, model, year, color)

        # chama (instancia) a classe Battery como fosse um metodo desta classe.
        self.battery = Battery()
    
    def fill_gas_tank_description(self):
        """Carros eletricos não tem tanque de combustível."""

        msg = ("Este carro não tem tanque de combustível, já que é um veículo elétrico.")

        return msg

# ---------------------------------------------------------------------
# definindo uma classe especifica para a bateria:
class Battery:
    """
    Classe específica para modelar uma bateria para carro eletrico
    """
    def __init__(self, battery_size=40):
        """Inicializa os atributos da bateria"""
        self.batery_size = battery_size

    # ---------------------------------------------------------------------
    def describe_battery(self):
        """
        Exibe uma frase descrevendo o tamanho da bateria
        """

        print(f"Este carro tem uma bateria de {self.batery_size} amperes.")

    # ---------------------------------------------------------------------
    def update_battery(self, new_size_battery):
        """
        atualiza o atributo battery_size com o valor informado no parametro
        """

        if type(new_size_battery) is not int or new_size_battery < 40:
            print("Voce deve informar o valor numerico válido.")

        else:
            self.battery_size = new_size_battery
    
    # ---------------------------------------------------------------------
    def get_range(self):
        """Exibe uma frase sobre a distancia que o carro percorre de acordo com a capacidade da bateria"""

        if self.batery_size == 40:
            range = 150
        elif self.batery_size == 65:
            range = 225
        
        msg = (f"Este veículo pode percorrer até {range} km com um carga completa.")

        return msg
