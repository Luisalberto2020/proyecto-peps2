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
            productos.append(Producto(producto[0], producto[1], float(producto[2]), producto[3]))

        return productos


    def delete_producto(self, id:int):
        cursor = self.useDatabase()
        cursor.execute("DELETE FROM productos WHERE id = %s", (id,))
        self.mydb.commit()
        self.mydb.close()


    def update_producto(self, id:int, nombre:str, precio:float, url:str):
        cursor = self.useDatabase()
        cursor.execute(
            "UPDATE productos SET nombre = %s, precio = %s, url = %s WHERE id = %s", 
            (nombre, precio, url, id)
        )
        self.mydb.commit()
        self.mydb.close()



    def get_producto(self, id:int) -> Producto:
        cursor = self.useDatabase()
        cursor.execute("SELECT * FROM productos WHERE id = %s", (id,))
        result = cursor.fetchone()
        self.mydb.commit()
        self.mydb.close()

        return Producto(result[0], result[1], float(result[2]), result[3])

