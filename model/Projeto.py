class Projeto:
    def __init__(self, descricao, nome, integrantes, pesquisadores, resultado):
        self._nome = nome
        self._descricao = descricao
        self._integrantes = integrantes
        self._pesquisadores = pesquisadores
        self._resultado = resultado
        self._codigo = None

    def get_descricao(self):
        return self._descricao

    def set_descricao(self, descricao):
        self._descricao = descricao

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_integrantes(self):
        return self._integrantes

    def set_integrantes(self, integrantes):
        self._integrantes = integrantes

    def get_pesquisadores(self):
        return self._pesquisadores

    def set_pesquisadores(self, pesquisadores):
        self._pesquisadores = pesquisadores

    def get_resultado(self):
        return self._resultado

    def set_resultado(self, resultado):
        self._resultado = resultado

    def get_codigo(self):
        return self._codigo

    def set_codigo(self, codigo):
        self._codigo = codigo

    def __str__(self):
        return f"Nome: {self._nome}, Descrição: {self._descricao}, Código: {self._codigo}"
