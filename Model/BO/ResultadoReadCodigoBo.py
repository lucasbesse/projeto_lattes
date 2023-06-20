class ResultadoReadCodigoBo:
    def __init__(self, resultado_dmo):
        self.resultado_dmo = resultado_dmo

    def execute(self, codigo):
        result = self.resultado_dmo.read_resultado(codigo)

        return result
