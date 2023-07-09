from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Projeto(Base):
    __tablename__ = 'projeto'

    codigo = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String)
    descricao = Column(String)

    def __init__(self, titulo=None, descricao=None):
        self.titulo = titulo
        self.descricao = descricao
        self.codigo = None

    def __str__(self):
        return f"Titulo: {self.titulo}, Descrição: {self.descricao}, Código: {self.codigo}"
