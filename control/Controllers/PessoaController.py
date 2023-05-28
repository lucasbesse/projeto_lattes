import json

from flask import jsonify

from control.Schemas.PessoaSchema import PessoaSchema


class PessoaController:
    def __init__(self, create_pessoa_bo,
                 read_pessoa_codigo_bo,
                 read_pessoa_pagina_bo,
                 update_pessoa_bo,
                 delete_pessoa_bo):
        self._create_pessoa_bo = create_pessoa_bo
        self._read_pessoa_codigo_bo = read_pessoa_codigo_bo
        self._read_pessoa_pagina_bo = read_pessoa_pagina_bo
        self._update_pessoa_bo = update_pessoa_bo
        self._delete_pessoa_bo = delete_pessoa_bo

        self.pessoa_schema = PessoaSchema()

    def criar_pessoa(self, json_data):
        if not json_data:
            return jsonify({'error': 'Dados JSON ausentes'}), 400

        # Validar campos obrigatórios
        errors = self.pessoa_schema.validate(json.loads(json_data))

        if errors:
            return jsonify({'error': errors}), 400

        # Executar ação do Business Object
        try:
            pessoa = self.pessoa_schema.load(json.loads(json_data))
            pessoa_id = self._create_pessoa_bo.execute(pessoa)
            return jsonify({'success': 'Pessoa criada com sucesso', 'id': pessoa_id}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def ler_pessoa_codigo(self, codigo):
        pessoa = self._read_pessoa_codigo_bo.execute(codigo)
        if pessoa:
            pessoa_json = self.pessoa_schema.dump(pessoa)
            return jsonify(pessoa_json), 200
        else:
            return jsonify({'error': 'Pessoa não encontrada'}), 404

    def ler_pessoa_pagina(self, limit, offset):

        if limit > 200:
            limit = 200

        pessoas = self._read_pessoa_pagina_bo.execute(limit, offset)
        pessoas_json = self.pessoa_schema.dump(pessoas, many=True)
        return jsonify(pessoas_json), 200

    def atualizar_pessoa(self, codigo, json_data):
        if not json_data:
            return jsonify({'error': 'Dados JSON ausentes'}), 400

        # Validar campos obrigatórios
        errors = self.pessoa_schema.validate(json.loads(json_data))
        if errors:
            return jsonify({'error': errors}), 400

        # Executar ação do Business Object
        try:
            print(json_data)
            pessoa = self.pessoa_schema.load(json.loads(json_data))
            print(pessoa)
            success = self._update_pessoa_bo.execute(codigo, pessoa)
            if success:
                return jsonify({'success': 'Pessoa atualizada com sucesso'}), 200
            else:
                return jsonify({'error': 'Pessoa não encontrada'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def deletar_pessoa(self, codigo):
        success = self._delete_pessoa_bo.execute(codigo)
        if success:
            return jsonify({'success': 'Pessoa deletada com sucesso'}), 200
        else:
            return jsonify({'error': 'Pessoa não encontrada'}), 404


