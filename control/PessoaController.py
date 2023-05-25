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

    def criar_pessoa(self, json_data):

        self._create_pessoa_bo.execute(json_data)

    def ler_pessoa_codigo(self, codigo):
        return self._read_pessoa_codigo_bo.execute(codigo=codigo)

    def ler_pessoa_pagina(self, limit, offset):
        return self._read_pessoa_pagina_bo.execute(limit=limit, offset=offset)

    def atualizar_pessoa(self, codigo, json_data):
        return self._update_pessoa_bo.execute(codigo, json_data)

    def deletar_pessoa(self, codigo):
        return self._delete_pessoa_bo.execute(codigo)