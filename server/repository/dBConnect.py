import mysql.connector
import os

class dBConnector():
    
    host = os.environ.get('DB_HOST')
    port = os.environ.get('DB_PORT')
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')
    
    def connect(self):
        try:
            self.mydb = mysql.connector.connect(
                host= self.host,
                port = self.port,
                user = self.user,
                password = self.password,
            )
        except Exception as e:
            print("Error: al connectarse ", e)

    def getCursor(self):
        return self.mydb.cursor()


    def close(self):
        self.mydb.close()


    def createDatabase(self):
        self.connect()
        cursor =self.getCursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS tienda")
        self.mydb.commit()

        self.mydb.close()

    def useDatabase(self):
        self.connect()
        self.getCursor().execute("USE tienda")
        return self.mydb.cursor()

    def createTables(self):
        self.connect()
        cursor = self.useDatabase()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS productos"+
             "(id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(50)," +
             " precio DECIMAL(10,2), url VARCHAR(255))"
            )
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS usuarios"+
                "(id INT AUTO_INCREMENT PRIMARY KEY,"+
                "email VARCHAR(150) UNIQUE, password VARCHAR(255),admin BOOLEAN, dinero Decimal(10,2))"
        )
        self.mydb.commit()
        self.mydb.close()

            

