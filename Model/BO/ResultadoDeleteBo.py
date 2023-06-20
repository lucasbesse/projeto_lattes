class ResultadoDeleteBo:
    def __init__(self, resultado_dmo):
        self.resultado_dmo = resultado_dmo

    def execute(self, codigo):
        return self.resultado_dmo.remove(codigo)
