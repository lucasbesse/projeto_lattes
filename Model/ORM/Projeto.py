from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Projeto(Base):
    __tablename__ = 'projeto'

    codigo = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String)
    descricao = Column(String)
    data_inicio = Column(String)
    data_final = Column(String)
    palavras_chave = Column(String)

    def __init__(self, titulo=None, descricao=None, data_inicio=None, data_final=None, palavras_chave=None):
        self.titulo = titulo
        self.descricao = descricao
        self.data_inicio = data_inicio
        self.data_final = data_final
        self.palavras_chave = palavras_chave
        self.codigo = None

    def __str__(self):
        return f"Titulo: {self.titulo}, Descrição: {self.descricao}, Código: {self.codigo}"
