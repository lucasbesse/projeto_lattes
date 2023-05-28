from marshmallow import Schema, fields, validate


class PessoaSchema(Schema):
    nome = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    codigo = fields.Int(required=False)
