import json, sys, os
caminho = os.path.dirname(__file__)


class Database:
    ''' 
        Este método de instância busca os gerentes já cadastrados na 
        "base de dados" e adiciona o novo gerente que está sendo cadastrado
    '''
    def add_gerentes_json(self, gerente):
        # Tenta ler o arquiso Json se não estiver vazio
        try:
            # busca os gerentes na "base de dados"
            with open(caminho + '/gerente.json', 'r', encoding='UTF-8') as arquivo:
                lista_dos_gerente = json.load(arquivo)
                lista_dos_gerente.append(vars(gerente))

            # adiciona os antigos e novo gerente na "base de dados"
            with open(caminho + '/gerente.json', 'w+', encoding='UTF-8') as arquivo:
                json.dump(lista_dos_gerente, arquivo)
        # adiciona um novo gerente se o arquivo Json estiver vazio
        except:
            lista_dos_gerente = []
            with open(caminho + '/gerente.json', 'w+', encoding='UTF-8') as arquivo:
                lista_dos_gerente.append(vars(gerente))
                json.dump(lista_dos_gerente, arquivo)

    ''' 
        Este método de instância busca os cursos já cadastrados na 
        "base de dados" e adiciona o novo curso que está sendo cadastrado
    '''
    def add_cursos_json(self, curso):
        # Tenta ler o arquiso Json se não estiver vazio
        try:
            with open(caminho + '/cursos.json', 'r', encoding='UTF-8') as arquivo:
                lista_dos_cursos = json.load(arquivo)
                lista_dos_cursos.append(vars(curso))

                print(lista_dos_cursos)
        
            with open(caminho + '/cursos.json', 'w+', encoding='UTF-8') as arquivo:
                json.dump(lista_dos_cursos, arquivo)     
        # adiciona um novo curso se o arquivo Json estiver vazio
        except:
            lista_dos_cursos = []
            with open(caminho + '/cursos.json', 'w+', encoding='UTF-8') as arquivo:
                lista_dos_cursos.append(vars(curso))
                json.dump(lista_dos_cursos, arquivo)

    ''' 
        Este método de instância busca os clientes já cadastrados na 
        "base de dados" e adiciona o novo cliente que está sendo cadastrado
    '''
    def add_clientes_json(self, cliente):
        # Tenta ler o arquiso Json se não estiver vazio
        try:
            with open(caminho + '/clientes.json', 'r', encoding='UTF-8') as arquivo:
                lista_dos_clientes = json.load(arquivo)
                lista_dos_clientes.append(vars(cliente))

                print(lista_dos_clientes)
        
            with open(caminho + '/clientes.json', 'w+', encoding='UTF-8') as arquivo:
                json.dump(lista_dos_clientes, arquivo)     
        # adiciona um cliente gerente se o arquivo Json estiver vazio
        except:
            lista_dos_clientes = []
            with open(caminho + '/clientes.json', 'w+', encoding='UTF-8') as arquivo:
                lista_dos_clientes.append(vars(cliente))
                json.dump(lista_dos_clientes, arquivo)

