from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Banco:
    def __init__(self):

        host = 'localhost'
        db = 'projeto_lattes'
        user = 'projeto_lattes'
        pwd = 'abcd1234'
        engine = create_engine(f"postgresql://{user}:{pwd}@{host}/{db}")
        session = sessionmaker(bind=engine)
        self.session = session()
