from gerentes import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf, email, senha, curso):
        super(Cliente, self).__init__(nome, idade, cpf)
        self.__email = email
        self.__senha = senha
        self.__curso = None

        @property
        def email(self):
            return self.__email
            
        @property
        def senha(self):
            return self.__senha
        
        @email.setter
        def email(self, email):
            self.__email = email
        
        @senha.setter
        def senha(self, senha):
            self.__senha = senha
