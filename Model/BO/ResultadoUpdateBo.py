class ResultadoUpdateBo:
    def __init__(self, resultado_dmo):
        self.resultado_dmo = resultado_dmo

    def execute(self, codigo_resultado, data_dict):

        return self.resultado_dmo.update(codigo_resultado, **data_dict)
