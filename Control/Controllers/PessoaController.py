import json

from flask import jsonify
from flask import make_response

from Model.Schemas.PessoaSchema import PessoaSchema
from Model.Schemas.PessoaUpdateSchema import PessoaUpdateSchema
from Model.Schemas.ProjetoPessoaSchemaRead import ProjetoPessoaSchemaRead
from Model.Schemas.ProjetoSchema import ProjetoSchema
from Model.Schemas.ResultadoPessoaSchemaRead import ResultadoPessoaSchemaRead
from Model.Schemas.ResultadoSchema import ResultadoSchema


class PessoaController:
    def __init__(self, pessoa_create_bo,
                 pessoa_read_codigo_bo,
                 pessoa_read_pagina_bo,
                 pessoa_update_bo,
                 pessoa_delete_bo,
                 projeto_pessoa_read_p_id_bo,
                 resultado_pessoa_read_p_id_bo,
                 projeto_read_codigo_bo,
                 resultado_read_codigo_bo):

        self.pessoa_create_bo = pessoa_create_bo
        self.pessoa_read_codigo_bo = pessoa_read_codigo_bo
        self.pessoa_read_pagina_bo = pessoa_read_pagina_bo
        self.pessoa_update_bo = pessoa_update_bo
        self.pessoa_delete_bo = pessoa_delete_bo
        self.resultado_pessoa_read_p_id_bo = resultado_pessoa_read_p_id_bo
        self.projeto_pessoa_read_p_id_bo = projeto_pessoa_read_p_id_bo
        self.projeto_read_codigo_bo = projeto_read_codigo_bo
        self.resultado_read_codigo_bo = resultado_read_codigo_bo

        self.resultado_pessoa_schema_read = ResultadoPessoaSchemaRead()
        self.resultado_schema = ResultadoSchema()
        self.projeto_schema = ProjetoSchema()
        self.pessoa_schema = PessoaSchema()
        self.pessoa_update_schema = PessoaUpdateSchema()
        self.projeto_pessoa_schema_read = ProjetoPessoaSchemaRead()

    def criar_pessoa(self, json_data):
        if not json_data:
            response = make_response(jsonify({'error': 'Dados JSON ausentes'}), 400)
            return response
        # Validar campos obrigatórios
        errors = self.pessoa_schema.validate(json.loads(json_data))

        if errors:
            response = make_response(jsonify({'error': errors}), 400)
            return response

        # Executar ação do Business Object
        try:
            pessoa = self.pessoa_schema.load(json.loads(json_data))
            pessoa_id = self.pessoa_create_bo.execute(pessoa)

            response = make_response(jsonify({'success': 'Pessoa criada com sucesso', 'id': pessoa_id}), 201)
            response.headers['Access-Control-Allow-Origin'] = '*'

            return response
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def ler_pessoa_codigo(self, codigo):
        pessoa = self.pessoa_read_codigo_bo.execute(codigo)
        if pessoa:
            pessoa_json = self.pessoa_schema.dump(pessoa)
            return jsonify(pessoa_json), 200
        else:
            return jsonify({'error': 'Pessoa não encontrada'}), 404

    def ler_pessoa_pagina(self, limit, offset):

        if limit > 200:
            limit = 200

        pessoas = self.pessoa_read_pagina_bo.execute(limit, offset)
        pessoas_json = self.pessoa_schema.dump(pessoas, many=True)

        for pessoa_json in pessoas_json:
            pessoa_json['projetos'] = []

            list_projeto_pessoa = self.projeto_pessoa_read_p_id_bo.execute(pessoa_json['codigo'])
            if list_projeto_pessoa:
                list_projeto_pessoa_json = self.projeto_pessoa_schema_read.dump(list_projeto_pessoa, many=True)
                print("entrou")
                projetos_list = []
                for projeto_pessoa in list_projeto_pessoa_json:
                    projeto = self.projeto_read_codigo_bo.execute(projeto_pessoa['projeto_codigo'])
                    projeto_json = self.projeto_schema.dump(projeto)
                    projetos_list.append(projeto_json)

                pessoa_json['projetos'] = projetos_list

            pessoa_json['resultados'] = []

            list_resultado_pessoa = self.resultado_pessoa_read_p_id_bo.execute(pessoa_json['codigo'])
            if list_resultado_pessoa:
                list_resultado_pessoa_json = self.resultado_pessoa_schema_read.dump(list_resultado_pessoa, many=True)

                resultados_list = []
                for resultado_pessoa in list_resultado_pessoa_json:
                    resultado = self.resultado_read_codigo_bo.execute(resultado_pessoa['resultado_codigo'])
                    resultado_json = self.resultado_schema.dump(resultado)
                    resultados_list.append(resultado_json)

                pessoa_json['resultados'] = resultados_list

        response = make_response(jsonify(pessoas_json), 200)
        response.headers['Access-Control-Allow-Origin'] = '*'

        return response

    def atualizar_pessoa(self, codigo, json_data):
        if not json_data:
            return jsonify({'error': 'Dados JSON ausentes'}), 400

        # Validar campos obrigatórios
        errors = self.pessoa_update_schema.validate(json.loads(json_data))
        if errors:
            return jsonify({'error': errors}), 400

        # Executar ação do Business Object
        try:

            pessoa = self.pessoa_update_schema.load(json.loads(json_data))
            success = self.pessoa_update_bo.execute(codigo, pessoa)
            if success:
                return jsonify({'success': 'Pessoa atualizada com sucesso'}), 200
            else:
                return jsonify({'error': 'Pessoa não encontrada'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def deletar_pessoa(self, codigo):
        success = self.pessoa_delete_bo.execute(codigo)
        if success:
            return jsonify({'success': 'Pessoa deletada com sucesso'}), 200
        else:
            return jsonify({'error': 'Pessoa não encontrada'}), 404
