from marshmallow import Schema, fields, validate


class ProjetoSchema(Schema):
    codigo = fields.Int(required=False)
    titulo = fields.Str(required=True)
    descricao = fields.Str(required=True)
