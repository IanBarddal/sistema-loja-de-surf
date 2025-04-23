from tkinter import Canvas, Entry, Listbox, Button
import tkinter as tk
from modules.customers import Customer
from modules.database import DataBase

def edit_customer_window(window):
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
    text="Editar Cliente",
    fill="#FFFFFF",
    font=("Arial-Bold", 55 * -1)
    )

    canvas.create_text(
        100.0,
        210.0,
        anchor="nw",
        text="ID do Cliente (Não pode ser alterado):",
        fill="#FFFFFF",
        font=("Arial", 22 * -1)
    )

    canvas.create_text(
        100.0,
        280.0,
        anchor="nw",
        text="Nome do Cliente:",
        fill="#FFFFFF",
        font=("Arial", 22 * -1)
    )

    canvas.create_text(
        100.0,
        350.0,
        anchor="nw",
        text="CPF:",
        fill="#FFFFFF",
        font=("Arial", 22 * -1)
    )

    canvas.create_text(
        100.0,
        420.0,
        anchor="nw",
        text="Telefone (Digite apenas números):",
        fill="#FFFFFF",
        font=("Arial", 22 * -1)
    )

    id_entry = Entry(
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )

    id_entry.place(
        x=600.0,
        y=240.0,
        width=650.0,
        height=36.0
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
        y=310.0,
        width=650.0,
        height=36.0
    )

    cpf_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )
    cpf_entry.place(
        x=600.0,
        y=380.0,
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

    ok_button = Button (text="Editar", command=lambda: Customer(id_entry, name_entry, cpf_entry, telephone_entry, console_text).edit_customer())

    ok_button.place(
        x=850.0,
        y=505.0,
        width=157.0,
        height=29.0
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

    active_entry = None

    def on_type_name(event=None):
        typed_text = name_entry.get().strip()
        console_text.delete(0, tk.END)
        
        if not typed_text:
            return
        
        DataBase().connect()
        filtered = DataBase().read("SELECT Nome FROM Clientes WHERE Nome LIKE ?", [f"%{typed_text}%"])
        DataBase().close_connection()
        
        filtered_names = [customer[0] for customer in filtered] if filtered else ["Cliente não encontrado."]
        for names in filtered_names:
            console_text.insert(tk.END, names)

    def set_active_entry(entry):
        global active_entry
        active_entry = entry
                    
    def on_click_suggestion(event):
        global active_entry
        
        try:
            selected_index = console_text.curselection()[0]
            selected_text = console_text.get(selected_index)
        except IndexError:
            return
        
        if selected_text not in ["Cliente não encontrado."]:

            active_entry.delete(0, tk.END)
            active_entry.insert(0, selected_text)

            selected_text = str(selected_text)

            parts = selected_text.split('|')

            if active_entry == name_entry:

                DataBase().connect()
                result = DataBase().read("SELECT * FROM Clientes WHERE Nome = ?", [parts[0]])
                DataBase().close_connection()

                id_entry.delete(0, tk.END)
                id_entry.insert(0, result[0][0])

                name_entry.delete(0, tk.END)
                name_entry.insert(0, result[0][1])

                cpf_entry.delete(0, tk.END)
                cpf_entry.insert(0, result[0][2])

                telephone_entry.delete(0, tk.END)
                telephone_entry.insert(0, result[0][3])

    name_entry.bind("<KeyRelease>", on_type_name)
    console_text.bind("<<ListboxSelect>>", on_click_suggestion)
    name_entry.bind("<FocusIn>", lambda e: set_active_entry(name_entry))

    window1.id_entry = id_entry
    window1.name_entry = name_entry
    window1.cpf_entry = cpf_entry
    window1.telephone_entry = telephone_entry
    window1.ok_button = ok_button
    window1.console_text = console_text

    return window1

def edit_customer_window_on_click(window, result):

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
    text="Editar Cliente",
    fill="#FFFFFF",
    font=("Arial-Bold", 55 * -1)
    )

    canvas.create_text(
    100.0,
    210.0,
    anchor="nw",
    text="ID do Cliente (Não pode ser alterado):",
    fill="#FFFFFF",
    font=("Arial", 22 * -1)
    )

    canvas.create_text(
    100.0,
    280.0,
    anchor="nw",
    text="Nome do Cliente:",
    fill="#FFFFFF",
    font=("Arial", 22 * -1)
    )

    canvas.create_text(
        100.0,
        350.0,
        anchor="nw",
        text="CPF:",
        fill="#FFFFFF",
        font=("Arial", 22 * -1)
    )

    canvas.create_text(
        100.0,
        420.0,
        anchor="nw",
        text="Telefone (Digite apenas números):",
        fill="#FFFFFF",
        font=("Arial", 22 * -1)
    )

    id_entry = Entry(
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )

    id_entry.place(
        x=600.0,
        y=240.0,
        width=650.0,
        height=36.0
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
        y=310.0,
        width=650.0,
        height=36.0
    )

    cpf_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )
    cpf_entry.place(
        x=600.0,
        y=380.0,
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

    ok_button = Button (text="Editar", command=lambda: Customer(id_entry, name_entry, cpf_entry, telephone_entry, console_text).edit_customer())

    ok_button.place(
        x=850.0,
        y=505.0,
        width=157.0,
        height=29.0
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

    id_entry.delete(0, tk.END)
    id_entry.insert(0, result[0][0])

    name_entry.delete(0, tk.END)
    name_entry.insert(0, result[0][1])

    cpf_entry.delete(0, tk.END)
    cpf_entry.insert(0, result[0][2])

    telephone_entry.delete(0, tk.END)
    telephone_entry.insert(0, result[0][3])

    window1.id_entry = id_entry
    window1.name_entry = name_entry
    window1.cpf_entry = cpf_entry
    window1.telephone_entry = telephone_entry
    window1.ok_button = ok_button
    window1.console_text = console_text

    return window1