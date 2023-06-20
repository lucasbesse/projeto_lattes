class ProjetoDeleteBo:
    def __init__(self, projeto_dmo):
        self.projeto_dmo = projeto_dmo

    def execute(self, codigo):
        return self.projeto_dmo.remove(codigo)
