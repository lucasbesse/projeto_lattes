from marshmallow import Schema, fields


class ProjetoPessoaSchemaRead(Schema):
    projeto_codigo = fields.Int(required=True)
    pessoa_codigo = fields.Int(required=True)
    tipo = fields.Str(required=True)
