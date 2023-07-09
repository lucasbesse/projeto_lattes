from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from Model.ORM.Projeto import Projeto

Base = declarative_base()


class Resultado(Base):
    __tablename__ = 'resultado'

    codigo = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String)
    descricao = Column(Text)
    tipo = Column(String)
    projeto_codigo = Column(Integer, ForeignKey(Projeto.codigo))

    def __init__(self, titulo=None, descricao=None, tipo=None, projeto_codigo=None):
        self.titulo = titulo
        self.descricao = descricao
        self.tipo = tipo
        self.projeto_codigo = projeto_codigo
        self.codigo = None

    def __str__(self):
        return f"Título: {self.titulo}, Descrição: {self.descricao}, Código: {self.codigo}"
