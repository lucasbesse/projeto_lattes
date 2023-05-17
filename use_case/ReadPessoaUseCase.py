class ReadPessoaUseCase:
    def __init__(self, pessoa_repository):
        self._pessoa_repository = pessoa_repository

    def execute(self):
        result = self._pessoa_repository.read()
        return result
