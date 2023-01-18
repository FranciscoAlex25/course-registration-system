from database import Database
import json 
import os 


class Curso:
    def __init__(self, nome, duracao, certificado=True):
        self.__nome = nome 
        self.__duracao = duracao
        self.__certificado = certificado

    @property 
    def nome(self):
        return self.__nome
        
    @property
    def duracao(self):
        return self.__duracao

    @nome.setter
    def nome(self, nome):
        self.__nome = nome 
        
    @duracao.setter
    def duracao(self):
        self.__duracao

    def cadastrar_curso(self, nome, duracao, certificado=True):
        curso = Curso(nome, duracao, certificado)

        Database.add_cursos_json(self, curso)

    def listar_cursos(self):
        with open('cursos.json', 'r', encoding='UTF-8') as arquivo:
            cursos = json.load(arquivo)

        os.system('clear')

        print(80 * '-')
        for curso in cursos:
            print(f'''
            Nome: {curso["_Curso__nome"]} | Duração: {curso["_Curso__duracao"]} horas | Certificado: {curso["_Curso__certificado"]}
            '''.center(100))
        print(80 * '-')


if __name__ == '__main__':
    Curso.listar_cursos('')
