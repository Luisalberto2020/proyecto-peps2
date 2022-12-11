
from dataclasses import dataclass


@dataclass
class Producto():
    id:int
    nombre:str
    precio:float
    url:str


    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'url': self.url
        }