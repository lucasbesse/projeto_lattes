from Model.ORM.ProjetoPessoa import ProjetoPessoa


class ProjetoPessoaDmo:
    def __init__(self, banco):
        # Configuração da conexão com o banco de dados
        self.banco = banco

    def add(self, projeto_pessoa):
        self.banco.session.add(projeto_pessoa)
        self.banco.session.commit()
        self.banco.session.refresh(projeto_pessoa)
        return projeto_pessoa.codigo

    def read_projeto_pessoa(self, projeto_id):
        projeto_pessoa = self.banco.session.query(ProjetoPessoa).filter(
            ProjetoPessoa.projeto_codigo == projeto_id).all()
        if projeto_pessoa:
            return projeto_pessoa
        return False

    def remove(self, codigo_projeto):
        self.banco.engine.execute(f'delete from projeto_pessoa where projeto_codigo = {codigo_projeto}')
        self.banco.session.commit()
        return True
