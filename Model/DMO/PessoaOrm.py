from Model.ORM.Pessoa import Pessoa


class PessoaOrm:
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
        print(pessoa)
        if pessoa:
            self.banco.session.delete(pessoa)
            self.banco.session.commit()
            return True
        return False

    def update(self, pessoa_codigo, nome="", codigo="", email="", formacao="", experiencia=""):
        pessoa = self.banco.session.query(Pessoa).get(pessoa_codigo)
        if pessoa:
            if codigo:
                pessoa.set_codigo(codigo)
            if nome:
                pessoa.set_nome(nome)
            if email:
                pessoa.set_email(email)
            if formacao:
                pessoa.set_formacao(formacao)
            if experiencia:
                pessoa.set_experiencia(experiencia)

            self.banco.session.commit()
            return True
        return False
