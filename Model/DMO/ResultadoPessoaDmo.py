from Model.ORM.ResultadoPessoa import ResultadoPessoa


class ResultadoPessoaDmo:
    def __init__(self, banco):
        # Configuração da conexão com o banco de dados
        self.banco = banco

    def add(self, resultado_pessoa):
        self.banco.session.add(resultado_pessoa)
        self.banco.session.commit()
        self.banco.session.refresh(resultado_pessoa)
        return resultado_pessoa.codigo

    def read_resultado_pessoa(self, resultado_id):
        resultado_pessoa = self.banco.session.query(ResultadoPessoa).filter(
            ResultadoPessoa.resultado_codigo == resultado_id).all()
        if resultado_pessoa:
            return resultado_pessoa
        return False

    def read_resultado_pessoa_p_id(self, pessoa_id):
        resultado_pessoa = self.banco.session.query(ResultadoPessoa).filter(
            ResultadoPessoa.pessoa_codigo == pessoa_id).all()
        if resultado_pessoa:
            return resultado_pessoa
        return False

    def remove(self, codigo_resultado):
        self.banco.engine.execute(f'delete from resultado_pessoa where resultado_codigo = {codigo_resultado}')
        self.banco.session.commit()
        return True
