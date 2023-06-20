class PessoaUpdateBo:
    def __init__(self, pessoa_dmo):
        self.pessoa_dmo = pessoa_dmo

    def execute(self, codigo_pessoa, data_dict):

        return self.pessoa_dmo.update(codigo_pessoa, **data_dict)
