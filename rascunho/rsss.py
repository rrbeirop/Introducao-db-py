import mysql.connector
from mysql.connector import Error
import ui

class SqlDatabase:
    def __init__(self, host, user, password, database):
        try:
            self.connection = mysql.connector.connect(host=host, user=user,password=password,database = database)
            if self.connection.is_connected():
                print('conectado com mysql')
            else:
                print('erro na conexão')
        except:
            print("error")

    def findAll(self, table):
        query = f'select * from {table}'
        print(query)
        
if __name__ == "__main__":
    db = SqlDatabase(host ='127.0.0.1',
                     user = 'root',
                     password= '',
                     database= 'imobilaria'
                     )
    
table = db.connection.cursor()
table.execute('select * from cliente')
table = table.fetchall()
for i in table:
    print(i)
db.findAll('imobilaria')

ui.tela_pricipal()







def tela_principal():
    root = tk.Tk()
    root.title("Mercadinho do Zé")
    root.geometry("600x600")
    
    
    
    input_clientes = tk.Entry(root)
    input_clientes.pack(pady=5)

   
    registros_texto = tk.Label(root, text="", justify='left', anchor='center')
    registros_texto.pack(pady=10)

    def atualizar():
        resultado = db.buscar_td("cliente")  
        registros_texto.config(text=resultado)

    btn_listar = tk.Button(root, text="Listar Todos", command=lambda:atualizar())
    btn_listar.pack(pady=10)
    
    
    root.mainloop()
