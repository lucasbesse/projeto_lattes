from flask import Blueprint, request
from flask_cors import CORS
import json

from Control.Controllers.ProjetoController import ProjetoController

from Model.BO.ProjetoCreateBo import ProjetoCreateBo
from Model.BO.ProjetoReadCodigoBo import ProjetoReadCodigoBo
from Model.BO.ProjetoReadPaginaBo import ProjetoReadPaginaBo
from Model.BO.ProjetoUpdateBo import ProjetoUpdateBo
from Model.BO.ProjetoDeleteBo import ProjetoDeleteBo

from Model.DMO.ProjetoDmo import ProjetoDmo

from DataBase.Banco import Banco

banco = Banco()
projeto_dmo = ProjetoDmo(banco)

create_projeto_bo = ProjetoCreateBo(projeto_dmo)
read_projeto_codigo_bo = ProjetoReadCodigoBo(projeto_dmo)
read_projeto_pagina_bo = ProjetoReadPaginaBo(projeto_dmo)
update_projeto_bo = ProjetoUpdateBo(projeto_dmo)
delete_projeto_bo = ProjetoDeleteBo(projeto_dmo)

projeto_controller = ProjetoController(create_projeto_bo,
                                     read_projeto_codigo_bo,
                                     read_projeto_pagina_bo,
                                     update_projeto_bo,
                                     delete_projeto_bo)

# pc = ProjetoController()

projeto_routes_bp = Blueprint("projeto_routes_bp", __name__)
CORS(projeto_routes_bp)


@projeto_routes_bp.route('/projetos', methods=['POST'])
def criar_projeto():
    json_data = json.dumps(request.get_json())
    print(type(json_data))
    print(json_data)
    return projeto_controller.criar_projeto(json_data)


@projeto_routes_bp.route('/projetos/<int:codigo>', methods=['GET'])
def ler_projeto_codigo(codigo):
    return projeto_controller.ler_projeto_codigo(codigo)


@projeto_routes_bp.route('/projetos', methods=['GET'])
def ler_projeto_pagina():
    limit = request.args.get('limit', default=100, type=int)
    offset = request.args.get('offset', default=0, type=int)
    return projeto_controller.ler_projeto_pagina(limit, offset)


@projeto_routes_bp.route('/projetos/<int:codigo>', methods=['PUT'])
def atualizar_projeto(codigo):
    json_data = json.dumps(request.get_json())
    print(type(json_data))
    print(json_data)
    return projeto_controller.atualizar_projeto(codigo, json_data)


@projeto_routes_bp.route('/projetos/<int:codigo>', methods=['DELETE'])
def deletar_projeto(codigo):
    return projeto_controller.deletar_projeto(codigo)
