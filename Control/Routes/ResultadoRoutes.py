from flask import Blueprint, request
from flask_cors import CORS
import json
from Control.Routes import *


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
