import json
import requests


def teste_criar():
    print('======= CREATE =========')
    # Endpoint para criar uma projeto
    url_criar_projeto = 'http://localhost:5000/projetos'
    # data_criar_projeto = {
    #     'nome': 'João',
    #     'idade': 30,
    #     'email': 'joao@example.com'
    # }
    # data_criar_projeto = {
    #     'nome': 'João',
    #     'email': 'abcd@email.com',
    #     'experiencia': 'nenhuma',
    #     'formacao': 'youtube'
    # }
    # data_criar_projeto = {
    #     'nome': 'João',
    #     'email': 'abcd@email.com',
    #     'experiencia': 'nenhuma'
    # }
    data_criar_projeto = {"titulo": "Projeto de teste 1",
                          "descricao":"Projeto de teste",
                          "pessoas": [{'codigo': 1, 'tipo': 'i'},
                                      {'codigo': 2, 'tipo': 'i'},
                                      {'codigo': 3, 'tipo': 'p'}],
                          "data_inicio":"2023-10-01",
                          "data_final":"2023-10-01",
                          "palavras_chave":"#TECNOLOGIA; #DESENVOLVIMENTO; #ADS"
                          }
    # data_criar_projeto = json.dumps(data_criar_projeto)
    print(type(data_criar_projeto), data_criar_projeto)
    response = requests.post(url_criar_projeto, json=data_criar_projeto)
    print(response.status_code)
    print(json.dumps(response.json(), indent=4))


def teste_ler_codigo():
    print('======= READ CODIGO =========')
    # Endpoint para ler uma projeto por código
    codigo = 1
    url_ler_projeto_codigo = f'http://localhost:5000/projetos/{codigo}'
    response = requests.get(url_ler_projeto_codigo)
    print(response.status_code)
    print(json.dumps(response.json(), indent=4))


def teste_ler():
    print('=========== READ ============')
    # Endpoint para ler projetos com paginação
    url_ler_projeto_pagina = 'http://localhost:5000/projetos?limit=10&offset=0'
    response = requests.get(url_ler_projeto_pagina)
    print(response.status_code)
    print(json.dumps(response.json(), indent=4))


def teste_atualiza():
    print('======= UPDATE =========')
    # Endpoint para atualizar uma projeto
    codigo = 28
    url_atualizar_projeto = f'http://localhost:5000/projetos/{codigo}'
    # data_atualizar_projeto = {"pessoas": [{'codigo': 1, 'tipo': 'a'},
    #                                       {'codigo': 2, 'tipo': 'a'},
    #                                       {'codigo': 3, 'tipo': 'a'}]}
    data_atualizar_projeto = {"data_final":"2023-10-07"}
    response = requests.put(url_atualizar_projeto, json=data_atualizar_projeto)
    print(response.status_code)
    print(json.dumps(response.json(), indent=4))


def teste_delete():
    print('======= DELETE =========')
    # Endpoint para deletar uma projeto
    codigo = 9
    url_deletar_projeto = f'http://127.0.0.1:5000/projetos/{codigo}'
    response = requests.delete(url_deletar_projeto)
    print(response.status_code)
    print(json.dumps(response.json(), indent=4))


# teste_criar()
# teste_ler_codigo()
teste_atualiza()
# teste_ler_codigo()
# teste_delete()
teste_ler()
