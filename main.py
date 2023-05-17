from projeto_lattes.control.PessoaController import PessoaController
from projeto_lattes.use_case.CreatePessoaUseCase import CreatePessoaUseCase
from projeto_lattes.use_case.ReadPessoaUseCase import ReadPessoaUseCase
from projeto_lattes.repository.PessoaRepository import PessoaRepository

pessoa_repository = PessoaRepository()

create_pessoa_use_case = CreatePessoaUseCase(pessoa_repository)
read_pessoa_use_case = ReadPessoaUseCase(pessoa_repository)

pc = PessoaController(create_pessoa_use_case, read_pessoa_use_case)

pc.criar_pessoa("Pedro")
print(pc.ler_pessoas())

pc.criar_pessoa("Daniel")
print(pc.ler_pessoas())