import tkinter as tk
from tkinter import ttk, messagebox 
import database as db
from PIL import Image, ImageTk


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
    
    def  excluir_produtos():
        selected_item = tabela_imoveis.selection()
        
        if selected_item:
            item = tabela_imoveis.item(selected_item)
        
        produto_id = item['values'][0]
        db.excluir_imovel(produto_id)

    # icon_delete_img = Image.open("assets/delete.png").resize((16, 16))
    # icon = ImageTk.PhotoImage(icon_delete_img)

    btn_delete = tk.Button(nova_janela, text="Deletar Item selecionado", command=lambda:excluir_produtos())
    btn_delete.pack(pady=10)
        # for r in registros:
            # tabela_imoveis.delete(item)

def abrir_janela_cadrastra_imoveis():
    def limpa_campo():
        input_tipo_imovel.delete(0,tk.END)
        input_endereco.delete(0,tk.END)
        input_descricao.delete(0,tk.END)
        input_valor.delete(0,tk.END)
        input_status.delete(0,tk.END)
    
    def salva_imovel():
        db.cadrastar_imoveis(input_tipo_imovel.get(),
            input_endereco.get(),
            input_valor.get(),
            input_descricao.get(),
            input_status.get())
        limpa_campo()

    nova_janela = tk.Toplevel()
    nova_janela.title("Cadastro de Imoveis")
    nova_janela.geometry("600x400")

    label_tipo_imovel = tk.Label(nova_janela,text= "Tipo do Imovel")
    label_tipo_imovel.pack(pady=0)
    input_tipo_imovel = tk.Entry(nova_janela)
    input_tipo_imovel.pack(pady=10)

    label_endereco = tk.Label(nova_janela,text= "Endereço do Imovel")
    label_endereco.pack(pady=0)
    input_endereco = tk.Entry(nova_janela)
    input_endereco.pack(pady=10)

    label_descricao = tk.Label(nova_janela,text= "Descrição do Imovel")
    label_descricao.pack(pady=0)
    input_descricao = tk.Entry(nova_janela)
    input_descricao.pack(pady=10)

    label_valor= tk.Label(nova_janela,text= "Valor do Imovel")
    label_valor.pack(pady=0)
    input_valor = tk.Entry(nova_janela)
    input_valor.pack(pady=10)

    
    label_status= tk.Label(nova_janela,text= "Status do Imovel")
    label_status.pack(pady=0)
    input_status = tk.Entry(nova_janela)
    input_status.pack(pady=10)

    # botao que vai cadrastrar no bd

    btn_cadrasta_imovel = tk.Button(nova_janela, text="Cadrastrar",command=lambda:salva_imovel)
    btn_cadrasta_imovel.pack(pady=10)

    
def tela_principal():
    root = tk.Tk()
    root.title("Mercadinho do Zé")
    root.geometry("600x600")
    # root['bg'] = '#062475'
    
    
    input_clientes = tk.Entry(root)
    input_clientes.pack(pady=5)

   
    registros_texto = tk.Label(root, text="", justify='left', anchor='center')
    registros_texto.pack(pady=10)

    # def atualizar():
        # resultado = db.buscar_td("cliente")  
        # registros_texto.config(text=resultado)


    # btn_listar = tk.Button(root, text="Listar Todos", command=lambda:atualizar())
    # btn_listar.pack(pady=10)
    
    btn_abrir_lista_imoveis = tk.Button(root, text="Visualizar Imoveis", command=lambda:listagem_registros())
    btn_abrir_lista_imoveis.pack(pady=10)

    btn_abrir_janela_cadrasta_imoveis = tk.Button(root, text= "Cadrastrar Imoveis", command=abrir_janela_cadrastra_imoveis)
    btn_abrir_janela_cadrasta_imoveis.pack(pady=10)
    root.mainloop()
