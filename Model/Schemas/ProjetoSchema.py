from marshmallow import Schema, fields, validate


class ProjetoSchema(Schema):
    titulo = fields.Str(required=True)
    descricao = fields.Str(required=True)
    integrantes = fields.Str(required=True)
    pesquisadores = fields.Str(required=False)
    resultado = fields.Str(required=False)
