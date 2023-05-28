from model.DTO.Pessoa import Pessoa


class CreatePessoaBo:
    def __init__(self, pessoa_dao):
        self._pessoa_dao = pessoa_dao

    def execute(self, data_dict):

        pessoa_aux = Pessoa(**data_dict)
        return self._pessoa_dao.add(pessoa_aux)
