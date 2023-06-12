from flask import Flask
from Control.Routes import PessoaRoutes

app = Flask(__name__)

# Registrar os blueprints
app.register_blueprint(PessoaRoutes.pessoa_routes_bp)

if __name__ == "__main__":
    app.run(debug=True)
