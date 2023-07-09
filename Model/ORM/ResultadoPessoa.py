from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from Model.ORM.Pessoa import Pessoa
from Model.ORM.Resultado import Resultado

Base = declarative_base()


class ResultadoPessoa(Base):
    __tablename__ = 'resultado_pessoa'

    codigo = Column(Integer, primary_key=True, autoincrement=True)
    pessoa_codigo = Column(Integer, ForeignKey(Pessoa.codigo))
    resultado_codigo = Column(Integer, ForeignKey(Resultado.codigo))
    tipo = Column(String)

    def __init__(self, resultado, pessoa, tipo):
        self.resultado_codigo = resultado
        self.pessoa_codigo = pessoa
        self.tipo = tipo
        self.codigo = None