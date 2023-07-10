from marshmallow import Schema, fields, validate


class ProjetoUpdateSchema(Schema):
    titulo = fields.Str(required=False)
    descricao = fields.Str(required=False)
    projeto_codigo = fields.Int(required=False)
