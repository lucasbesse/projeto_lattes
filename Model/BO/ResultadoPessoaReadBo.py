class ResultadoPessoaReadBo:
    def __init__(self, resultado_pessoa_dmo):
        self.resultado_pessoa_dmo = resultado_pessoa_dmo

    def execute(self, resultado_codigo):
        pessoa_resultado_list = self.resultado_pessoa_dmo.read_resultado_pessoa(resultado_codigo)

        return pessoa_resultado_list
