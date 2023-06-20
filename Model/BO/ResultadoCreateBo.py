from Model.ORM.Resultado import Resultado


class ResultadoCreateBo:
    def __init__(self, resultado_dmo):
        self.resultado_dmo = resultado_dmo

    def execute(self, data_dict):

        resultado_aux = Resultado(**data_dict)
        return self.resultado_dmo.add(resultado_aux)
