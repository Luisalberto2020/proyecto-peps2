import json

from controllers.jwt_utils import Jwtutils
from flask import Blueprint, request
from controllers.usuario_repository import UsuariosRepository
from flask_cors import cross_origin


usuarios_bluebrint = Blueprint('usuarios_bluebrint', __name__)


@usuarios_bluebrint.route('/crearusuario', methods=['POST'])
@cross_origin()
def crear_usuario():
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

@usuarios_bluebrint.route('/loginusuario', methods=['POST'])
@cross_origin()
def login_usuario():
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
            email = data['email']
            password = data['password']
            usuario_repository = UsuariosRepository()
            usuario = usuario_repository.login_usuario(email, password)
            if usuario is not None:
                token = Jwtutils()
                token_string = token.create_token(usuario[0], usuario[3])
                code = 200
                response = {
                    'code': code,
                    'token': token_string,
                    'message': 'Usuario logueado correctamente'
                }
            else:
                code = 401
                response = {
                    'code': code,
                    'message': 'Usuario o contraseña incorrectos'
                }
        except Exception as e:
            code = 401
            response = {
                'code': code,
                'message': f'Error al loguear usuario {e}',
            }

    return json.dumps(response), code
