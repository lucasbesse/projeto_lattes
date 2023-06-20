from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Projeto(Base):
    __tablename__ = 'projeto'

    codigo = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String)
    descricao = Column(String)
    # integrantes = Column(String)
    # pesquisadores = Column(String)
    # resultado = Column(String)

    def __init__(self, titulo, descricao):
        # , integrantes, pesquisadores, resultado):
        self.titulo = titulo
        self.descricao = descricao
        # self.integrantes = integrantes
        # self.pesquisadores = pesquisadores
        # self.resultado = resultado
        self.codigo = None

    def get_descricao(self):
        return self.descricao

    def set_descricao(self, descricao):
        self.descricao = descricao

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_integrantes(self):
        return self.integrantes

    def set_integrantes(self, integrantes):
        self.integrantes = integrantes

    def get_pesquisadores(self):
        return self.pesquisadores

    def set_pesquisadores(self, pesquisadores):
        self.pesquisadores = pesquisadores

    def get_resultado(self):
        return self.resultado

    def set_resultado(self, resultado):
        self.resultado = resultado

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def __str__(self):
        return f"Titulo: {self.titulo}, Descrição: {self.descricao}, Código: {self.codigo}"
