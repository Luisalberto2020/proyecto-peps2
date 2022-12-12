import json
import logging

from flask import Blueprint, request
from flask_cors import cross_origin
from repository.dBConnect import dBConnector
from repository.usuario_repository import UsuariosRepository
from utils.jwt_utils import Jwtutils
from markupsafe import Markup

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
            usuario_repository.crear_usuario(Markup(email), Markup(password), admin)
            code = 200
            response = {
                'code': code,
                'message': 'Usuario creado correctamente',
            }
            
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
            logging.error(f'usuario {usuario}')
            if usuario is not None:
                token_string = Jwtutils.create_token(usuario[0], usuario[3])
                logging.error(f'token_string {token_string}')
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
