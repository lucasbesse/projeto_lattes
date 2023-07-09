from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Pessoa(Base):
    __tablename__ = 'pessoa'

    codigo = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    email = Column(String)
    formacao = Column(String)
    experiencia = Column(String)

    def __init__(self, nome=None, email=None, formacao=None, experiencia=None):
        self.codigo = None
        self.nome = nome
        self.email = email
        self.formacao = formacao
        self.experiencia = experiencia

    def __str__(self):
        return f"Nome: {self.nome}, Código: {self.codigo}"
