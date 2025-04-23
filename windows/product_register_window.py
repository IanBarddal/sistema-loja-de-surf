from tkinter import Canvas, Entry, Listbox, Button, Listbox
import tkinter as tk
from modules.products import Products
from modules.database import DataBase

def product_register_window(window):

    window1 = tk.Frame(window, bg="#278ee3", width=1100, height=900)
    window1.place(x=500, y=0)

    canvas = Canvas(window1,
    bg = "#278ee3",
    height = 900,
    width = 1100,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)

    canvas.create_rectangle(
    0.0,
    0.0,
    1100.0,
    900.0,
    fill="#278ee3",
    outline="")

    canvas.create_text(
    200.0,
    70.0,
    anchor="nw",
    text="Cadastrar Produto",
    fill="#FFFFFF",
    font=("Arial-Bold", 55 * -1)
    )

    canvas.create_text(
    100.0,
    200.0,
    anchor="nw",
    text="Nome do Produto:",
    fill="#FFFFFF",
    font=("Arial", 36 * -1)
    )

    canvas.create_text(
        100.0,
        300.0,
        anchor="nw",
        text="Preço Unitário:",
        fill="#FFFFFF",
        font=("Arial", 36 * -1)
    )

    canvas.create_text(
        100.0,
        400.0,
        anchor="nw",
        text="Quantidade em Estoque:",
        fill="#FFFFFF",
        font=("Arial", 36 * -1)
    )

    name_product_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )
    name_product_entry.place(
        x=600.0,
        y=250.0,
        width=650.0,
        height=36.0
    )

    suggestion_box = Listbox(window1, font=("Arial", 16), height=5, bg="white")
    suggestion_box.place_forget()

    id_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )

    price_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )
    price_entry.place(
        x=600.0,
        y=350.0,
        width=650.0,
        height=36.0
    )

    stock_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )
    stock_entry.place(
        x=600.0,
        y=450.0,
        width=650.0,
        height=36.0
    )

    amount_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )

    console_text = Listbox (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )
    console_text.place(
        x=600.0,
        y=550.0,
        width=650.0,
        height=200.0
    )

    ok_button = Button (text="Cadastrar", command=lambda:Products(id_entry, name_product_entry, price_entry, stock_entry, amount_entry, console_text, window1).create_product())

    ok_button.place (x=850.0, y=505.0, width=157.0, height=29.0)

    # Função para autocompletar conforme o usuário digita
    def on_type_product(event=None):
        typed_text = name_product_entry.get().strip()
        console_text.delete(0, tk.END)

        if not typed_text:
            return
        
        DataBase().connect()
        filtered = DataBase().read("SELECT Produto FROM Produtos WHERE Produto LIKE ?", [f"%{typed_text}%"])
        DataBase().close_connection()

        nomes_filtrados = [customer[0] for customer in filtered] if filtered else ["Nenhum produto encontrado"]

        if nomes_filtrados:
            for nome in nomes_filtrados:
                console_text.insert(tk.END, nome)

    def on_select(event=None):
        selected_index = suggestion_box.curselection()
        if selected_index:
            name_product_entry.delete(0, tk.END)
            name_product_entry.insert(0, suggestion_box.get(selected_index))

    # Função para capturar o Enter e preencher o campo
    def on_enter(event):
        on_select()

    name_product_entry.bind("<KeyRelease>", on_type_product)
    suggestion_box.bind("<<ListboxSelect>>", on_select)
    name_product_entry.bind("<Return>", on_enter)

    window1.name_product_entry = name_product_entry
    window1.price_entry = price_entry
    window1.stock_entry = stock_entry
    window1.ok_button = ok_button
    window1.console_text = console_text

    return window1