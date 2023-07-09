import json
import requests


def teste_criar():
    print('======= CREATE =========')
    # Endpoint para criar uma resultado
    url_criar_resultado = 'http://localhost:5000/resultados'
    # data_criar_resultado = {
    #     'nome': 'João',
    #     'idade': 30,
    #     'email': 'joao@example.com'
    # }
    # data_criar_resultado = {
    #     'nome': 'João',
    #     'email': 'abcd@email.com',
    #     'experiencia': 'nenhuma',
    #     'formacao': 'youtube'
    # }
    # data_criar_resultado = {
    #     'nome': 'João',
    #     'email': 'abcd@email.com',
    #     'experiencia': 'nenhuma'
    # }
    data_criar_resultado = {"titulo": "A era das flores",
                            "descricao": "Filme sobre independência cognitiva",
                            "tipo": "Produçao audiovisual",
                            "pessoas": [{'codigo': 1, 'tipo': 'a'},
                                        {'codigo': 2, 'tipo': 'a'},
                                        {'codigo': 3, 'tipo': 'i'}]
                            }
    # data_criar_resultado = json.dumps(data_criar_resultado)
    print(type(data_criar_resultado), data_criar_resultado)
    response = requests.post(url_criar_resultado, json=data_criar_resultado)
    print(response.status_code)
    print(json.dumps(response.json(), indent=4))


def teste_ler_codigo():
    print('======= READ CODIGO =========')
    # Endpoint para ler uma resultado por código
    codigo = 1
    url_ler_resultado_codigo = f'http://localhost:5000/resultados/{codigo}'
    response = requests.get(url_ler_resultado_codigo)
    print(response.status_code)
    print(json.dumps(response.json(), indent=4))


def teste_ler():
    print('=========== READ ============')
    # Endpoint para ler resultados com paginação
    url_ler_resultado_pagina = 'http://localhost:5000/resultados?limit=10&offset=0'
    response = requests.get(url_ler_resultado_pagina)
    print(response.status_code)
    print(json.dumps(response.json(), indent=4))


def teste_atualiza():
    print('======= UPDATE =========')
    # Endpoint para atualizar uma resultado
    codigo = 1
    url_atualizar_resultado = f'http://localhost:5000/resultados/{codigo}'
    # data_atualizar_resultado = {"pessoas": [{'codigo': 1, 'tipo': 'a'},
    #                                       {'codigo': 2, 'tipo': 'a'},
    #                                       {'codigo': 3, 'tipo': 'a'}]}
    data_atualizar_resultado = {"pessoas": [{'codigo': 1, 'tipo': 'b'}]}
    response = requests.put(url_atualizar_resultado, json=data_atualizar_resultado)
    print(response.status_code)
    print(json.dumps(response.json(), indent=4))


def teste_delete():
    print('======= DELETE =========')
    # Endpoint para deletar uma resultado
    codigo = 9
    url_deletar_resultado = f'http://127.0.0.1:5000/resultados/{codigo}'
    response = requests.delete(url_deletar_resultado)
    print(response.status_code)
    print(json.dumps(response.json(), indent=4))


teste_criar()
# teste_ler_codigo()
teste_atualiza()
# teste_ler_codigo()
# teste_delete()
teste_ler()
