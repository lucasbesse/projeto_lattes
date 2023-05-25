class ReadPessoaPaginaBo:
    def __init__(self, pessoa_repository):
        self._pessoa_repository = pessoa_repository

    def execute(self, limit, offset, ):
        result = self._pessoa_repository.read_pagination(limit=limit, offset=offset)

        return result
