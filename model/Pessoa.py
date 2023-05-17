class Pessoa:
    def __init__(self, nome):
        self._nome = nome
        self._codigo = None

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_codigo(self):
        return self._codigo

    def __str__(self):
        return f"Nome: {self._nome}, Código: {self._codigo}"

