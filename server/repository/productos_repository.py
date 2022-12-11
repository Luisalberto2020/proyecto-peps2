from repository.dBConnect import dBConnector
from model.producto import Producto


class ProductoRepository(dBConnector):

    def crear_producto(self, nombre:str, precio:float, url:str):
        cursor = self.useDatabase()
        cursor.execute(
            "INSERT INTO productos (nombre, precio, url) VALUES (%s, %s, %s)", 
            (nombre, precio, url)
        )
        self.mydb.commit()
        self.mydb.close()


    def get_productos(self) -> list:
        cursor = self.useDatabase()
        cursor.execute("SELECT * FROM productos")
        result = cursor.fetchall()
        self.mydb.commit()
        self.mydb.close()

        productos = []
        for producto in result:
            productos.append(Producto(producto[0], producto[1], producto[2], producto[3]))

        return productos