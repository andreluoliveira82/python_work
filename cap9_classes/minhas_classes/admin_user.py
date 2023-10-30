# classe filha da classe Usuario:

from minhas_classes.usuario import Usuario

class Admin(Usuario):
    """Classe-filha da classe Usuario para modelar um ususario com privilégios de admin"""

    # -----------------------------------------------------------------------
    def __init__(self, first_name, last_name, data_nasc, sexo):
        """
        Inicializa os atributos da classe-pai
        e na sequencia inicializa os atributos da classe-filha
        """
        super().__init__(first_name, last_name, data_nasc, sexo)

        self.privileges = Privileges()

# ----------------------------------------------------------------------------
# Classe específica para definições de previlégios
class Privileges:
    """
    Classe-filha da classe Admin para definir os privilégios de um admin

    """
    def __init__(self):
        """
        Inicializa os atributos da classe
        """

    # atributo privilegies exclusivo da classe-filha Admin
        self.privileges = [
            "pode adicionar posts",
            "pode deletar posts",
            "pode banir usuário"
        ]
    # -----------------------------------------------------------------------
    def show_privileges(self):
        """
        Exibe a lista de privilégios que somente o usuario da classe Admin possui
        """

        privileges_list = self.privileges

        return privileges_list
    # -----------------------------------------------------------------------
    def remove_privileges(self, privilege_name):
        """
        Remove previlégios da lista de previlegios do admin
        """
        # se o previlégio passado como parametro não estiver na lista de previlégios:
        if privilege_name == "" or not privilege_name.lower() in self.privileges:
            print("para remover um previlégio, você deve informar o privilégio da lista de previlégios existentes")
        else:
            self.privileges.remove(privilege_name)

    # -----------------------------------------------------------------------
    def add_privileges(self, privilege_name):
        """
        Adiciona previlégios da lista de previlegios do admin
        """
        # se o previlégio passado como parametro não estiver na lista de previlégios:
        if privilege_name == "":
            print("para adicionar um previlégio, você deve informar o nome de privilégio")
        else:
            self.privileges.append(privilege_name)