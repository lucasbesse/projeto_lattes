class Resultado:
    def __init__(self, descricao, nome, codigo):
        self._nome = nome
        self._descricao = descricao
        self._codigo = None

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_descricao(self):
        return self._descricao

    def set_descricao(self, descricao):
        self._descricao = descricao

    def get_codigo(self):
        return self._codigo

    def __str__(self):
        return f"Nome: {self._nome}, descricao: {self._descricao}, Código: {self._codigo}"

