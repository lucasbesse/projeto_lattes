class ProjetoPessoaReadPIdBo:
    def __init__(self, projeto_pessoa_dmo):
        self.projeto_pessoa_dmo = projeto_pessoa_dmo

    def execute(self, pessoa_codigo):
        pessoa_projeto_list = self.projeto_pessoa_dmo.read_projeto_pessoa_p_id(pessoa_codigo)

        return pessoa_projeto_list
