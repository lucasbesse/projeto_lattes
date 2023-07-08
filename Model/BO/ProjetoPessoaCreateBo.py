from Model.ORM.ProjetoPessoa import ProjetoPessoa


class ProjetoPessoaCreateBo:
    def __init__(self, projeto_pessoa_dmo, pessoa_read_codigo_bo, projeto_read_codigo_bo):
        self.projeto_pessoa_dmo = projeto_pessoa_dmo
        self.pessoa_read_codigo_bo = pessoa_read_codigo_bo
        self.projeto_read_codigo_bo = projeto_read_codigo_bo

    def execute(self, codigo_projeto, pessoas):
        print(type(pessoas), pessoas)

        projeto = self.projeto_read_codigo_bo.execute(codigo_projeto)
        self.projeto_pessoa_dmo.remove(codigo_projeto)

        for json_pessoa in pessoas:
            pessoa = self.pessoa_read_codigo_bo.execute(json_pessoa['codigo'])
            if pessoa and projeto:

                projeto_pessoa = ProjetoPessoa(projeto=projeto.codigo, pessoa=pessoa.codigo, tipo=json_pessoa['tipo'])

                self.projeto_pessoa_dmo.add(projeto_pessoa)

        return True