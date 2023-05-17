class CreatePessoaUseCase:
    def __init__(self, pessoa_repository):
        self._pessoa_repository = pessoa_repository

    def execute(self, pessoa):
        self._pessoa_repository.add(pessoa)
