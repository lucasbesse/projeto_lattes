from Model.ORM.Projeto import Projeto
from Model.ORM.Resultado import Resultado


class ResultadoDmo:
    def __init__(self, banco):
        # Configuração da conexão com o banco de dados
        self.banco = banco

    def add(self, resultado):
        self.banco.session.add(resultado)
        self.banco.session.commit()
        self.banco.session.refresh(resultado)
        return resultado.codigo

    def read_pagination(self, limit, offset):
        resultados = self.banco.session.query(Resultado).limit(limit).offset(offset).all()
        return resultados

    def read_resultado(self, resultado_id):
        resultado = self.banco.session.query(Resultado).get(resultado_id)
        if resultado:
            return resultado
        return False

    def remove(self, resultado_id):
        resultado = self.banco.session.query(Resultado).get(resultado_id)
        print(resultado)
        if resultado:
            self.banco.session.delete(resultado)
            self.banco.session.commit()
            return True
        return False

    def update(self, resultado_codigo, titulo="", descricao="", tipo="", projeto_codigo="", codigo=""):
        resultado = self.banco.session.query(Resultado).get(resultado_codigo)
        if resultado:
            if titulo:
                resultado.titulo = titulo
            if descricao:
                resultado.descricao = descricao
            if tipo:
                resultado.tipo = tipo
            if projeto_codigo:
                resultado.projeto_codigo = projeto_codigo
            if codigo:
                resultado.codigo = codigo

            self.banco.session.commit()
            return True
        return False

    def read_projeto_resultado(self, projeto_codigo):
        resultados = self.banco.session.query(Resultado).filter(
            Resultado.projeto_codigo == projeto_codigo).all()

        print(resultados)

        return resultados
