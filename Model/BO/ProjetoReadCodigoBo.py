class ProjetoReadCodigoBo:
    def __init__(self, projeto_dmo):
        self.projeto_dmo = projeto_dmo

    def execute(self, codigo):
        result = self.projeto_dmo.read_projeto(codigo)

        return result
