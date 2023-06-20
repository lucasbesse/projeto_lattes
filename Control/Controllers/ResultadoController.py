import json

from flask import jsonify
from flask import make_response

from Model.Schemas.ResultadoSchema import ResultadoSchema
from Model.Schemas.ResultadoUpdateSchema import ResultadoUpdateSchema


class ResultadoController:
    def __init__(self, resultado_create_bo,
                 resultado_read_codigo_bo,
                 resultado_read_pagina_bo,
                 resultado_update_bo,
                 resultado_delete_bo):
        self.resultado_create_bo = resultado_create_bo
        self.resultado_read_codigo_bo = resultado_read_codigo_bo
        self.resultado_read_pagina_bo = resultado_read_pagina_bo
        self.resultado_update_bo = resultado_update_bo
        self.resultado_delete_bo = resultado_delete_bo

        self.resultado_schema = ResultadoSchema()
        self.resultado_update_schema = ResultadoUpdateSchema()

    def criar_resultado(self, json_data):
        print(type(json.loads(json_data)))
        if not json_data:
            print('nao tem json')
            response = make_response(jsonify({'error': 'Dados JSON ausentes'}), 400)
            return response
        print('tem json')
        # Validar campos obrigatórios
        errors = self.resultado_schema.validate(json.loads(json_data))

        if errors:
            response = make_response(jsonify({'error': errors}), 400)
            return response

        # Executar ação do Business Object
        try:
            resultado = self.resultado_schema.load(json.loads(json_data))
            resultado_id = self.resultado_create_bo.execute(resultado)

            response = make_response(jsonify({'success': 'Resultado criada com sucesso', 'id': resultado_id}), 201)
            response.headers['Access-Control-Allow-Origin'] = '*'

            return response
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def ler_resultado_codigo(self, codigo):
        resultado = self.resultado_read_codigo_bo.execute(codigo)
        if resultado:
            resultado_json = self.resultado_schema.dump(resultado)
            return jsonify(resultado_json), 200
        else:
            return jsonify({'error': 'Resultado não encontrada'}), 404

    def ler_resultado_pagina(self, limit, offset):

        if limit > 200:
            limit = 200

        resultados = self.resultado_read_pagina_bo.execute(limit, offset)
        resultados_json = self.resultado_schema.dump(resultados, many=True)

        response = make_response(jsonify(resultados_json), 200)
        response.headers['Access-Control-Allow-Origin'] = '*'

        return response

    def atualizar_resultado(self, codigo, json_data):
        if not json_data:
            return jsonify({'error': 'Dados JSON ausentes'}), 400

        # Validar campos obrigatórios
        errors = self.resultado_update_schema.validate(json.loads(json_data))
        if errors:
            return jsonify({'error': errors}), 400

        # Executar ação do Business Object
        try:
            # print(json_data)
            resultado = self.resultado_update_schema.load(json.loads(json_data))
            print(type(resultado),resultado)
            success = self.resultado_update_bo.execute(codigo, resultado)
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
