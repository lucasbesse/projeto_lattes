from marshmallow import Schema, fields, validate


class ResultadoUpdateSchema(Schema):
    titulo = fields.Str(required=False)
    descricao = fields.Str(required=False)
    tipo = fields.Str(required=False)
    autores = fields.Str(required=False)
    colaboradores = fields.Str(required=False)
    projeto = fields.Str(required=False)
