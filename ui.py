import tkinter as tk
from tkinter import ttk
import database as db 


def listagem_registros():
    nova_janela = tk.Toplevel()
    nova_janela.title("Listagem de Registros")
    nova_janela.geometry("600x600")

    label_titulo = tk.Label(nova_janela, text= "Listagem de Imoveis")
    label_titulo.pack(pady=10)

    colunas = ("id_imovel","tipo_imovel","endereco","valor","descricao", "status")
    tabela_imoveis = ttk.Treeview(nova_janela,columns=colunas,show="headings")
    tabela_imoveis.pack(fill="both")

    #configura o cabeçalho da coluna
    tabela_imoveis.heading("id_imovel",text= "Id")
    tabela_imoveis.heading("tipo_imovel",text= "Imovel")
    tabela_imoveis.heading("endereco",text= "Endereço")
    tabela_imoveis.heading("valor",text= "Valor")
    tabela_imoveis.heading("descricao",text= "Descrição")
    tabela_imoveis.heading("status",text= "Status")

    #Especificafr tamanho das colums
    tabela_imoveis.column("id_imovel", width=50)
    tabela_imoveis.column("tipo_imovel", width=50)

    tabela_imoveis.column("valor", width=50)
    tabela_imoveis.column("descricao",width=250)
    tabela_imoveis.column("status",width=100)

    btn_lista_produtos = tk.Button(nova_janela,text="Listagem de Imoveis",command=lambda:carregar_imoveis())
    btn_lista_produtos.pack(pady=10)

    def carregar_imoveis():
        registros = db.buscar_imoveis("imoveis")
        for registro in registros:
            tabela_imoveis.insert('',tk.END,values=registro)

        # for item in registros:
            # tabela_imoveis.delete(item)

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
    
    btn_abrir_lista_imoveis = tk.Button(root, text="Visualizar Imoveis", command=lambda:listagem_registros())
    btn_abrir_lista_imoveis.pack(pady=10)

    
    root.mainloop()
