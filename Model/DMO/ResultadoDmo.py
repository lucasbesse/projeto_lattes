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

    def update(self, resultado_codigo, titulo="", descricao="", tipo="", autores="", colaboradores="", projeto="", codigo=""):
        resultado = self.banco.session.query(Resultado).get(resultado_codigo)
        if resultado:
            if titulo:
                resultado.set_titulo(titulo)
            if descricao:
                resultado.set_descricao(descricao)
            if tipo:
                resultado.set_tipo(tipo)
            if autores:
                resultado.set_autores(autores)
            if colaboradores:
                resultado.set_colaboradores(colaboradores)
            if projeto:
                resultado.set_projeto(projeto)
            if codigo:
                resultado.set_codigo(codigo)

            self.banco.session.commit()
            return True
        return False
