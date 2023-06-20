class PessoaReadPaginaBo:
    def __init__(self, pessoa_dmo):
        self.pessoa_dmo = pessoa_dmo

    def execute(self, limit, offset):
        result = self.pessoa_dmo.read_pagination(limit=limit, offset=offset)

        return result
