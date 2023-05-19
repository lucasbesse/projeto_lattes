

class PessoaController:
    def __init__(self, create_pessoa_use_case,
                 read_pessoa_codigo_use_case,
                 read_pessoa_pagina_use_case,
                 update_pessoa_use_case,
                 delete_pessoa_use_case):
        self._create_pessoa_use_case = create_pessoa_use_case
        self._read_pessoa_codigo_use_case = read_pessoa_codigo_use_case
        self._read_pessoa_pagina_use_case = read_pessoa_pagina_use_case
        self._update_pessoa_use_case = update_pessoa_use_case
        self._delete_pessoa_use_case = delete_pessoa_use_case

    def criar_pessoa(self, json_data):
        self._create_pessoa_use_case.execute(json_data)

    def ler_pessoa_codigo(self, codigo):
        return self._read_pessoa_codigo_use_case.execute(codigo=codigo)

    def ler_pessoa_pagina(self, limit, offset):
        return self._read_pessoa_pagina_use_case.execute(limit=limit, offset=offset)

    def atualizar_pessoa(self, codigo, json_data):
        return self._update_pessoa_use_case.execute(codigo, json_data)

    def deletar_pessoa(self, codigo):
        return self._delete_pessoa_use_case.execute(codigo)