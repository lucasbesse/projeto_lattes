from marshmallow import Schema, fields


class ProjetoPessoaSchemaRead(Schema):
    pessoa_codigo = fields.Int(required=True)
    tipo = fields.Str(required=True)