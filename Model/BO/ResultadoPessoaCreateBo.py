from Model.ORM.ResultadoPessoa import ResultadoPessoa


class ResultadoPessoaCreateBo:
    def __init__(self, resultado_pessoa_dmo, pessoa_read_codigo_bo, resultado_read_codigo_bo):
        self.resultado_pessoa_dmo = resultado_pessoa_dmo
        self.pessoa_read_codigo_bo = pessoa_read_codigo_bo
        self.resultado_read_codigo_bo = resultado_read_codigo_bo

    def execute(self, codigo_resultado, pessoas):
        print(type(pessoas), pessoas)

        resultado = self.resultado_read_codigo_bo.execute(codigo_resultado)
        self.resultado_pessoa_dmo.remove(codigo_resultado)

        for json_pessoa in pessoas:
            pessoa = self.pessoa_read_codigo_bo.execute(json_pessoa['codigo'])
            if pessoa and resultado:

                resultado_pessoa = ResultadoPessoa(resultado=resultado.codigo, pessoa=pessoa.codigo, tipo=json_pessoa['tipo'])

                self.resultado_pessoa_dmo.add(resultado_pessoa)

        return True