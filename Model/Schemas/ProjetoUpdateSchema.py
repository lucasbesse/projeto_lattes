from marshmallow import Schema, fields


class ProjetoUpdateSchema(Schema):
    titulo = fields.Str(required=False)
    descricao = fields.Str(required=False)
    projeto_codigo = fields.Int(required=False)
    data_inicio = fields.Str(required=False)
    data_final = fields.Str(required=False)
    palavras_chave = fields.Str(required=False)
