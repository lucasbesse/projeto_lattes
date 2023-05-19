import json

from control.PessoaController import PessoaController
from use_case.CreatePessoaUseCase import CreatePessoaUseCase
from use_case.ReadPessoaCodigoUseCase import ReadPessoaCodigoUseCase
from use_case.ReadPessoaPaginaUseCase import ReadPessoaPaginaUseCase
from use_case.UpdatePessoaUseCase import UpdatePessoaUseCase
from use_case.DeletePessoaUseCase import DeletePessoaUseCase
from repository.PessoaRepository import PessoaRepository

pessoa_repository = PessoaRepository()

create_pessoa_use_case = CreatePessoaUseCase(pessoa_repository)
read_pessoa_codigo_use_case = ReadPessoaCodigoUseCase(pessoa_repository)
read_pessoa_pagina_use_case = ReadPessoaPaginaUseCase(pessoa_repository)
update_pessoa_use_case = UpdatePessoaUseCase(pessoa_repository)
delete_pessoa_use_case = DeletePessoaUseCase(pessoa_repository)

pc = PessoaController(create_pessoa_use_case,
                      read_pessoa_codigo_use_case,
                      read_pessoa_pagina_use_case,
                      update_pessoa_use_case,
                      delete_pessoa_use_case)

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

