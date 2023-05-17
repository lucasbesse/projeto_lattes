class Pessoa:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.codigo = None

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_codigo(self):
        return self.codigo

    def __str__(self):
        return f"Nome: {self.nome}, tipo: {self.tipo}, Código: {self.codigo}"

