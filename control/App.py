from flask import Flask


class App:
    def __init__(self, pessoa_controler_app):
        self.app = Flask(__name__)

        # Registra as rotas do controller de Pessoa
        self.app.register_blueprint(pessoa_controler_app)

    def run(self):
        self.app.run()
