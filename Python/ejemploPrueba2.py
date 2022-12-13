from datosPrueba2 import *

def jsonBuscar(clave,objeto):
    valorDevuelto= []
    if isinstance(objeto, dict): 
        for k, v in objeto.items(): 
            if k == clave:
                temp={k:v}
                valorDevuelto.append(temp)
            else:
                if isinstance(v, dict): 
                   valorDevuelto=jsonBuscar(clave, v)
    else: 
        for val in objeto:
            if not isinstance(val, (str,int)):
                valorDevuelto=jsonBuscar(clave,val)
    return valorDevuelto
print (jsonBuscar ("prioridad", datosCompra))
