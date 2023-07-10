from marshmallow import Schema, fields


class ResultadoPessoaSchemaRead(Schema):
    resultado_codigo = fields.Int(required=True)
    pessoa_codigo = fields.Int(required=True)
    tipo = fields.Str(required=True)
