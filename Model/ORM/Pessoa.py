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
    # projeto_pessoa_rel = relationship(ProjetoPessoa, back_populates='pessoa')

    def __init__(self, nome, email=None, formacao=None, experiencia=None, codigo=None):
        self.codigo = codigo
        self.nome = nome
        self.email = email
        self.formacao = formacao
        self.experiencia = experiencia

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_formacao(self):
        return self.formacao

    def set_formacao(self, formacao):
        self.formacao = formacao

    def get_experiencia(self):
        return self.experiencia

    def set_experiencia(self, experiencia):
        self.experiencia = experiencia

    def get_codigo(self):
        return self.codigo

    def _set_codigo(self, codigo):
        self.codigo = codigo

    def __str__(self):
        return f"Nome: {self.nome}, Código: {self.codigo}"
