from cursos import Curso
from gerente_admin import Gerente_admin

class Main:
    def __init__(self):
        self.exibir_menu()
    
    # exibe o menu iniciar
    def exibir_menu(self):
        print(80 * '*')
        print('CURSOS ONLINE'.center(80))
        print(80 * '*')

        print(80 * '-')
        print('GERENTE(1) - CURSOS(2) - USUARIO(3)'.center(80))
        print(80 * '-')     

        self.verificar_escolha()

    # verifica qual escolha o usuário fez e chama a função
    def verificar_escolha(self):
        self.escolha = input('DIGITE O NÚMERO DE SUA OPÇÃO: ')

        self.opcoes = {
            '1': lambda: Gerente_admin(),
            '2': lambda: Curso.listar_cursos(self), 
            '3': lambda: self.entrar_area_usuario(self)
        }

        for opcao in self.opcoes.keys():
            if self.escolha == opcao:
                self.opcoes[opcao]()
       
        self.exibir_menu()


Main()
