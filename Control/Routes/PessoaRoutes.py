from flask import Blueprint, request
from flask_cors import CORS
import json

from Control.Controllers.PessoaController import PessoaController

from Model.BO.PessoaCreateBo import PessoaCreateBo
from Model.BO.PessoaReadCodigoBo import PessoaReadCodigoBo
from Model.BO.PessoaReadPaginaBo import PessoaReadPaginaBo
from Model.BO.PessoaUpdateBo import PessoaUpdateBo
from Model.BO.PessoaDeleteBo import PessoaDeleteBo

from Model.DMO.PessoaDmo import PessoaDmo

from DataBase.Banco import Banco

banco = Banco()
pessoa_dmo = PessoaDmo(banco)

create_pessoa_bo = PessoaCreateBo(pessoa_dmo)
read_pessoa_codigo_bo = PessoaReadCodigoBo(pessoa_dmo)
read_pessoa_pagina_bo = PessoaReadPaginaBo(pessoa_dmo)
update_pessoa_bo = PessoaUpdateBo(pessoa_dmo)
delete_pessoa_bo = PessoaDeleteBo(pessoa_dmo)

pessoa_controller = PessoaController(create_pessoa_bo,
                                     read_pessoa_codigo_bo,
                                     read_pessoa_pagina_bo,
                                     update_pessoa_bo,
                                     delete_pessoa_bo)

# pc = PessoaController()

pessoa_routes_bp = Blueprint("pessoa_routes_bp", __name__)
CORS(pessoa_routes_bp)


@pessoa_routes_bp.route('/pessoas', methods=['POST'])
def criar_pessoa():
    json_data = json.dumps(request.get_json())
    print(type(json_data))
    print(json_data)
    return pessoa_controller.criar_pessoa(json_data)


@pessoa_routes_bp.route('/pessoas/<int:codigo>', methods=['GET'])
def ler_pessoa_codigo(codigo):
    return pessoa_controller.ler_pessoa_codigo(codigo)


@pessoa_routes_bp.route('/pessoas', methods=['GET'])
def ler_pessoa_pagina():
    limit = request.args.get('limit', default=100, type=int)
    offset = request.args.get('offset', default=0, type=int)
    return pessoa_controller.ler_pessoa_pagina(limit, offset)


@pessoa_routes_bp.route('/pessoas/<int:codigo>', methods=['PUT'])
def atualizar_pessoa(codigo):
    json_data = json.dumps(request.get_json())
    print(type(json_data))
    print(json_data)
    return pessoa_controller.atualizar_pessoa(codigo, json_data)


@pessoa_routes_bp.route('/pessoas/<int:codigo>', methods=['DELETE'])
def deletar_pessoa(codigo):
    return pessoa_controller.deletar_pessoa(codigo)
