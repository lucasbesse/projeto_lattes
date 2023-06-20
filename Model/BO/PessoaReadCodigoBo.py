class PessoaReadCodigoBo:
    def __init__(self, pessoa_dmo):
        self.pessoa_dmo = pessoa_dmo

    def execute(self, codigo):
        result = self.pessoa_dmo.read_pessoa(codigo)

        return result
