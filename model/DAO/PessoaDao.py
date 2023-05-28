from model.DTO.Pessoa import Pessoa


class PessoaDao:
    def __init__(self, banco):
        # Configuração da conexão com o banco de dados
        self.banco = banco

    def add(self, pessoa):
        self.banco.session.add(pessoa)
        self.banco.session.commit()
        self.banco.session.refresh(pessoa)
        return pessoa.codigo

    def read_pagination(self, limit, offset):
        pessoas = self.banco.session.query(Pessoa).limit(limit).offset(offset).all()
        return pessoas

    def read_pessoa(self, pessoa_id):
        pessoa = self.banco.session.query(Pessoa).get(pessoa_id)
        if pessoa:
            return pessoa
        return False

    def remove(self, pessoa_id):
        pessoa = self.banco.session.query(Pessoa).get(pessoa_id)
        if pessoa:
            self.banco.session.delete(pessoa)
            self.banco.session.commit()
            return True
        return False

    def update(self, pessoa_codigo, nome="", codigo=""):
        pessoa = self.banco.session.query(Pessoa).get(pessoa_codigo)
        if pessoa:
            if nome:
                pessoa.nome = nome
            if codigo:
                pessoa.codigo = codigo
            self.banco.session.commit()
            return True
        return False
