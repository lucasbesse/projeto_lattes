class ProjetoUpdateBo:
    def __init__(self, projeto_dmo):
        self.projeto_dmo = projeto_dmo

    def execute(self, codigo_projeto, data_dict):

        return self.projeto_dmo.update(codigo_projeto, **data_dict)
