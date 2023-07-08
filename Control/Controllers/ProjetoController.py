import json

from flask import jsonify
from flask import make_response

from Model.Schemas.PessoaSchema import PessoaSchema
from Model.Schemas.ProjetoPessoaSchema import ProjetoPessoaSchema
from Model.Schemas.ProjetoPessoaSchemaRead import ProjetoPessoaSchemaRead
from Model.Schemas.ProjetoSchema import ProjetoSchema
from Model.Schemas.ProjetoUpdateSchema import ProjetoUpdateSchema


class ProjetoController:
    def __init__(self, projeto_create_bo,
                 projeto_read_codigo_bo,
                 projeto_read_pagina_bo,
                 projeto_update_bo,
                 projeto_delete_bo,
                 projeto_pessoa_create_bo,
                 projeto_pessoa_read_bo,
                 read_pessoa_codigo_bo):

        self.projeto_create_bo = projeto_create_bo
        self.projeto_read_codigo_bo = projeto_read_codigo_bo
        self.projeto_read_pagina_bo = projeto_read_pagina_bo
        self.projeto_update_bo = projeto_update_bo
        self.projeto_delete_bo = projeto_delete_bo
        self.projeto_pessoa_create_bo = projeto_pessoa_create_bo
        self.projeto_pessoa_read_bo = projeto_pessoa_read_bo
        self.read_pessoa_codigo_bo = read_pessoa_codigo_bo
        self.projeto_schema = ProjetoSchema()
        self.projeto_pessoa_schema_read = ProjetoPessoaSchemaRead()
        self.projeto_update_schema = ProjetoUpdateSchema()
        self.pessoa_schema = PessoaSchema()

    def criar_projeto(self, json_data):
        if not json_data:
            print('nao tem json')
            response = make_response(jsonify({'error': 'Dados JSON ausentes'}), 400)
            return response

        # pessoas
        json_data = json.loads(json_data)
        pessoas = json_data.pop("pessoas") if "pessoas" in json_data else None

        # Validar campos obrigatórios
        errors = self.projeto_schema.validate(json_data)

        if errors:
            response = make_response(jsonify({'error': errors}), 400)
            return response

        # Executar ação do Business Object
        try:
            projeto = self.projeto_schema.load(json_data)
            projeto_id = self.projeto_create_bo.execute(projeto)

            if pessoas:
                self.projeto_pessoa_create_bo.execute(projeto_id, pessoas)

            response = make_response(jsonify({'success': 'Projeto criada com sucesso', 'id': projeto_id}), 201)
            response.headers['Access-Control-Allow-Origin'] = '*'

            return response
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def ler_projeto_codigo(self, codigo):
        projeto = self.projeto_read_codigo_bo.execute(codigo)
        if projeto:
            projeto_json = self.projeto_schema.dump(projeto)
            projeto_json['pessoas'] = []

            list_projeto_pessoa = self.projeto_pessoa_read_bo.execute(codigo)
            if list_projeto_pessoa:
                list_projeto_pessoa_json = self.projeto_pessoa_schema_read.dump(list_projeto_pessoa, many=True)
                print(list_projeto_pessoa_json)
                pessoas_list = []
                for projeto_pessoa in list_projeto_pessoa_json:
                    pessoa = self.read_pessoa_codigo_bo.execute(projeto_pessoa['pessoa_codigo'])
                    pessoa_json = self.pessoa_schema.dump(pessoa)
                    projeto_pessoa['pessoa'] = pessoa_json
                    projeto_pessoa.pop('pessoa_codigo')
                    pessoas_list.append(projeto_pessoa)

                projeto_json['pessoas'] = pessoas_list
            return jsonify(projeto_json), 200
        else:
            return jsonify({'error': 'Projeto não encontrada'}), 404

    def ler_projeto_pagina(self, limit, offset):

        if limit > 200:
            limit = 200

        projetos = self.projeto_read_pagina_bo.execute(limit, offset)
        projetos_json = self.projeto_schema.dump(projetos, many=True)

        if projetos:

            for projeto_json in projetos_json:
                projeto_json['pessoas'] = []

                list_projeto_pessoa = self.projeto_pessoa_read_bo.execute(projeto_json['codigo'])
                if list_projeto_pessoa:
                    list_projeto_pessoa_json = self.projeto_pessoa_schema_read.dump(list_projeto_pessoa, many=True)
                    print(list_projeto_pessoa_json)
                    pessoas_list = []
                    for projeto_pessoa in list_projeto_pessoa_json:
                        pessoa = self.read_pessoa_codigo_bo.execute(projeto_pessoa['pessoa_codigo'])
                        pessoa_json = self.pessoa_schema.dump(pessoa)
                        projeto_pessoa['pessoa'] = pessoa_json
                        projeto_pessoa.pop('pessoa_codigo')
                        pessoas_list.append(projeto_pessoa)

                    projeto_json['pessoas'] = pessoas_list

        response = make_response(jsonify(projetos_json), 200)
        response.headers['Access-Control-Allow-Origin'] = '*'

        return response

    def atualizar_projeto(self, codigo, json_data):
        if not json_data:
            return jsonify({'error': 'Dados JSON ausentes'}), 400

        # pessoas
        json_data = json.loads(json_data)
        pessoas = json_data.pop("pessoas") if "pessoas" in json_data else None

        # Validar campos obrigatórios
        errors = self.projeto_update_schema.validate(json_data)
        if errors:
            return jsonify({'error': errors}), 400

        # Executar ação do Business Object
        try:
            # print(json_data)
            projeto = self.projeto_update_schema.load(json_data)
            success = self.projeto_update_bo.execute(codigo, projeto)

            if pessoas:
                self.projeto_pessoa_create_bo.execute(codigo, pessoas)

            if success:
                return jsonify({'success': 'Projeto atualizada com sucesso'}), 200
            else:
                return jsonify({'error': 'Projeto não encontrada'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def deletar_projeto(self, codigo):
        success = self.projeto_delete_bo.execute(codigo)
        if success:
            return jsonify({'success': 'Projeto deletada com sucesso'}), 200
        else:
            return jsonify({'error': 'Projeto não encontrada'}), 404
