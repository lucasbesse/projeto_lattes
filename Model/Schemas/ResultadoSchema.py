from marshmallow import Schema, fields, validate


class ResultadoSchema(Schema):
    codigo = fields.Int(required=False)
    titulo = fields.Str(required=True)
    descricao = fields.Str(required=True)
    tipo = fields.Str(required=False)