import json

from flask import Blueprint, request
from controllers.usuario_repository import UsuariosRepository

usuarios_bluebrint = Blueprint('usuarios_bluebrint', __name__)

@usuarios_bluebrint.route('/crearusuario', methods=['POST'])
def crear_usuario():
    headers = request.headers
    if headers['Content-Type'] != 'application/json':
        code = 401
        response = {
            'code': code,
            'message': 'Content-Type debe ser application/json'
        }
    else:
        data = json.loads(request.data)
        email = data['email']
        password = data['password']
        admin = data['admin']

        try:
            usuario_repository = UsuariosRepository()
            usuario_repository.crear_usuario(email, password, admin)
        except Exception as e:
            code = 401
            response = {
                'code': code,
                'message': 'Error al crear usuario',
            }
            print(e)
        
    res = flask.response(response, code)
    res.headers['Content-Type'] = 'application/json'
    res.headers['Access-Control-Allow-Origin'] = '*'

    return res


