import json

from flask import Blueprint, request
from controllers.usuario_repository import UsuariosRepository
from flask_cors import cross_origin


usuarios_bluebrint = Blueprint('usuarios_bluebrint', __name__)


@usuarios_bluebrint.route('/crearusuario', methods=['POST'])
@cross_origin()
def crear_usuario():
    print('crear usuario')
    headers = request.headers
    if headers['Content-Type'] != 'application/json':
        code = 401
        response = {
            'code': code,
            'message': 'Content-Type debe ser application/json'
        }
    else:
        try:
            data = json.loads(request.data)
            print(data)
            email = data['email']
            password = data['password']
            admin = data['admin']
            usuario_repository = UsuariosRepository()
            usuario_repository.crear_usuario(email, password, admin)
        except Exception as e:
            code = 401
            response = {
                'code': code,
                'message': f'Error al crear usuario {e}',
            }

    return json.dumps(response), code


