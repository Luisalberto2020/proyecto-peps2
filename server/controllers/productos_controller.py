from flask import Blueprint, request
from flask_cors import cross_origin
import json
from markupsafe import Markup
from repository.productos_repository import ProductoRepository
from model.producto import Producto


productos_bluebrint = Blueprint('usuarios_bluebrint', __name__)

@productos_bluebrint.route('/crearproducto', methods=['POST'])
@cross_origin()
def crear_producto():
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
            nombre = data['nombre']
            precio = data['precio']
            url = data['url']
            producto_repository = ProductoRepository()
            producto_repository.crear_producto(Markup(nombre), Markup(precio), Markup(url))
        except Exception as e:
            code = 401
            response = {
                'code': code,
                'message': f'Error al crear producto {e}',
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