from gerentes import Pessoa
from database import Database


class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf, email, senha, curso=None):
        super(Cliente, self).__init__(nome, idade, cpf)
        self.__email = email
        self.__senha = senha
        self.__curso = curso

    @property
    def email(self):
        return self.__email
            
    @property
    def senha(self):
        return self.__senha
    
    @property
    def curso(self):
        return self.__curso
        
    @email.setter
    def email(self, email):
        self.__email = email
        
    @senha.setter
    def senha(self, senha):
        self.__senha = senha
    
    @curso.setter
    def curso(self, curso):
        self.__curso = curso

    def cadastrar_clientes(self, nome, idade, cpf, email, senha, curso=None):
        cliente = Cliente(nome, idade, cpf, email, senha, curso)

        Database.add_clientes_json(self, cliente)


if __name__ == '__main__':
    Cliente.cadastrar_clientes('', 'Alex', 22, '203.322.333-12', '@gmail.com', '12345')
