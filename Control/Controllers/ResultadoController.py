import json

from flask import jsonify
from flask import make_response

from Model.Schemas.PessoaSchema import PessoaSchema
from Model.Schemas.ProjetoPessoaSchemaRead import ProjetoPessoaSchemaRead
from Model.Schemas.ProjetoSchema import ProjetoSchema
from Model.Schemas.ResultadoPessoaSchemaRead import ResultadoPessoaSchemaRead
from Model.Schemas.ResultadoSchema import ResultadoSchema
from Model.Schemas.ResultadoUpdateSchema import ResultadoUpdateSchema


class ResultadoController:
    def __init__(self, resultado_create_bo,
                 resultado_read_codigo_bo,
                 resultado_read_pagina_bo,
                 resultado_update_bo,
                 resultado_delete_bo,
                 resultado_pessoa_create_bo,
                 resultado_pessoa_read_bo,
                 pessoa_read_codigo_bo,
                 projeto_read_codigo_bo,
                 projeto_pessoa_read_bo):

        self.resultado_create_bo = resultado_create_bo
        self.resultado_read_codigo_bo = resultado_read_codigo_bo
        self.resultado_read_pagina_bo = resultado_read_pagina_bo
        self.resultado_update_bo = resultado_update_bo
        self.resultado_delete_bo = resultado_delete_bo
        self.resultado_pessoa_create_bo = resultado_pessoa_create_bo
        self.resultado_pessoa_read_bo = resultado_pessoa_read_bo
        self.pessoa_read_codigo_bo = pessoa_read_codigo_bo
        self.projeto_read_codigo_bo = projeto_read_codigo_bo
        self.projeto_pessoa_read_bo = projeto_pessoa_read_bo

        self.resultado_schema = ResultadoSchema()
        self.resultado_update_schema = ResultadoUpdateSchema()
        self.resultado_pessoa_schema_read = ResultadoPessoaSchemaRead()
        self.pessoa_schema = PessoaSchema()

        self.projeto_schema = ProjetoSchema()

        self.projeto_pessoa_schema_read = ProjetoPessoaSchemaRead()

    def criar_resultado(self, json_data):
        json_data = json.loads(json_data)
        if not json_data:

            response = make_response(jsonify({'error': 'Dados JSON ausentes'}), 400)
            return response

        # Validar campos obrigatórios
        pessoas = json_data.pop("pessoas") if "pessoas" in json_data else None
        errors = self.resultado_schema.validate(json_data)

        if errors:
            response = make_response(jsonify({'error': errors}), 400)
            return response

        # Executar ação do Business Object
        try:
            resultado = self.resultado_schema.load(json_data)
            resultado_id = self.resultado_create_bo.execute(resultado)

            if pessoas:
                self.resultado_pessoa_create_bo.execute(resultado_id, pessoas)

            response = make_response(jsonify({'success': 'Resultado criada com sucesso', 'id': resultado_id}), 201)
            response.headers['Access-Control-Allow-Origin'] = '*'

            return response
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def ler_resultado_codigo(self, codigo):
        resultado = self.resultado_read_codigo_bo.execute(codigo)
        if resultado:
            resultado_json = self.resultado_schema.dump(resultado)

            resultado_json['pessoas'] = []

            list_resultado_pessoa = self.resultado_pessoa_read_bo.execute(resultado.codigo)
            if list_resultado_pessoa:
                list_resultado_pessoa_json = self.resultado_pessoa_schema_read.dump(list_resultado_pessoa, many=True)
                pessoas_list = []
                for resultado_pessoa in list_resultado_pessoa_json:
                    pessoa = self.pessoa_read_codigo_bo.execute(resultado_pessoa['pessoa_codigo'])
                    pessoa_json = self.pessoa_schema.dump(pessoa)
                    resultado_pessoa['pessoa'] = pessoa_json
                    resultado_pessoa.pop('pessoa_codigo')
                    pessoas_list.append(resultado_pessoa)

                resultado_json['pessoas'] = pessoas_list

            resultado_json['projeto'] = None
            projeto = self.projeto_read_codigo_bo.execute(resultado.projeto_codigo)
            if projeto:
                projeto_json = self.projeto_schema.dump(projeto)
                projeto_json['pessoas'] = []

                list_projeto_pessoa = self.projeto_pessoa_read_bo.execute(codigo)
                if list_projeto_pessoa:
                    list_projeto_pessoa_json = self.projeto_pessoa_schema_read.dump(list_projeto_pessoa, many=True)

                    pessoas_list = []
                    for projeto_pessoa in list_projeto_pessoa_json:
                        pessoa = self.pessoa_read_codigo_bo.execute(projeto_pessoa['pessoa_codigo'])
                        pessoa_json = self.pessoa_schema.dump(pessoa)
                        projeto_pessoa['pessoa'] = pessoa_json
                        projeto_pessoa.pop('pessoa_codigo')
                        pessoas_list.append(projeto_pessoa)

                    projeto_json['pessoas'] = pessoas_list

                resultado_json['projeto'] = projeto_json

            resultado_json.pop('projeto_codigo')


            return jsonify(resultado_json), 200
        else:
            return jsonify({'error': 'Resultado não encontrada'}), 404

    def ler_resultado_pagina(self, limit, offset):

        if limit > 200:
            limit = 200

        resultados = self.resultado_read_pagina_bo.execute(limit, offset)
        resultados_json = self.resultado_schema.dump(resultados, many=True)
        if resultados:

            for resultado_json in resultados_json:
                resultado_json['pessoas'] = []

                list_resultado_pessoa = self.resultado_pessoa_read_bo.execute(resultado_json['codigo'])
                if list_resultado_pessoa:
                    list_resultado_pessoa_json = self.resultado_pessoa_schema_read.dump(list_resultado_pessoa, many=True)

                    pessoas_list = []
                    for resultado_pessoa in list_resultado_pessoa_json:
                        pessoa = self.pessoa_read_codigo_bo.execute(resultado_pessoa['pessoa_codigo'])
                        pessoa_json = self.pessoa_schema.dump(pessoa)
                        resultado_pessoa['pessoa'] = pessoa_json
                        resultado_pessoa.pop('pessoa_codigo')
                        pessoas_list.append(resultado_pessoa)

                    resultado_json['pessoas'] = pessoas_list

                resultado_json['projeto'] = None
                projeto = self.projeto_read_codigo_bo.execute(resultado_json['projeto_codigo'])
                if projeto:
                    projeto_json = self.projeto_schema.dump(projeto)
                    projeto_json['pessoas'] = []

                    list_projeto_pessoa = self.projeto_pessoa_read_bo.execute(projeto.codigo)
                    if list_projeto_pessoa:
                        list_projeto_pessoa_json = self.projeto_pessoa_schema_read.dump(list_projeto_pessoa, many=True)

                        pessoas_list = []
                        for projeto_pessoa in list_projeto_pessoa_json:
                            pessoa = self.pessoa_read_codigo_bo.execute(projeto_pessoa['pessoa_codigo'])
                            pessoa_json = self.pessoa_schema.dump(pessoa)
                            projeto_pessoa['pessoa'] = pessoa_json
                            projeto_pessoa.pop('pessoa_codigo')
                            pessoas_list.append(projeto_pessoa)

                        projeto_json['pessoas'] = pessoas_list

                    resultado_json['projeto'] = projeto_json

                resultado_json.pop('projeto_codigo')

        response = make_response(jsonify(resultados_json), 200)
        response.headers['Access-Control-Allow-Origin'] = '*'

        return response

    def atualizar_resultado(self, codigo, json_data):
        if not json_data:
            return jsonify({'error': 'Dados JSON ausentes'}), 400

        json_data = json.loads(json_data)
        # Validar campos obrigatórios
        pessoas = json_data.pop("pessoas") if "pessoas" in json_data else None
        errors = self.resultado_update_schema.validate(json_data)
        if errors:
            return jsonify({'error': errors}), 400

        # Executar ação do Business Object
        try:

            resultado = self.resultado_update_schema.load(json_data)

            success = self.resultado_update_bo.execute(codigo, resultado)

            self.resultado_pessoa_create_bo.execute(codigo, pessoas)

            if success:
                return jsonify({'success': 'Resultado atualizada com sucesso'}), 200
            else:
                return jsonify({'error': 'Resultado não encontrada'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def deletar_resultado(self, codigo):
        success = self.resultado_delete_bo.execute(codigo)
        if success:
            return jsonify({'success': 'Resultado deletada com sucesso'}), 200
        else:
            return jsonify({'error': 'Resultado não encontrada'}), 404
