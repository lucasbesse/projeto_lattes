from marshmallow import Schema, fields


class PessoaUpdateSchema(Schema):
    codigo = fields.Int(required=False)
    nome = fields.Str(required=False)
    email = fields.Str(required=False)
    formacao = fields.Str(required=False)
    experiencia = fields.Str(required=False)
