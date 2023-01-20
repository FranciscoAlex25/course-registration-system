from gerentes import Pessoa
from database import Database
import json


class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf, email, senha=None, curso=[]):
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

    # cadastrar clientes pelo gerente
    def cadastrar_clientes(self, nome, idade, cpf, email, senha=None, curso=[]):
        cliente = Cliente(nome, idade, cpf, email, senha, curso)

        Database.add_clientes_json(self, cliente)

    # listar os clientes cadastrados para o ADMIN
    def listar_clientes(self):
        with open('clientes.json', 'r', encoding='UTF-8') as arquivo:
            lista_de_clientes = json.load(arquivo)

        for cliente in lista_de_clientes:
            if len(cliente['_Cliente__curso']) > 0:
                print(f'''
                NOME: {cliente["_Pessoa__nome"]} | IDADE: {cliente["_Pessoa__idade"]} 
                CPF: {cliente["_Pessoa__cpf"]} | CÓDIGO: {cliente["_Cliente__email"]} 
                SENHA: {cliente["_Cliente__senha"]} | CURSO: {[nome["_Curso__nome"] for nome in cliente["_Cliente__curso"]]}
                '''.center(100))
            else:
                print(f'''
                NOME: {cliente["_Pessoa__nome"]} | IDADE: {cliente["_Pessoa__idade"]} 
                CPF: {cliente["_Pessoa__cpf"]} | CÓDIGO: {cliente["_Cliente__email"]} 
                SENHA: {cliente["_Cliente__senha"]} | CURSO: SEM CURSO
                '''.center(100))


if __name__ == '__main__':
    Cliente.cadastrar_clientes(
        '', 'Alex', 22, '203.322.333-12', '@gmail.com', '12345')
