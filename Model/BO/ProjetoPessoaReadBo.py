class ProjetoPessoaReadBo:
    def __init__(self, projeto_pessoa_dmo):
        self.projeto_pessoa_dmo = projeto_pessoa_dmo

    def execute(self, projeto_codigo):
        pessoa_projeto_list = self.projeto_pessoa_dmo.read_projeto_pessoa(projeto_codigo)

        return pessoa_projeto_list
