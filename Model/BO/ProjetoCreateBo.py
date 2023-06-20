from Model.ORM.Projeto import Projeto


class ProjetoCreateBo:
    def __init__(self, projeto_dmo):
        self.projeto_dmo = projeto_dmo

    def execute(self, data_dict):

        projeto_aux = Projeto(**data_dict)
        return self.projeto_dmo.add(projeto_aux)
