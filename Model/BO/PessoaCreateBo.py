from Model.ORM.Pessoa import Pessoa


class CreatePessoaBo:
    def __init__(self, pessoa_dmo):
        self.pessoa_dmo = pessoa_dmo

    def execute(self, data_dict):

        pessoa_aux = Pessoa(**data_dict)
        return self.pessoa_dmo.add(pessoa_aux)
