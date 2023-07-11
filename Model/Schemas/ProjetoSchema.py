from marshmallow import Schema, fields


class ProjetoSchema(Schema):
    codigo = fields.Int(required=False)
    titulo = fields.Str(required=True)
    descricao = fields.Str(required=True)
    projeto_codigo = fields.Int(required=False)
    data_inicio = fields.Str(required=False)
    data_final = fields.Str(required=False)
    palavras_chave = fields.Str(required=False)
