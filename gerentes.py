from database import Database
import json


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

    # cadastra gerente pelo gerente principal
    def cadastrar_gerente(self, nome, idade, cpf, codigo, email):
        gerente = Gerente(nome, idade, cpf, codigo, email)
        Database.add_gerentes_json(self, gerente)

    # lista todos os gerentes cadastrados na "base de dados"
    def listar_gerentes(self):
        with open('gerente.json', 'r', encoding='UTF-8') as arquivo:
            lista_de_gerentes = json.load(arquivo)

        for gerente in lista_de_gerentes:
            print(f'''
            NOME: {gerente["_Pessoa__nome"]} | IDADE: {gerente["_Pessoa__idade"]} 
            CPF: {gerente["_Pessoa__cpf"]} | CÓDIGO: {gerente["_Gerente__codigo"]} EMAIL: {gerente["_Gerente__email"]}
            '''.center(100))
