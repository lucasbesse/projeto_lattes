from marshmallow import Schema, fields


class PessoaSchema(Schema):
    codigo = fields.Int(required=False)
    nome = fields.Str(required=True)
    email = fields.Str(required=True)
    formacao = fields.Str(required=False)
    experiencia = fields.Str(required=False)
