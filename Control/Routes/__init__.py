from Control.Controllers.PessoaController import PessoaController
from Control.Controllers.ProjetoController import ProjetoController
from Control.Controllers.ResultadoController import ResultadoController
from DataBase.Banco import Banco
from Model.BO.PessoaCreateBo import PessoaCreateBo
from Model.BO.PessoaDeleteBo import PessoaDeleteBo
from Model.BO.PessoaReadCodigoBo import PessoaReadCodigoBo
from Model.BO.PessoaReadPaginaBo import PessoaReadPaginaBo
from Model.BO.PessoaUpdateBo import PessoaUpdateBo
from Model.BO.ProjetoPessoaCreateBo import ProjetoPessoaCreateBo
from Model.BO.ProjetoCreateBo import ProjetoCreateBo
from Model.BO.ProjetoDeleteBo import ProjetoDeleteBo
from Model.BO.ProjetoPessoaReadBo import ProjetoPessoaReadBo
from Model.BO.ProjetoPessoaReadPIdBo import ProjetoPessoaReadPIdBo
from Model.BO.ProjetoReadCodigoBo import ProjetoReadCodigoBo
from Model.BO.ProjetoReadPaginaBo import ProjetoReadPaginaBo
from Model.BO.ProjetoUpdateBo import ProjetoUpdateBo
from Model.BO.ResultadoCreateBo import ResultadoCreateBo
from Model.BO.ResultadoDeleteBo import ResultadoDeleteBo
from Model.BO.ResultadoPessoaCreateBo import ResultadoPessoaCreateBo
from Model.BO.ResultadoPessoaReadBo import ResultadoPessoaReadBo
from Model.BO.ResultadoPessoaReadPIdBo import ResultadoPessoaReadPIdBo
from Model.BO.ResultadoReadCodigoBo import ResultadoReadCodigoBo
from Model.BO.ResultadoReadPaginaBo import ResultadoReadPaginaBo
from Model.BO.ResultadoSearchProjetoBo import ResultadoSearchProjetoBo
from Model.BO.ResultadoUpdateBo import ResultadoUpdateBo
from Model.DMO.PessoaDmo import PessoaDmo
from Model.DMO.ProjetoDmo import ProjetoDmo
from Model.DMO.ProjetoPessoaDmo import ProjetoPessoaDmo
from Model.DMO.ResultadoDmo import ResultadoDmo
from Model.DMO.ResultadoPessoaDmo import ResultadoPessoaDmo

print("Instanciando classes...")

banco = Banco()

projeto_dmo = ProjetoDmo(banco=banco)
pessoa_dmo = PessoaDmo(banco=banco)
projeto_pessoa_dmo = ProjetoPessoaDmo(banco=banco)
resultado_dmo = ResultadoDmo(banco=banco)
resultado_pessoa_dmo = ResultadoPessoaDmo(banco=banco)

pessoa_create_bo = PessoaCreateBo(pessoa_dmo=pessoa_dmo)
pessoa_delete_bo = PessoaDeleteBo(pessoa_dmo=pessoa_dmo)
pessoa_read_codigo_bo = PessoaReadCodigoBo(pessoa_dmo=pessoa_dmo)
pessoa_read_pagina_bo = PessoaReadPaginaBo(pessoa_dmo=pessoa_dmo)
pessoa_update_bo = PessoaUpdateBo(pessoa_dmo=pessoa_dmo)
projeto_create_bo = ProjetoCreateBo(projeto_dmo=projeto_dmo)
projeto_delete_bo = ProjetoDeleteBo(projeto_dmo=projeto_dmo)
projeto_pessoa_read_bo = ProjetoPessoaReadBo(projeto_pessoa_dmo=projeto_pessoa_dmo)
projeto_pessoa_read_p_id_bo = ProjetoPessoaReadPIdBo(projeto_pessoa_dmo=projeto_pessoa_dmo)
projeto_read_codigo_bo = ProjetoReadCodigoBo(projeto_dmo=projeto_dmo)
projeto_read_pagina_bo = ProjetoReadPaginaBo(projeto_dmo=projeto_dmo)
projeto_update_bo = ProjetoUpdateBo(projeto_dmo=projeto_dmo)
resultado_create_bo = ResultadoCreateBo(resultado_dmo=resultado_dmo)
resultado_delete_bo = ResultadoDeleteBo(resultado_dmo=resultado_dmo)
resultado_pessoa_read_bo = ResultadoPessoaReadBo(resultado_pessoa_dmo=resultado_pessoa_dmo)
resultado_pessoa_read_p_id_bo = ResultadoPessoaReadPIdBo(resultado_pessoa_dmo=resultado_pessoa_dmo)
resultado_read_codigo_bo = ResultadoReadCodigoBo(resultado_dmo=resultado_dmo)
resultado_read_pagina_bo = ResultadoReadPaginaBo(resultado_dmo=resultado_dmo)
resultado_search_projeto_bo = ResultadoSearchProjetoBo(resultado_dmo=resultado_dmo)
resultado_update_bo = ResultadoUpdateBo(resultado_dmo=resultado_dmo)

projeto_pessoa_create_bo = ProjetoPessoaCreateBo(projeto_pessoa_dmo=projeto_pessoa_dmo,
                                                 pessoa_read_codigo_bo=pessoa_read_codigo_bo,
                                                 projeto_read_codigo_bo=projeto_read_codigo_bo)
resultado_pessoa_create_bo = ResultadoPessoaCreateBo(resultado_pessoa_dmo=resultado_pessoa_dmo,
                                                     pessoa_read_codigo_bo=pessoa_read_codigo_bo,
                                                     resultado_read_codigo_bo=resultado_read_codigo_bo)

pessoa_controller = PessoaController(pessoa_create_bo=pessoa_create_bo,
                                     pessoa_read_codigo_bo=pessoa_read_codigo_bo,
                                     pessoa_read_pagina_bo=pessoa_read_pagina_bo,
                                     pessoa_update_bo=pessoa_update_bo,
                                     pessoa_delete_bo=pessoa_delete_bo,
                                     projeto_pessoa_read_p_id_bo=projeto_pessoa_read_p_id_bo,
                                     resultado_pessoa_read_p_id_bo=resultado_pessoa_read_p_id_bo,
                                     projeto_read_codigo_bo=projeto_read_codigo_bo,
                                     resultado_read_codigo_bo=resultado_read_codigo_bo
)

projeto_controller = ProjetoController(projeto_create_bo=projeto_create_bo,
                                       projeto_read_codigo_bo=projeto_read_codigo_bo,
                                       projeto_read_pagina_bo=projeto_read_pagina_bo,
                                       projeto_update_bo=projeto_update_bo,
                                       projeto_delete_bo=projeto_delete_bo,
                                       projeto_pessoa_create_bo=projeto_pessoa_create_bo,
                                       projeto_pessoa_read_bo=projeto_pessoa_read_bo,
                                       pessoa_read_codigo_bo=pessoa_read_codigo_bo,
                                       resultado_search_projeto_bo=resultado_search_projeto_bo)


resultado_controller = ResultadoController(resultado_create_bo=resultado_create_bo,
                                           resultado_read_codigo_bo=resultado_read_codigo_bo,
                                           resultado_read_pagina_bo=resultado_read_pagina_bo,
                                           resultado_update_bo=resultado_update_bo,
                                           resultado_delete_bo=resultado_delete_bo,
                                           resultado_pessoa_create_bo=resultado_pessoa_create_bo,
                                           resultado_pessoa_read_bo=resultado_pessoa_read_bo,
                                           pessoa_read_codigo_bo=pessoa_read_codigo_bo,
                                           projeto_read_codigo_bo=projeto_read_codigo_bo,
                                           projeto_pessoa_read_bo=projeto_pessoa_read_bo)

print("Classes Instanciadas!")
