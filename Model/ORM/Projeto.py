from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Projeto(Base):
    __tablename__ = 'projeto'

    codigo = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String)
    descricao = Column(String)
    # resultado = Column(String)

    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
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

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def __str__(self):
        return f"Titulo: {self.titulo}, Descrição: {self.descricao}, Código: {self.codigo}"
