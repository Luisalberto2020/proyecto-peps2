from controllers.dBConnect import dBConnector
from hashlib import sha256


class UsuariosRepository(dBConnector):
    def crear_usuario(self, email:str, password:str,admin:bool):
        cursor = self.useDatabase()
        password_encrypted = sha256(password.encode()).hexdigest()

        cursor.execute(
            "INSERT INTO usuarios (email, password, admin) VALUES (%s, %s, %s)", 
            (email, password_encrypted, admin)
        )
        self.mydb.commit()
        self.mydb.close()