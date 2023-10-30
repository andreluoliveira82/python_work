
class Restaurant:
    """simples tentativa de criar um classe restaurant"""
   
    def __init__(self, restaurant_name, cuisine_type):
        """Inicia as variáveis 'restaurant_name' e 'cuisine_type'"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 # incluindo um atributo com o valor default = 0

    def open_restaurant(self, aberto="sim"):
        """
        Exibe uma mensagem informando se o restaurante está aberto ou fechado
        Por default o parametro é aberto=sim

        """
        # atributo
        name = self.restaurant_name
        print (f"O restaurante {name.title()} está aberto? {aberto.title()}")


    
    def describe_restaurant(self):
        """Imprime uma descrição detalhada do restaurante"""
        name = self.restaurant_name
        # print("------------------------------------")
        print(f"Descrição Detalhada do Restaurante {name.title()}.")
        print(f"\nO nome deste restaurante é {name.title()}.")
        print(f"A cozinha do {name} é tipo {self.cuisine_type.title()}.")
        print(f"Quantidade de pessoas atendidas hoje: {self.number_served}.")
        Restaurant.open_restaurant(self,"sim")

    # metodo para DEFINIR/ATUALIZAR o numero de pessoas atendidas:
    def set_number_served(self, number_served=0):     
        """
        metodo para definir/atualizar o numero de pessoas atendidas.
        por defaul o metodo é inicializdo com o paramentro number_served=0
        """

        if type(number_served) is not int or number_served <=0:
            print(f"Você deve informar um valor numerico maior que 0 (zero).")
        else:
            self.number_served = number_served

            return number_served
        
    # metodo para INCREMENTAR o numero de pessoas atendidas:
    def increment_number_served(self, number_increment=0):     
        """
        metodo para incrementar o numero de pessoas atendidas.
        por defaul o metodo é inicializado com o paramentro number_served=0
        Este médtodo acrescenta o valor informado ao valor já existente
        """

        if type(number_increment) is not int or number_increment <=0:
            print(f"Você deve informar um valor numerico maior que 0 (zero).")
        else:
            self.number_served += number_increment

            return self.number_served
        