from tkinter import Canvas, Entry, Listbox, Button, Listbox
import tkinter as tk
from modules.customers import Customer
from modules.database import DataBase

def register_customer_window(window):
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
    text="Registrar Cliente",
    fill="#FFFFFF",
    font=("Arial-Bold", 55 * -1)
    )

    canvas.create_text(
    100.0,
    200.0,
    anchor="nw",
    text="Nome do Cliente:",
    fill="#FFFFFF",
    font=("Arial", 36 * -1)
    )

    canvas.create_text(
        100.0,
        300.0,
        anchor="nw",
        text="CPF:",
        fill="#FFFFFF",
        font=("Arial", 36 * -1)
    )

    canvas.create_text(
        100.0,
        400.0,
        anchor="nw",
        text="Telefone (Digite apenas números):",
        fill="#FFFFFF",
        font=("Arial", 36 * -1)
    )

    id_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )

    name_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )

    name_entry.place(
        x=600.0,
        y=250.0,
        width=650.0,
        height=36.0
    )

    suggestion_box = Listbox(window1, font=("Arial", 16), height=5, bg="white")
    suggestion_box.place_forget()

    cpf_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )
    cpf_entry.place(
        x=600.0,
        y=350.0,
        width=650.0,
        height=36.0
    )

    telephone_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )
    telephone_entry.place(
        x=600.0,
        y=450.0,
        width=650.0,
        height=36.0
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

    ok_button = Button (text="Cadastrar", command=lambda:Customer(id_entry, name_entry, cpf_entry, telephone_entry, console_text).register_customer())

    ok_button.place(
        x=850.0,
        y=505.0,
        width=157.0,
        height=29.0
    )

    # Função para autocompletar conforme o usuário digita
    def on_type(event=None):
        typed_text = name_entry.get().strip()
        console_text.delete(0, tk.END)

        if not typed_text:
            return
        
        DataBase().connect()
        filtered = DataBase().read("SELECT Nome FROM Clientes WHERE Nome LIKE ?", [f"%{typed_text}%"])
        DataBase().close_connection()

        nomes_filtrados = [customer[0] for customer in filtered] if filtered else ["Nenhum cliente encontrado"]

        if nomes_filtrados:
            for nome in nomes_filtrados:
                console_text.insert(0, nome)

    name_entry.bind("<KeyRelease>", on_type)

    window1.name_entry = name_entry
    window1.cpf_entry = cpf_entry
    window1.telephone_entry = telephone_entry
    window1.ok_button = ok_button
    window1.console_text = console_text
    
    return window1