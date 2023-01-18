from database import Database
import json
import os
from gerentes import Gerente
from cursos import Curso


class Gerente_admin:
    def __init__(self):
        self.verificar_gerente()

    def verificar_gerente(self):
        os.system('clear')

        self.usuario = input('Digite seu usuário: ')
        self.codigo = input(f'Digite seu código de acesso {self.usuario}: ')

        with open('gerente.json', 'r', encoding='UTF-8') as arquivo:
            lista_de_gerentes = json.load(arquivo)

        for gerente in lista_de_gerentes:
            if (self.usuario not in gerente.values()) or (self.codigo not in gerente.values()):
                os.system('clear')
                print('DESCULPE, GERENTE OU SENHA INVÁLIDOS!')
            else:
                os.system('clear')
                self.exibir_menu_admin(self.usuario)

    def exibir_menu_admin(self, gerente):
        print(80 * '*')
        print(f'BEM VINDO(A) {gerente}'.center(80))
        print(80 * '*')

        print(80 * '-')
        print('''
            CADASTRAR GERENTE(1) - LISTAR GERENTE(2) 
            CADASTRAR CURSOS(3) - LISTAR  CURSOS(4) 
            CADASTRAR CLIENATES(5) - LISTAR CLIENTES(6)    
            '''.center(80))
        print(80 * '-')

        self.verificar_escolha()

    def verificar_escolha(self):
        self.escolha = input('DIGITE O NÚMERO DE SUA OPÇÃO: ')

        if self.escolha == '1':
            self.pedir_dados_gerente()

        elif self.escolha == '2':
            os.system('clear')

            print(80 * '-')
            Gerente.listar_gerentes(self)
            print(80 * '-')

            self.exibir_menu_admin(self.usuario)
            

        elif self.escolha == '3':
            self.pegar_dados_curso()

        elif self.escolha == '4':
            os.system('clear')

            print(80 * '-')
            Curso.listar_cursos(self)
            print(80 * '-')

            self.exibir_menu_admin(self.usuario)
           
        elif self.escolha == '5':
            ...
        elif self.escolha == '6':
            ...
        elif self.escolha == 'sair':
            ...
        else:
            os.system('clear')
            print('VALOR INFORMADO INVÁLIDO!')
            self.exibir_menu_admin(self.usuario)

    def pedir_dados_gerente(self):
        self.nome = input('Digite o nome do gerente: ')
        self.idade = input('Digite a idade do gerente: ')
        self.cpf = input('Digite o CPF do gerente: ')
        self.codigo = input('Digite o código de acesso do gerente: ')
        self.email = input('Digite o email do gerente: ')

        Gerente.cadastrar_gerente(
            '', self.nome, self.idade, self.cpf, self.codigo, self.email)

        os.system('clear')
        self.exibir_menu_admin(self.usuario)

    def pegar_dados_curso(self):
        self.nome = input('Digite o nome do curso: ')
        self.duracao = input('Digite a duração do curso: ')
        self.certificado = input('Tem certificado? ')

        Curso.cadastrar_cursos(self, self.nome, self.duracao, self.certificado)

        os.system('clear')
        self.exibir_menu_admin(self.usuario)
