class ProjetoReadPaginaBo:
    def __init__(self, projeto_dmo):
        self.projeto_dmo = projeto_dmo

    def execute(self, limit, offset):
        result = self.projeto_dmo.read_pagination(limit=limit, offset=offset)

        return result
