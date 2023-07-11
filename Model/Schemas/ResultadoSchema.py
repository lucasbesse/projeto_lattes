from marshmallow import Schema, fields


class ResultadoSchema(Schema):
    codigo = fields.Int(required=False)
    titulo = fields.Str(required=True)
    descricao = fields.Str(required=True)
    tipo = fields.Str(required=False)
    projeto_codigo = fields.Int(required=False)
    data_publicacao = fields.Str(required=False)
