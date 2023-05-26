from model.vo.Pessoa import Pessoa


class PessoaDao:
    def __init__(self, banco):
        # Configuração da conexão com o banco de dados
        self.banco = banco

    def add(self, pessoa):
        self.banco.session.add(pessoa)
        self.banco.session.commit()
        return True

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

    def update(self, pessoa_id, novo_nome="", novo_codigo=""):
        pessoa = self.banco.session.query(Pessoa).get(pessoa_id)
        if pessoa:
            if novo_nome:
                pessoa.nome = novo_nome
            if novo_codigo:
                pessoa.codigo = novo_codigo
            self.banco.session.commit()
            return True
        return False
