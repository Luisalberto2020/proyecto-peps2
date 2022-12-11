import mysql.connector
class dBConnector():
    def connect(self):
        try:
            self.mydb = mysql.connector.connect(
                host="db",
                port = 3306,
                user = "root",
                password = "root",
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

            

