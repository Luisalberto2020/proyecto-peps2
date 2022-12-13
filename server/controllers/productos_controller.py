from flask import Blueprint, request
from flask_cors import cross_origin
import json
from markupsafe import Markup
from repository.productos_repository import ProductoRepository
from model.producto import Producto
from utils.jwt_utils import Jwtutils
import logging

productos_bluebrint = Blueprint('productos_bluebrint', __name__)

@productos_bluebrint.route('/crearproducto', methods=['POST'])
@cross_origin()
def crear_producto():
    code = 401
    response = {
            'code': code,
            'message': 'Errror'
        }
    headers = request.headers
    if headers['Content-Type'] != 'application/json':
        code = 401
        response = {
            'code': code,
            'message': 'Content-Type debe ser application/json'
        }
    else:
        if headers['token']:
            print(headers['token'])
            if Jwtutils().is_valido(headers['token']):
                print('token valido')
                if Jwtutils().is_admin(headers['token']):
                    print('es admin')
                  
                    try:
                        data = json.loads(request.data)
                        nombre = data['nombre']
                        precio = data['precio']
                        producto_repository = ProductoRepository()
                        producto_repository.crear_producto(Markup(nombre), Markup(precio),'')
                        code = 200
                        response = {
                        'code': code,
                        'message': 'insertado correctamente'
                        }
                    except Exception as e:
                        code = 401
                        response = {
                            'code': code,
                            'message': f'Error al crear producto {e}',
                        }
            else:
                code = 401
                response = {
                    'code': code,
                    'message': 'Token invalido',
                }

    return json.dumps(response), code


@productos_bluebrint.route('/getproductos', methods=['GET'])
@cross_origin()
def get_productos():
    try:
        producto_repository = ProductoRepository()
        productos = producto_repository.get_productos()
        response = []
        for producto in productos:
            response.append(producto.to_dict())
        code = 200
    except Exception as e:
        code = 401
        response = {
            'code': code,
            'message': f'Error al obtener productos {e}',
        }

    return json.dumps(response), code

@productos_bluebrint.route('/deleteproducto/<id>', methods=['DELETE'])
@cross_origin()
def delete_producto(id):
    headers = request.headers
    if headers['token'] and Jwtutils().is_valido(headers['token']) and Jwtutils().is_admin(headers['token']):
        try:
            data = json.loads(request.data)
            producto_repository = ProductoRepository()
            producto_repository.delete_producto(id)
            code = 200
            response = {
                'code': code,
                'message': 'Eliminado correctamente',
            }
        except Exception as e:
            code = 401
            response = {
                'code': code,
                'message': f'Error al eliminar producto {e}',
            }
    else:
        code = 401
        response = {
            'code': code,
            'message': 'Token invalido',
        }

    return json.dumps(response), code