class PessoaDeleteBo:
    def __init__(self, pessoa_dmo):
        self.pessoa_dmo = pessoa_dmo

    def execute(self, codigo):
        return self.pessoa_dmo.remove(codigo)
