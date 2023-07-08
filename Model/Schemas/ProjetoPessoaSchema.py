from marshmallow import Schema, fields, validate


class ProjetoPessoaSchema(Schema):
    projeto_codigo = fields.Int(required=False)
    pessoa_codigo = fields.Str(required=True)
    tipo = fields.Str(required=True)