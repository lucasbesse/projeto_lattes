class ReadPessoaCodigoBo:
    def __init__(self, pessoa_repository):
        self._pessoa_repository = pessoa_repository

    def execute(self, codigo):
        result = self._pessoa_repository.read_pessoa(codigo)

        return result
