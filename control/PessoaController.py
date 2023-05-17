from projeto_lattes.model.Pessoa import Pessoa


class PessoaController:
    def __init__(self,create_pessoa_use_case,read_pessoa_use_case):
        self._create_pessoa_use_case = create_pessoa_use_case
        self._read_pessoa_use_case = read_pessoa_use_case

    def criar_pessoa(self, nome):
        pessoa_aux = Pessoa(nome)
        self._create_pessoa_use_case.execute(pessoa_aux)

    def ler_pessoas(self):
        return self._read_pessoa_use_case.execute()