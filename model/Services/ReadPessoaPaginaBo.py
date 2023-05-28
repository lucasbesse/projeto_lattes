class ReadPessoaPaginaBo:
    def __init__(self, pessoa_dao):
        self._pessoa_dao = pessoa_dao

    def execute(self, limit, offset):
        result = self._pessoa_dao.read_pagination(limit=limit, offset=offset)

        return result
