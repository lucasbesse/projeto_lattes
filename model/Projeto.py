class Projeto:
    def __init__(self, descricao, nome, integrantes, pesquisadores, resultado):
        self.nome = nome
        self.descricao = descricao
        self.integrantes = integrantes
        self.pesquisadores = pesquisadores
        self.resultado = resultado
        self.codigo = None

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_descricao(self):
        return self.descricao

    def set_descricao(self, descricao):
        self.descricao = descricao

    def get_codigo(self):
        return self.codigo

    def __str__(self):
        return f"Nome: {self.nome}, tipo: {self.tipo}, Código: {self.codigo}"