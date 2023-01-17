import json, sys, os
caminho = os.path.dirname(__file__)


class Database:
    def add_gerentes_json(self, gerente):
        try:
            with open(caminho + '/gerente.json', 'r', encoding='UTF-8') as arquivo:
                lista_dos_gerente = json.load(arquivo)
                lista_dos_gerente.append(vars(gerente))

                print(lista_dos_gerente)
        
            with open(caminho + '/gerente.json', 'w+', encoding='UTF-8') as arquivo:
                json.dump(lista_dos_gerente, arquivo)     
        except:
            lista_dos_gerente = []
            with open(caminho + '/gerente.json', 'w+', encoding='UTF-8') as arquivo:
                lista_dos_gerente.append(vars(gerente))
                json.dump(lista_dos_gerente, arquivo)

    def add_cursos_json(self, curso):
        try:
            with open(caminho + '/cursos.json', 'r', encoding='UTF-8') as arquivo:
                lista_dos_cursos = json.load(arquivo)
                lista_dos_cursos.append(vars(curso))

                print(lista_dos_cursos)
        
            with open(caminho + '/cursos.json', 'w+', encoding='UTF-8') as arquivo:
                json.dump(lista_dos_cursos, arquivo)     
        except:
            lista_dos_cursos = []
            with open(caminho + '/cursos.json', 'w+', encoding='UTF-8') as arquivo:
                lista_dos_cursos.append(vars(curso))
                json.dump(lista_dos_cursos, arquivo)
