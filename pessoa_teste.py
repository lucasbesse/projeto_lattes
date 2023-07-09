import requests


def teste_criar():
    print('======= CREATE =========')
    # Endpoint para criar uma pessoa
    url_criar_pessoa = 'http://localhost:5000/pessoas'
    # data_criar_pessoa = {
    #     'nome': 'João',
    #     'idade': 30,
    #     'email': 'joao@example.com'
    # }
    # data_criar_pessoa = {
    #     'nome': 'João',
    #     'email': 'abcd@email.com',
    #     'experiencia': 'nenhuma',
    #     'formacao': 'youtube'
    # }
    # data_criar_pessoa = {
    #     'nome': 'João',
    #     'email': 'abcd@email.com',
    #     'experiencia': 'nenhuma'
    # }
    data_criar_pessoa = {"nome": "João", "email": "abcd@email.com", "experiencia": "nenhuma"}
    # data_criar_pessoa = json.dumps(data_criar_pessoa)
    print(type(data_criar_pessoa), data_criar_pessoa)
    response = requests.post(url_criar_pessoa, json=data_criar_pessoa)
    print(response.status_code)
    print(response.text)


def teste_ler_codigo():
    print('======= READ CODIGO =========')
    # Endpoint para ler uma pessoa por código
    codigo = 40
    url_ler_pessoa_codigo = f'http://localhost:5000/pessoas/{codigo}'
    response = requests.get(url_ler_pessoa_codigo)
    print(response.status_code)
    print(response.json())


def teste_ler():
    print('=========== READ ============')
    # Endpoint para ler pessoas com paginação
    url_ler_pessoa_pagina = 'http://localhost:5000/pessoas?limit=10&offset=0'
    response = requests.get(url_ler_pessoa_pagina)
    print(response.status_code)
    print(response.json())


def teste_atualiza():
    print('======= UPDATE =========')
    # Endpoint para atualizar uma pessoa
    codigo = 6
    url_atualizar_pessoa = f'http://localhost:5000/pessoas/{codigo}'
    data_atualizar_pessoa = {
        'nome': 'João e o Pé de Feijão',
        'experiencia': 'alguma',
        'formacao': 'pra que?'
    }
    response = requests.put(url_atualizar_pessoa, json=data_atualizar_pessoa)
    print(response.status_code)
    print(response.json())


def teste_delete():
    print('======= DELETE =========')
    # Endpoint para deletar uma pessoa
    codigo = 9
    url_deletar_pessoa = f'http://127.0.0.1:5000/pessoas/{codigo}'
    response = requests.delete(url_deletar_pessoa)
    print(response.status_code)
    print(response.json())


teste_criar()
# teste_ler_codigo()
# teste_atualiza()
# teste_ler_codigo()
# teste_delete()
teste_ler()