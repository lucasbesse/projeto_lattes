from marshmallow import Schema, fields, validate


class PessoaUpdateSchema(Schema):
    nome = fields.Str(required=False, validate=validate.Length(min=3, max=50))
    codigo = fields.Int(required=False)
    email = fields.Str(required=False)
    formacao = fields.Str(required=False)
    experiencia = fields.Str(required=False)
