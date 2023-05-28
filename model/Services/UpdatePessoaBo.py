class UpdatePessoaBo:
    def __init__(self, pessoa_dao):
        self._pessoa_dao = pessoa_dao

    def execute(self, codigo_pessoa, data_dict):

        return self._pessoa_dao.update(codigo_pessoa, **data_dict)
