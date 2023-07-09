from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from Model.ORM.Pessoa import Pessoa
from Model.ORM.Projeto import Projeto

Base = declarative_base()


class ProjetoPessoa(Base):
    __tablename__ = 'projeto_pessoa'

    codigo = Column(Integer, primary_key=True, autoincrement=True)
    pessoa_codigo = Column(Integer, ForeignKey(Pessoa.codigo))
    projeto_codigo = Column(Integer, ForeignKey(Projeto.codigo))
    tipo = Column(String)

    def __init__(self, projeto, pessoa, tipo):
        self.projeto_codigo = projeto
        self.pessoa_codigo = pessoa
        self.tipo = tipo
        self.codigo = None