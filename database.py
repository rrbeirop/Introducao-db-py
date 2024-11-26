import mysql.connector
from tkinter import ttk, messagebox
import tkinter as tk

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


def buscar_imoveis_id(produto_id):
    try: 
        conexao = conexao_banco()
        cursor = conexao.cursor()
        query = "select * from imoveis where id_imovel={}".format(produto_id)
        cursor.execute(query)

        imoveis = cursor.fetchone()
        
        if imoveis:
            return {"id_imovel":imoveis[0],
                    "tipo_imovel":imoveis[1],
                    "endereco": imoveis [2],
                    "valor": imoveis[3],
                    "descricao":imoveis[4],
                    "status": imoveis[5]
            }   

    except: 
        messagebox.showerror("Alerta", "Não foi possivel encontrar o registro com esse id")

def buscar_imoveis_nome(tipo_imovel):
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()
        query = "SELECT * FROM imoveis WHERE tipo_imovel LIKE '%{}%'".format(tipo_imovel)
        cursor.execute(query)
        registros = cursor.fetchall()
 
        # for registro in registros:
        #     tree.insert("", tk.END, values=registro)
 
        resposta = []
        for row in registros:
            resposta = [{"id_imovel":row[0],
                          "tipo_imovel":row[1], 
                          "endereco":row[2],
                          "valor":row[3],
                          "descricao":row[4],
                          "status":row[5]
                          }]
 
        return resposta
   
    except:
        print("Não encontrei esse registro")
 
    finally:
        cursor.close()

def cadrastar_imoveis(tipo_imovel,endereco,valor,descricao,status):
    try: 
        conexao = conexao_banco()
        cursor = conexao.cursor()
        query = "INSERT INTO imoveis (tipo_imovel, endereco,valor,descricao,status) values (%s,%s,%s,%s,%s)"
        cursor.execute(query,(tipo_imovel,endereco,valor,descricao,status))
        conexao.commit()
        messagebox.showwarning('Sucesso' , 'Imovel Cadrastado com Sucesso')

    except: 
            messagebox.showwarning("Erro", "Não foi possivel Cadrastrar Imovel")

def excluir_imovel(produto_id):
    try: 
        conexao = conexao_banco()
        cursor = conexao.cursor()

        query = "DELETE FROM imoveis WHERE id_imovel = {}".format(produto_id)
        cursor.execute(query)
        conexao.commit()

        messagebox.showinfo("Imovel Excluido", "Este Imovel foi apagado")

    except:
        messagebox.showerror("ERRO", "Não foi possivel excluir o produto")

def atualizar_imovel(id_imovel, tipo_imovel, endereco, valor,descricao, status):
    try: 
        conexao = conexao_banco()
        cursor = conexao.cursor()

        query = """UPDATE imoveis set tipo_imovel = %s, endereco = %s, valor = %s, descricao = %s,status = %s 
        WHERE id_imovel = %s """
        cursor.execute(query, ( tipo_imovel, endereco, valor, descricao, status, id_imovel))
        conexao.commit()

        messagebox.showinfo("Atualizado")

    except:
        messagebox.showerror("AVISO", "Não foi possivel atualizar o registro") 


