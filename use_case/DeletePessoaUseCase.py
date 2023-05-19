class DeletePessoaUseCase:
    def __init__(self, pessoa_repository):
        self._pessoa_repository = pessoa_repository

    def execute(self, codigo):
        self._pessoa_repository.remove(codigo)
