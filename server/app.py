
from flask import Flask
from controllers.usuariosController import usuarios_bluebrint
from repository.dBConnect import dBConnector
from flask_cors import CORS
from controllers.productos_controller import productos_bluebrint

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(usuarios_bluebrint)
app.register_blueprint(productos_bluebrint)


@app.after_request
def set_secure_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response

if __name__ == '__main__':
    db = dBConnector()
    db.createDatabase()
    db.createTables()
    app.run(debug=True,host='0.0.0.0',port=5000)

