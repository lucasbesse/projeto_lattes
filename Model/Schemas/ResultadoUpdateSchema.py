from marshmallow import Schema, fields


class ResultadoUpdateSchema(Schema):
    titulo = fields.Str(required=False)
    descricao = fields.Str(required=False)
    tipo = fields.Str(required=False)
    projeto_codigo = fields.Int(required=False)
    data_publicacao = fields.Str(required=False)
