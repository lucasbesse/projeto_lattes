from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Resultado(Base):
    __tablename__ = 'resultado'

    codigo = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String)
    descricao = Column(Text)
    tipo = Column(String)
    # autores = Column(String)
    # colaboradores = Column(String)
    # projeto = Column(String)

    def __init__(self, titulo, descricao, tipo):
                 # autores, colaboradores, projeto):
        self.titulo = titulo
        self.descricao = descricao
        self.tipo = tipo
        # self.autores = autores
        # self.colaboradores = colaboradores
        # self.projeto = projeto
        self.codigo = None

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_descricao(self):
        return self.descricao

    def set_descricao(self, descricao):
        self.descricao = descricao

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_autores(self):
        return self.autores

    def set_autores(self, autores):
        self.autores = autores

    def get_colaboradores(self):
        return self.colaboradores

    def set_colaboradores(self, colaboradores):
        self.colaboradores = colaboradores

    def get_projeto(self):
        return self.projeto

    def set_projeto(self, projeto):
        self.projeto = projeto

    def get_codigo(self):
        return self.codigo

    def __str__(self):
        return f"Título: {self.titulo}, Descrição: {self.descricao}, Código: {self.codigo}"
