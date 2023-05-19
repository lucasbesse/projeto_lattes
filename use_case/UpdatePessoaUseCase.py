import json


class UpdatePessoaUseCase:
    def __init__(self, pessoa_repository):
        self._pessoa_repository = pessoa_repository

    def execute(self, codigo_pessoa, json_data):
        # Converter o JSON para um dicionário Python
        data_dict = json.loads(json_data)

        # Lista de chaves válidas
        chaves_aceitas = ['nome']

        # Percorrer as chaves e criar variáveis apenas para as chaves aceitas
        for key in data_dict:
            if key in chaves_aceitas:
                locals()[key] = data_dict[key]

        if 'nome' in locals():
            # print(locals())
            # print(locals()['nome'])
            self._pessoa_repository.update(codigo_pessoa, novo_nome=locals()['nome'])
