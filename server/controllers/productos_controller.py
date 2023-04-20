import os
from flask import Blueprint, request
from flask_cors import cross_origin
import json
from markupsafe import Markup
from repository.productos_repository import ProductoRepository
from model.producto import Producto
from utils.jwt_utils import Jwtutils
import logging
import uuid
from werkzeug.utils import secure_filename
from flask import send_from_directory, escape

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
                        nombre = escape(data['nombre'])
                        precio = escape(data['precio'])
                        producto_repository = ProductoRepository()
                        id = producto_repository.crear_producto(Markup(nombre), Markup(precio),'')
                        code = 200
                        response = {
                        'code': code,
                        'message': 'insertado correctamente',
                        'id': id
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
            producto_repository = ProductoRepository()
            producto_repository.delete_producto(int(id))
            code = 200
            response = {
                'code': code,
                'message': 'Eliminado correctamente ',
            }
        except Exception as e:
            code = 400
            response = {
                'code': code,
                'message': f'Error al eliminar producto {id}',
            }
    else:
        code = 401
        response = {
            'code': code,
            'message': 'Token invalido',
        }

    return json.dumps(response), code

@productos_bluebrint.route('/updateproducto/', methods=['PUT'])
@cross_origin()
def update_producto():
    code = 401
    response = {
            'code': code,
            'message': 'Error'
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
                        producto_repository.update_producto(data['id'],Markup(nombre), Markup(precio), data['url'])
                        code = 200
                        response = {
                        'code': code,
                        'message': 'actualizado correctamente'
                        }
                    except Exception as e:
                        code = 401
                        response = {
                            'code': code,
                            'message': f'Error al actualizar producto {e}',
                        }
            else:
                code = 401
                response = {
                    'code': code,
                    'message': 'Token inválido',
                }

    return json.dumps(response), code

@productos_bluebrint.route('/getproducto/<id>', methods=['GET'])
@cross_origin()
def get_producto(id):
    try:
        producto_repository = ProductoRepository()
        producto = producto_repository.get_producto(id)
        response = producto.to_dict()
        code = 200


    except Exception as e:
        code = 401
        response = {
            'code': code,
            'message': f'Error al obtener producto {e}',
        }

    return json.dumps(response), code


@productos_bluebrint.route('/subirfoto/<id>', methods=['POST'])
@cross_origin()
def subir_foto(id):
    headers = request.headers

    if headers['token'] and Jwtutils().is_valido(headers['token']) and Jwtutils().is_admin(headers['token']):
        try:
            fichero = request.files['file']
            extension = os.path.splitext(request.url)[1]
            imagen = uuid.uuid4()
            sitio:str = f'/images/{imagen}.jpg'
            f = open(sitio, 'wb')
            f.write(fichero.read())
            f.close()
            producto_repository = ProductoRepository()
            producto = producto_repository.get_producto(id)
            logging.error(f'imagen')
            producto_repository.update_producto(id,producto.nombre, producto.precio,str(imagen) )
            code = 200
            response = {
                'code': code,
                'message': 'Foto subida correctamente ',
            }
        except Exception as e:
            code = 400
            response = {
                'code': code,
                'message': f'Error al subir foto {e}',
            }
    else:
        code = 401
        response = {
            'code': code,
            'message': 'Token invalido',
        }

    return json.dumps(response), code



@productos_bluebrint.route('/getfoto/<url>', methods=['GET'])
@cross_origin()
def get_fotos(url):
    url2  =secure_filename(url)

    return send_from_directory('/images/',f'{url}.jpg')





