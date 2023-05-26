class DeletePessoaBo:
    def __init__(self, pessoa_dao):
        self._pessoa_dao = pessoa_dao

    def execute(self, codigo):
        self._pessoa_dao.remove(codigo)
