from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model.ORM.Pessoa import Base as BasePessoa
from Model.ORM.Projeto import Base as BaseProjeto
from Model.ORM.Resultado import Base as BaseResultado
from Model.ORM.ProjetoPessoa import Base as BaseProjetoPessoa
from Model.ORM.ResultadoPessoa import Base as BaseResultadoPessoa


class Banco:
    def __init__(self):

        host = 'localhost'
        db = 'projeto_lattes'
        user = 'projeto_lattes'
        pwd = 'abcd1234'

        print("Conectando a base de dados...")
        self.engine = create_engine(f"postgresql://{user}:{pwd}@{host}/{db}")
        BasePessoa.metadata.create_all(self.engine)
        BaseProjeto.metadata.create_all(self.engine)
        BaseResultado.metadata.create_all(self.engine)
        BaseProjetoPessoa.metadata.create_all(self.engine)
        BaseResultadoPessoa.metadata.create_all(self.engine)
        session = sessionmaker(bind=self.engine)
        self.session = session()
        print("Conectado!")

