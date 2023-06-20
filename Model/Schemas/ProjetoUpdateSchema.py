from marshmallow import Schema, fields, validate


class ProjetoUpdateSchema(Schema):
    titulo = fields.Str(required=False)
    descricao = fields.Str(required=False)
    integrantes = fields.Str(required=False)
    pesquisadores = fields.Str(required=False)
    resultado = fields.Str(required=False)
