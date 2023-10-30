
# Exercício 9.6 - sorveteria
# classe especifica para uma sorveteria.
# já que a sorveteria também possui elementos do restaurante, esta classe será filha e vai herdar da classe-pai restaurant

from minhas_classes.restautante import Restaurant

class IceCreamStand(Restaurant):
    """ Modelagem de uma sorveteria, com base na classe-pai Restaurant"""

    # -----------------------------------------------------------------------
    def __init__(self, restaurant_name, cuisine_type):
        """
        Inicializa os atributos de restaurant
        Em seguida inicializa os atributos especificos de uma sorveteria
        """
        super().__init__(restaurant_name, cuisine_type)

        #atributo flavors para armazenar uma lista de sabores
        self.flavors = [
            "morango", "chocolate", "leite ninho","uva","banana","baunilha",
            "uva"
            ]
    # -----------------------------------------------------------------------
    def describe_ice_cream_flavors(self):
        """Exibem uma mensagem descrevendo a lista de sabores de sorveres de nossa sorveteria"""

        msg = f"Atualmente estes são nossos principais sabores de sorvetes:\n{ self.flavors}."

        return msg
    
    # -----------------------------------------------------------------------
    def include_flavor(self, flavor_name):
        """
        Acrescenta sabor à lista de flavors
        """
        if flavor_name == "":
            print("Você precisa informar o nome do sabor a ser incluído.")
        else:
            self.flavors.append(flavor_name)
    
