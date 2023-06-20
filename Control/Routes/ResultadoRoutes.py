from flask import Blueprint, request
from flask_cors import CORS
import json

from Control.Controllers.ResultadoController import ResultadoController

from Model.BO.ResultadoCreateBo import ResultadoCreateBo
from Model.BO.ResultadoReadCodigoBo import ResultadoReadCodigoBo
from Model.BO.ResultadoReadPaginaBo import ResultadoReadPaginaBo
from Model.BO.ResultadoUpdateBo import ResultadoUpdateBo
from Model.BO.ResultadoDeleteBo import ResultadoDeleteBo

from Model.DMO.ResultadoDmo import ResultadoDmo

from DataBase.Banco import Banco

banco = Banco()
resultado_dmo = ResultadoDmo(banco)

create_resultado_bo = ResultadoCreateBo(resultado_dmo)
read_resultado_codigo_bo = ResultadoReadCodigoBo(resultado_dmo)
read_resultado_pagina_bo = ResultadoReadPaginaBo(resultado_dmo)
update_resultado_bo = ResultadoUpdateBo(resultado_dmo)
delete_resultado_bo = ResultadoDeleteBo(resultado_dmo)

resultado_controller = ResultadoController(create_resultado_bo,
                                     read_resultado_codigo_bo,
                                     read_resultado_pagina_bo,
                                     update_resultado_bo,
                                     delete_resultado_bo)

# pc = ResultadoController()

resultado_routes_bp = Blueprint("resultado_routes_bp", __name__)
CORS(resultado_routes_bp)


@resultado_routes_bp.route('/resultados', methods=['POST'])
def criar_resultado():
    json_data = json.dumps(request.get_json())
    print(type(json_data))
    print(json_data)
    return resultado_controller.criar_resultado(json_data)


@resultado_routes_bp.route('/resultados/<int:codigo>', methods=['GET'])
def ler_resultado_codigo(codigo):
    return resultado_controller.ler_resultado_codigo(codigo)


@resultado_routes_bp.route('/resultados', methods=['GET'])
def ler_resultado_pagina():
    limit = request.args.get('limit', default=100, type=int)
    offset = request.args.get('offset', default=0, type=int)
    return resultado_controller.ler_resultado_pagina(limit, offset)


@resultado_routes_bp.route('/resultados/<int:codigo>', methods=['PUT'])
def atualizar_resultado(codigo):
    json_data = json.dumps(request.get_json())
    print(type(json_data))
    print(json_data)
    return resultado_controller.atualizar_resultado(codigo, json_data)


@resultado_routes_bp.route('/resultados/<int:codigo>', methods=['DELETE'])
def deletar_resultado(codigo):
    return resultado_controller.deletar_resultado(codigo)
