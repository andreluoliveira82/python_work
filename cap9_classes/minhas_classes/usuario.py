
class Usuario:
    """modela um perfil de usuario"""
    #--------------------------------------------------------------------------
    def __init__(self, first_name, last_name, data_nasc, sexo):
        """Inicia as variaveis de usuario"""
        self.firts_name = first_name
        self.last_name = last_name
        self.data_nasc = data_nasc
        self.sexo = sexo
        self.login_attemps = 0
    #--------------------------------------------------------------------------
    def describe_user(self):
        """
        Descreve detalhadamente as caracteristicas do perfil do usuario
        """

        nome = self.firts_name
        nome_completo = self.firts_name + " " + self.last_name
        data_nasc = self.data_nasc
        sexo = self.sexo
        qtde_acessos = self.login_attemps
        
        print(f"""
        Nome do usuário: {nome.title()}
        Nome completo: {nome_completo.title()}
        Data de nasc.: {data_nasc}
        Sexo: {sexo.title()}
        Qtde acessos: {qtde_acessos}
        """)
    #--------------------------------------------------------------------------
    def increment_login_attemps(self):
        """
        incrementa o valor de 'login_attemps' em 1
        """
        self.login_attemps +=1
    #--------------------------------------------------------------------------
    def reset_login_attemps(self):
        """
        reseta o valor de 'login_attemps' para o valor 0
        """
        self.login_attemps = 0