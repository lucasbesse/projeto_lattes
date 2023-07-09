from marshmallow import Schema, fields


class ProjetoPessoaSchema(Schema):
    pessoa_codigo = fields.Str(required=True)
    tipo = fields.Str(required=True)
    projeto_codigo = fields.Int(required=True)
