import mysql.connector
from mysql.connector import Error

class SqlDatabase:
    def __init__(self, host, user, password, database):
        try:
            # Estabelece a conexão com o banco de dados
            self.connection = mysql.connector.connect(host=host, user=user, password=password, database=database)
            if self.connection.is_connected():
                print('Conectado com MySQL')
            else:
                print('Erro na conexão')
        except Error as e:
            print("Erro:", e)

    def show_tables(self):
        try:
            # Cria um cursor para executar a consulta
            cursor = self.connection.cursor()
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            print("Tabelas no banco de dados:")
            for table in tables:
                print(table[0])
        except Error as e:
            print("Erro ao listar as tabelas:", e)
        finally:
            cursor.close()

if __name__ == "__main__":
    db = SqlDatabase(host='127.0.0.1', user='root', password='', database='imobilaria')
    if db.connection.is_connected():
        db.show_tables()  # Chama o método para listar as tabelas
        db.connection.close()  # Fecha a conexão após o uso
