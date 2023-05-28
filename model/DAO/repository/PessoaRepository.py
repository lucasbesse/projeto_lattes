import copy

class PessoaRepository:
    def __init__(self):
        self._pessoas = []

    def add(self, pessoa):
        pessoa._set_codigo(len(self._pessoas)+1)  # auto increment da base
        self._pessoas.append(pessoa)
        return True

    def read_pagination(self, limit, offset):
        pessoas_aux = self._pessoas[offset:]

        # Aplicar o limite
        if limit is not None:
            pessoas_aux = pessoas_aux[:limit]

        return pessoas_aux

    def read_pessoa(self, pessoa_id):
        # Aplicar o limite
        for pessoa in self._pessoas:
            if pessoa.get_codigo() == pessoa_id:
                return pessoa  # Indica que a pessoa foi removida com sucesso
        return False  # Indica que a pessoa não foi encontrada

    def remove(self, pessoa_id):
        for pessoa in self._pessoas:
            if pessoa.get_codigo() == pessoa_id:
                self._pessoas.remove(pessoa)
                return True  # Indica que a pessoa foi removida com sucesso
        return False  # Indica que a pessoa não foi encontrada

    def update(self, pessoa_id, novo_nome="", novo_codigo=""):
        for pessoa in self._pessoas:
            if pessoa.get_codigo() == pessoa_id:
                if novo_nome:
                    pessoa.set_nome(novo_nome)
                if novo_codigo:
                    pessoa.__set_codigo(novo_codigo)
                return True  # Indica que a pessoa foi atualizada com sucesso
        return False  # Indica que a pessoa não foi encontrada
