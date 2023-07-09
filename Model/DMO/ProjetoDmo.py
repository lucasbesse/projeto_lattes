from Model.ORM.Projeto import Projeto


class ProjetoDmo:
    def __init__(self, banco):
        # Configuração da conexão com o banco de dados
        self.banco = banco

    def add(self, projeto):
        self.banco.session.add(projeto)
        self.banco.session.commit()
        self.banco.session.refresh(projeto)
        return projeto.codigo

    def read_pagination(self, limit, offset):
        projetos = self.banco.session.query(Projeto).limit(limit).offset(offset).all()
        return projetos

    def read_projeto(self, projeto_id):
        projeto = self.banco.session.query(Projeto).get(projeto_id)
        if projeto:
            return projeto
        return False

    def remove(self, projeto_id):
        projeto = self.banco.session.query(Projeto).get(projeto_id)
        print(projeto)
        if projeto:
            self.banco.session.delete(projeto)
            self.banco.session.commit()
            return True
        return False

    def update(self, projeto_codigo, codigo="", titulo="", descricao="", integrantes="", pesquisadores="", resultado=""):
        projeto = self.banco.session.query(Projeto).get(projeto_codigo)
        if projeto:
            if codigo:
                projeto.codigo = codigo
            if titulo:
                projeto.titulo = titulo
            if descricao:
                projeto.descricao = descricao
            if integrantes:
                projeto.integrantes = integrantes
            if pesquisadores:
                projeto.pesquisadores = pesquisadores
            if resultado:
                projeto.resultado = resultado

            self.banco.session.commit()
            return True
        return False


