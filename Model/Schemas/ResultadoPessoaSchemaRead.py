from marshmallow import Schema, fields


class ResultadoPessoaSchemaRead(Schema):
    pessoa_codigo = fields.Int(required=True)
    tipo = fields.Str(required=True)