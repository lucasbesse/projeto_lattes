class PessoaRepository:
    def __init__(self):
        self._pessoas = []

    def add(self, pessoa):
        self._pessoas.append(pessoa)

    def read(self):
        return self._pessoas
