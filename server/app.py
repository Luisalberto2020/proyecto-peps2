
from flask import Flask
from controllers.usuariosController import usuarios_bluebrint

app = Flask(__name__)
app.register_blueprint(usuarios_bluebrint)


if __name__ == '__main__':
    app.run(debug=True)

