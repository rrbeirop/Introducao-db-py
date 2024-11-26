import tkinter as tk
from tkinter import ttk, messagebox 
import database as db
from PIL import Image, ImageTk

def listagem_registros():
    nova_janela = tk.Toplevel()
    nova_janela.title("Listagem de Registros")
    nova_janela.geometry("600x600")

    label_titulo = tk.Label(nova_janela, text="Listagem de Imoveis")
    label_titulo.grid(row=0, column=0, columnspan=2, pady=10)

    colunas = ("id_imovel", "tipo_imovel", "endereco", "valor", "descricao", "status")
    tabela_imoveis = ttk.Treeview(nova_janela, columns=colunas, show="headings")
    tabela_imoveis.grid(row=1, column=0, columnspan=2, sticky="nsew")

    # Configura o cabeçalho da coluna
    tabela_imoveis.heading("id_imovel", text="Id")
    tabela_imoveis.heading("tipo_imovel", text="Imóvel")
    tabela_imoveis.heading("endereco", text="Endereço")
    tabela_imoveis.heading("valor", text="Valor")
    tabela_imoveis.heading("descricao", text="Descrição")
    tabela_imoveis.heading("status", text="Status")

    # Especifica o tamanho das colunas
    tabela_imoveis.column("id_imovel", width=50)
    tabela_imoveis.column("tipo_imovel", width=50)
    tabela_imoveis.column("valor", width=50)
    tabela_imoveis.column("descricao", width=250)
    tabela_imoveis.column("status", width=100)

    btn_lista_produtos = tk.Button(nova_janela, text="Listagem de Imóveis", command=lambda: carregar_imoveis())
    btn_lista_produtos.grid(row=2, column=0, pady=10)

    def carregar_imoveis():
        registros = db.buscar_imoveis("imoveis")
        for registro in registros:
            tabela_imoveis.insert('', tk.END, values=registro)
    
    def excluir_produtos():
        selected_item = tabela_imoveis.selection()
        if selected_item:
            item = tabela_imoveis.item(selected_item)
            produto_id = item['values'][0]
            db.excluir_imovel(produto_id)

    def editar_imoveis():
        selected_item = tabela_imoveis.selection()
        if selected_item:
            item = tabela_imoveis.item(selected_item)
            id_imv = item['values'][0]
            abrir_janela_editar_imoveis(id_imv)
    
    def aplicar_filtro():
        for item in tabela_imoveis.get_children():
            tabela_imoveis.delete(item)
        registros_filtro = db.buscar_imoveis_nome(entry_tipo_imovel.get())
        for registro in registros_filtro:
            tabela_imoveis.insert("", "end", values=(
                registro.get("id_imovel", ""),
                registro.get("tipo_imovel", ""),
                registro.get("status", ""),
                registro.get("descricao", ""),
                registro.get("status", ""),
            ))

    # Label e Entrada para filtro
    tk.Label(nova_janela, text="Procurar").grid(row=3, column=0, pady=10)
    entry_tipo_imovel = tk.Entry(nova_janela, width=50)
    entry_tipo_imovel.grid(row=4, column=0, pady=10)

    # Botão para filtrar
    btn_filtro = tk.Button(nova_janela, text="Filtrar", command=lambda: aplicar_filtro())
    btn_filtro.grid(row=5, column=0, pady=10)

    # Botões de editar e deletar
    btn_editar_imoveis = tk.Button(nova_janela, text="Editar Item Selecionado", command=lambda: editar_imoveis())
    btn_editar_imoveis.grid(row=6, column=0, pady=10)
    
    btn_delete = tk.Button(nova_janela, text="Deletar Item selecionado", command=lambda: excluir_produtos())
    btn_delete.grid(row=7, column=0, pady=10)


def abrir_janela_cadrastra_imoveis():
    def limpa_campo():
        input_tipo_imovel.delete(0, tk.END)
        input_endereco.delete(0, tk.END)
        input_descricao.delete(0, tk.END)
        input_valor.delete(0, tk.END)
        input_status.delete(0, tk.END)
    
    def salva_imovel():
        db.cadrastar_imoveis(input_tipo_imovel.get(),
            input_endereco.get(),
            input_valor.get(),
            input_descricao.get(),
            input_status.get())
        limpa_campo()

    nova_janela = tk.Toplevel()
    nova_janela.title("Cadastro de Imóveis")
    nova_janela.geometry("600x400")

    label_tipo_imovel = tk.Label(nova_janela, text="Tipo do Imóvel")
    label_tipo_imovel.grid(row=0, column=0, pady=10)
    input_tipo_imovel = tk.Entry(nova_janela)
    input_tipo_imovel.grid(row=0, column=1, pady=10)

    label_endereco = tk.Label(nova_janela, text="Endereço do Imóvel")
    label_endereco.grid(row=1, column=0, pady=10)
    input_endereco = tk.Entry(nova_janela)
    input_endereco.grid(row=1, column=1, pady=10)

    label_descricao = tk.Label(nova_janela, text="Descrição do Imóvel")
    label_descricao.grid(row=2, column=0, pady=10)
    input_descricao = tk.Entry(nova_janela)
    input_descricao.grid(row=2, column=1, pady=10)

    label_valor = tk.Label(nova_janela, text="Valor do Imóvel")
    label_valor.grid(row=3, column=0, pady=10)
    input_valor = tk.Entry(nova_janela)
    input_valor.grid(row=3, column=1, pady=10)

    label_status = tk.Label(nova_janela, text="Status do Imóvel")
    label_status.grid(row=4, column=0, pady=10)
    input_status = tk.Entry(nova_janela)
    input_status.grid(row=4, column=1, pady=10)

    # Botão de cadastrar
    btn_cadrasta_imovel = tk.Button(nova_janela, text="Cadastrar", command=lambda: salva_imovel())
    btn_cadrasta_imovel.grid(row=5, column=0, columnspan=2, pady=10)


def abrir_janela_editar_imoveis(id_imoveis):
    lancamentos = db.buscar_imoveis_id(id_imoveis)

    nova_janela = tk.Toplevel()
    nova_janela.title("Editar Registro")
    nova_janela.geometry("300x400")

    tk.Label(nova_janela, text="Id do Imóvel").grid(row=0, column=0, pady=10)
    entry_id = tk.Entry(nova_janela)
    entry_id.insert(0, str(id_imoveis))
    entry_id.config(state="disabled")
    entry_id.grid(row=0, column=1, pady=10)

    tk.Label(nova_janela, text="Tipo do Imóvel").grid(row=1, column=0, pady=10)
    entry_tp_imovel = tk.Entry(nova_janela)
    entry_tp_imovel.grid(row=1, column=1, pady=10)
    entry_tp_imovel.insert(0, str(lancamentos.get("tipo_imovel")))

    tk.Label(nova_janela, text="Endereço do Imóvel").grid(row=2, column=0, pady=10)
    entry_endereco = tk.Entry(nova_janela)
    entry_endereco.grid(row=2, column=1, pady=10)
    entry_endereco.insert(0, str(lancamentos.get("endereco")))

    tk.Label(nova_janela, text="Descrição do Imóvel").grid(row=3, column=0, pady=10)
    entry_descricao = tk.Entry(nova_janela)
    entry_descricao.grid(row=3, column=1, pady=10)
    entry_descricao.insert(0, str(lancamentos.get("descricao")))

    tk.Label(nova_janela, text="Valor do Imóvel").grid(row=4, column=0, pady=10)
    entry_valor = tk.Entry(nova_janela)
    entry_valor.grid(row=4, column=1, pady=10)
    entry_valor.insert(0, str(lancamentos.get("valor")))

    tk.Label(nova_janela, text="Status do Imóvel").grid(row=5, column=0, pady=10)
    entry_status = tk.Entry(nova_janela)
    entry_status.grid(row=5, column=1, pady=10)
    entry_status.insert(0, str(lancamentos.get("status")))

    btn_salvar_alt = tk.Button(nova_janela, text="Salvar Alteração", command=lambda: db.atualizar_imovel(entry_id.get(),
                                                                                                       entry_tp_imovel.get(),
                                                                                                       entry_descricao.get(),
                                                                                                       entry_endereco.get(),
                                                                                                       entry_valor.get(),
                                                                                                       entry_status.get()))
    btn_salvar_alt.grid(row=6, column=0, columnspan=2, pady=10)


def tela_principal():
    root = tk.Tk()
    root.title("Mercadinho do Zé")
    root.geometry("600x600")
    
    input_clientes = tk.Entry(root)
    input_clientes.grid(row=0, column=0, pady=5)

    registros_texto = tk.Label(root, text="", justify='left', anchor='center')
    registros_texto.grid(row=1, column=0, pady=10)

    btn_abrir_lista_imoveis = tk.Button(root, text="Visualizar Imóveis", command=lambda: listagem_registros())
    btn_abrir_lista_imoveis.grid(row=2, column=0, pady=10)

    btn_abrir_janela_cadrasta_imoveis = tk.Button(root, text="Cadastrar Imóveis", command=abrir_janela_cadrastra_imoveis)
    btn_abrir_janela_cadrasta_imoveis.grid(row=3, column=0, pady=10)

    root.mainloop()
