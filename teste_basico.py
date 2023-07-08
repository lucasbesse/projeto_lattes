from flask import Blueprint, request
from flask_cors import CORS
import json

from Control.Controllers.PessoaController import PessoaController

from Model.BO.PessoaCreateBo import PessoaCreateBo
from Model.BO.PessoaReadCodigoBo import PessoaReadCodigoBo
from Model.BO.PessoaReadPaginaBo import PessoaReadPaginaBo
from Model.BO.PessoaUpdateBo import PessoaUpdateBo
from Model.BO.PessoaDeleteBo import PessoaDeleteBo

from Model.DMO.PessoaDmo import PessoaDmo

from DataBase.Banco import Banco

from Control.Controllers.ProjetoController import ProjetoController

from Model.BO.ProjetoCreateBo import ProjetoCreateBo
from Model.BO.ProjetoReadCodigoBo import ProjetoReadCodigoBo
from Model.BO.ProjetoReadPaginaBo import ProjetoReadPaginaBo
from Model.BO.ProjetoUpdateBo import ProjetoUpdateBo
from Model.BO.ProjetoDeleteBo import ProjetoDeleteBo
from Model.BO.ProjetoPessoaCreateBo import ProjetoPessoaCreateBo

from Model.DMO.ProjetoDmo import ProjetoDmo

banco = Banco()
pessoa_dmo = PessoaDmo(banco)

create_pessoa_bo = PessoaCreateBo(pessoa_dmo)
read_pessoa_codigo_bo = PessoaReadCodigoBo(pessoa_dmo)
read_pessoa_pagina_bo = PessoaReadPaginaBo(pessoa_dmo)
update_pessoa_bo = PessoaUpdateBo(pessoa_dmo)
delete_pessoa_bo = PessoaDeleteBo(pessoa_dmo)

pessoa_controller = PessoaController(create_pessoa_bo,
                                     read_pessoa_codigo_bo,
                                     read_pessoa_pagina_bo,
                                     update_pessoa_bo,
                                     delete_pessoa_bo)

projeto_dmo = ProjetoDmo(banco)


create_projeto_bo = ProjetoCreateBo(projeto_dmo)
read_projeto_codigo_bo = ProjetoReadCodigoBo(projeto_dmo)
read_projeto_pagina_bo = ProjetoReadPaginaBo(projeto_dmo)
update_projeto_bo = ProjetoUpdateBo(projeto_dmo)
delete_projeto_bo = ProjetoDeleteBo(projeto_dmo)
projeto_pessoa_create_bo = ProjetoPessoaCreateBo(banco, read_pessoa_codigo_bo, read_projeto_codigo_bo)

projeto_controller = ProjetoController(create_projeto_bo,
                                       read_projeto_codigo_bo,
                                       read_projeto_pagina_bo,
                                       update_projeto_bo,
                                       delete_projeto_bo,
                                       projeto_pessoa_create_bo)

data = {,
        'pessoas':[{'codigo':1,'tipo':'i'},
                   {'codigo':2,'tipo':'i'},
                   {'codigo':3,'tipo':'p'}
        ]


projeto_controller.adicionar_pessoa(1,)


