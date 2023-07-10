from marshmallow import Schema, fields


class ProjetoSchema(Schema):
    codigo = fields.Int(required=False)
    titulo = fields.Str(required=True)
    descricao = fields.Str(required=True)
    projeto_codigo = fields.Int(required=False)
