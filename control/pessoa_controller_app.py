from flask import Blueprint, jsonify, request, Flask

from control.Controllers.PessoaController import PessoaController

from model.Services.CreatePessoaBo import CreatePessoaBo
from model.Services.ReadPessoaCodigoBo import ReadPessoaCodigoBo
from model.Services.ReadPessoaPaginaBo import ReadPessoaPaginaBo
from model.Services.UpdatePessoaBo import UpdatePessoaBo
from model.Services.DeletePessoaBo import DeletePessoaBo

from model.DAO.PessoaDao import PessoaDao

from model.DAO.Banco import Banco

banco = Banco()
pessoa_dao = PessoaDao(banco)

create_pessoa_bo = CreatePessoaBo(pessoa_dao)
read_pessoa_codigo_bo = ReadPessoaCodigoBo(pessoa_dao)
read_pessoa_pagina_bo = ReadPessoaPaginaBo(pessoa_dao)
update_pessoa_bo = UpdatePessoaBo(pessoa_dao)
delete_pessoa_bo = DeletePessoaBo(pessoa_dao)

pessoa_controller = PessoaController(create_pessoa_bo,
                                     read_pessoa_codigo_bo,
                                     read_pessoa_pagina_bo,
                                     update_pessoa_bo,
                                     delete_pessoa_bo)

# pc = PessoaController()

pessoa_controller_app = Flask(__name__)


# pc = PessoaController()
@pessoa_controller_app.route('/pessoas', methods=['POST'])
def criar_pessoa():
    json_data = request.get_json()
    return pessoa_controller.criar_pessoa(json_data)


@pessoa_controller_app.route('/pessoas/<int:codigo>', methods=['GET'])
def ler_pessoa_codigo(codigo):
    return pessoa_controller.ler_pessoa_codigo(codigo)


@pessoa_controller_app.route('/pessoas', methods=['GET'])
def ler_pessoa_pagina():
    limit = request.args.get('limit', default=100, type=int)
    offset = request.args.get('offset', default=0, type=int)
    return pessoa_controller.ler_pessoa_pagina(limit, offset)


@pessoa_controller_app.route('/pessoas/<int:codigo>', methods=['PUT'])
def atualizar_pessoa(codigo):
    json_data = request.get_json()
    return pessoa_controller.atualizar_pessoa(codigo, json_data)


@pessoa_controller_app.route('/pessoas/<int:codigo>', methods=['DELETE'])
def deletar_pessoa(codigo):
    return pessoa_controller.deletar_pessoa(codigo)


if __name__ == '__main__':
    pessoa_controller_app.run(debug=True)
