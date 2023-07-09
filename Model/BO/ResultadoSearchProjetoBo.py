class ResultadoSearchProjetoBo:
    def __init__(self, resultado_dmo):
        self.resultado_dmo = resultado_dmo

    def execute(self, projeto_codigo):
        resultado_list = self.resultado_dmo.read_projeto_resultado(projeto_codigo)

        return resultado_list
