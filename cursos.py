from database import Database


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


if __name__ == '__main__':
    Curso.cadastrar_curso('', 'Java', '300')
