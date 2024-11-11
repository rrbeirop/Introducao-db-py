import mysql.connector

def conexao_banco():
    try: 
        cnx= mysql.connector.connect(
                    host ='127.0.0.1',
                     user = 'root',
                     password= '',
                     database= 'imobilaria'

        )   
        return cnx
    except:
        print ("Deu Erro na Conexão")

def buscar_todos(tabela):
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()
        query = "select * from Cliente where nome_cliente LIKE'%{}%' ".format(tabela)
        cursor.execute(query)
        registro = cursor.fetchall()
        print(registro)

    except: 
        print("n foi possivel selecionar todos da tabela {}".format(tabela))

    finally:
        cursor.close()

def buscar_td(tabela):
    try: 
        conexao = conexao_banco()
        cursor = conexao.cursor()
        query = "select nome_cliente from {}".format(tabela)
        cursor.execute(query)
        registros = cursor.fetchall()

        descricoes = "\n".join(registro[0] for registro in registros)
        return descricoes
    
    except: 
        print("n foi possivel selecionar todos da talb {}".format(tabela))

    finally:
        cursor.close()

def buscar_imoveis(tabela):
    try: 
        conexao = conexao_banco()
        cursor = conexao.cursor()
        query = "select * from {}".format(tabela)
        cursor.execute(query)
        imoveis = cursor.fetchall()

        return imoveis

    except: 
        print("n foi possivel selecionar todos da tables {}".format(tabela))

    finally:
        cursor.close()