from database import Database


class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.__nome = nome 
        self.__idade = idade
        self.__cpf = cpf  

    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade

    @property
    def cpf(self):
        return self.__cpf

    @nome.setter
    def nome(self, nome):
        self.__nome = nome 

    @idade.setter
    def idade(self, idade):
        self.__idade = idade
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf


class Gerente(Pessoa):
    def __init__(self, nome, idade, cpf, codigo, email):
        super(Gerente, self).__init__(nome, idade, cpf)
        self.__codigo = codigo
        self.__email = email

    @property
    def codigo(self):
        return self.__codigo
        
    @property
    def email(self):
        return self.__email

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
        
    @email.setter
    def email(self, email):
        self.__email = email

    def cadastrar_gerente(self, nome, idade, cpf, codigo, email):
        gerente = Gerente(nome, idade, cpf, codigo, email)
        Database.add_gerentes_json(self, gerente)
       

if __name__ == '__main__':
    Gerente.cadastrar_gerente('', 'alex', '22', '232.443.234-12', '123', 'franciscoalex@gmail.com')
