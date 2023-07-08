from flask import Flask
from Control.Routes import PessoaRoutes, ResultadoRoutes, ProjetoRoutes
from Control.Routes.ProjetoRoutes import projeto_pessoa_dmo
app = Flask(__name__)

# Registrar os blueprints
app.register_blueprint(PessoaRoutes.pessoa_routes_bp)
app.register_blueprint(ProjetoRoutes.projeto_routes_bp)
app.register_blueprint(ResultadoRoutes.resultado_routes_bp)

if __name__ == "__main__":
    app.run(debug=True)
    print(projeto_pessoa_dmo.read_projeto_pessoa(1))