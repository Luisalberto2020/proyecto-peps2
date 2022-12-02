from flask import Blueprint
import json

usuarios_bluebrint = Blueprint('usuarios_bluebrint', __name__)

@usuarios_bluebrint.route('/crear')
def crear():

    fdatos2 ='{ "nombre": "Juan", "apellido": [ "a", "b", "c" ] }'
    dicionario = json.loads(fdatos2)
    print(dicionario)
    print(dicionario["nombre"])

    datos:dict = {
        'nombre': 'Juan',
        'apellido': ['a', 'b', 'c'],
    } 
    datos['nombre'] 
    return json.dumps(datos, indent=4)


