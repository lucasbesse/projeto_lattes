class ReadPessoaCodigoBo:
    def __init__(self, pessoa_dao):
        self._pessoa_dao = pessoa_dao

    def execute(self, codigo):
        result = self._pessoa_dao.read_pessoa(codigo)

        return result
