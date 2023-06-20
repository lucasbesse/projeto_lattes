class ResultadoReadPaginaBo:
    def __init__(self, resultado_dmo):
        self.resultado_dmo = resultado_dmo

    def execute(self, limit, offset):
        result = self.resultado_dmo.read_pagination(limit=limit, offset=offset)

        return result
