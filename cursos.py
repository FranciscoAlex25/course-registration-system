from database import Database
import json
import os


class Curso:
    def __init__(self, nome, duracao, certificado='sim'):
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

    # cadastra  os cursos pelo gerente
    def cadastrar_cursos(self, nome, duracao, certificado='sim'):
        curso = Curso(nome, duracao, certificado)

        Database.add_cursos_json(self, curso)

    # lista os cursos
    def listar_cursos(self):
        with open('cursos.json', 'r', encoding='UTF-8') as arquivo:
            cursos = json.load(arquivo)

        os.system('clear')

        # percorre os cursos e exibe no terminal
        for curso in cursos:
            print(f'''
            Nome: {curso["_Curso__nome"]} | Duração: {curso["_Curso__duracao"]} horas | Certificado: {curso["_Curso__certificado"]}
            '''.center(100))


if __name__ == '__main__':
    Curso.listar_cursos('')
