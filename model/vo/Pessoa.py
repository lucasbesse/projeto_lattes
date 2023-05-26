from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Pessoa(Base):
    __tablename__ = 'pessoa'

    codigo = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)

    def __init__(self, nome, codigo=None):
        self.nome = nome
        self.codigo = codigo

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_codigo(self):
        return self.codigo

    def _set_codigo(self, codigo):
        self.codigo = codigo

    def __str__(self):
        return f"Nome: {self.nome}, Código: {self.codigo}"

