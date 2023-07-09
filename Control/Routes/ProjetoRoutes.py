from flask import Blueprint, request
from flask_cors import CORS
import json
from Control.Routes import *


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
