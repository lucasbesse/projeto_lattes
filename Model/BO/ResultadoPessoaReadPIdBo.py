class ResultadoPessoaReadPIdBo:
    def __init__(self, resultado_pessoa_dmo):
        self.resultado_pessoa_dmo = resultado_pessoa_dmo

    def execute(self, pessoa_codigo):
        pessoa_resultado_list = self.resultado_pessoa_dmo.read_resultado_pessoa_p_id(pessoa_codigo)

        return pessoa_resultado_list
