import json

from control.PessoaController import PessoaController

from model.bo.CreatePessoaBo import CreatePessoaBo
from model.bo.ReadPessoaCodigoBo import ReadPessoaCodigoBo
from model.bo.ReadPessoaPaginaBo import ReadPessoaPaginaBo
from model.bo.UpdatePessoaBo import UpdatePessoaBo
from model.bo.DeletePessoaBo import DeletePessoaBo

from model.dao.repository.PessoaRepository import PessoaRepository

from model.dao.PessoaDao import PessoaDao

from model.dao.Banco import Banco

banco = Banco()
pessoa_dao = PessoaDao(banco)

create_pessoa_bo = CreatePessoaBo(pessoa_dao)
read_pessoa_codigo_bo = ReadPessoaCodigoBo(pessoa_dao)
read_pessoa_pagina_bo = ReadPessoaPaginaBo(pessoa_dao)
update_pessoa_bo = UpdatePessoaBo(pessoa_dao)
delete_pessoa_bo = DeletePessoaBo(pessoa_dao)

pc = PessoaController(create_pessoa_bo,
                      read_pessoa_codigo_bo,
                      read_pessoa_pagina_bo,
                      update_pessoa_bo,
                      delete_pessoa_bo)

nomes = ['Joao',
         'Maria',
         'Pedro',
         'Ana',
         'Luiza',
         'Lucas',
         'Isabela',
         'Rafael',
         'Júlia',
         'Mateus',
         'Camila',
         'Gabriel',
         'Laura',
         'Davi',
         'Manuela',
         'Guilherme',
         'Beatriz',
         'Miguel',
         'Mariana',
         'Matheus',
         'Letícia',
         'Enzo',
         'Giovanna',
         'Felipe',
         'Carolina',
         'Thiago',
         'Vitória',
         'Henrique',
         'Amanda',
         'Daniel']

print('======= CREATE =========')
for nome in nomes:
    json_data = json.dumps({'nome': nome})
    # print(json_data)
    pc.criar_pessoa(json_data)

pessoas = pc.ler_pessoa_pagina(limit=4, offset=0)
for pessoa in pessoas:
    print(pessoa)

print('======= DELETE =========')
pc.deletar_pessoa(1)

pessoas = pc.ler_pessoa_pagina(limit=4, offset=0)
for pessoa in pessoas:
    print(pessoa)

print('======= UPDATE =========')
json_data = '{"nome": "Luz Maria"}'
pc.atualizar_pessoa(2, json_data)

pessoas = pc.ler_pessoa_pagina(limit=4, offset=0)
for pessoa in pessoas:
    print(pessoa)

print('======= READ CODIGO =========')
print(pc.ler_pessoa_codigo(2))

