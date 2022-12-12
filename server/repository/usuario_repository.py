from repository.dBConnect import dBConnector
from hashlib import sha256


class UsuariosRepository(dBConnector):
    def crear_usuario(self, email:str, password:str,admin:bool):
        cursor = self.useDatabase()
        password_encrypted = sha256(password.encode()).hexdigest()

        cursor.execute(
            "INSERT INTO usuarios (email, password, admin, dinero) VALUES (%s, %s, %s,0)", 
            (email, password_encrypted, admin)
        )
        self.mydb.commit()
        self.mydb.close()

    def login_usuario(self, email:str, password:str):
        cursor = self.useDatabase()
        password_encrypted = sha256(password.encode()).hexdigest()

        cursor.execute(
            "SELECT * FROM usuarios WHERE email = %s AND password = %s", 
            (email, password_encrypted)
        )
        result = cursor.fetchone()
        self.mydb.commit()
        self.mydb.close()
        return result 