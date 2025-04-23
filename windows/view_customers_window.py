from tkinter import Canvas, Entry, Listbox, Button
import tkinter as tk
from modules.customers import Customer
from modules.database import DataBase
from windows.edit_customer_window import *

def view_customers_window(window):
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
    text="Pesquisar Clientes",
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

    cpf_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )

    telephone_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )

    ok_button = Button (text="Pesquisar", command=lambda: Customer(id_entry, name_entry, cpf_entry, telephone_entry, console_text).get_customer())

    ok_button.place(
        x=750.0,
        y=300.0,
        width=157.0,
        height=29.0
    )

    ok_button_2 = Button (text="Pesquisar Todos os Clientes", command=lambda: Customer(id_entry, name_entry, cpf_entry, telephone_entry, console_text).get_all_customers())

    ok_button_2.place(
        x=950.0,
        y=300.0,
        width=157.0,
        height=29.0
    )

    console_text = Listbox (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 12)
    )
    console_text.place(
        x=600.0,
        y=350.0,
        width=650.0,
        height=200.0
    )

    window1.active_entry = None

    def on_type_name(event=None):
        typed_text = name_entry.get().strip()
        console_text.delete(0, tk.END)
        
        if not typed_text:
            return
        
        DataBase().connect()
        filtered = DataBase().read("SELECT Nome FROM Clientes WHERE Nome LIKE ?", [f"%{typed_text}%"])
        
        filtered_names = [customer[0] for customer in filtered] if filtered else ["Cliente não encontrado."]
        for names in filtered_names:
            console_text.insert(tk.END, names)

    def set_active_entry(entry):
        window1.active_entry = entry
                    
    def on_click_suggestion(event):
        try:
            selected_index = console_text.curselection()[0]
            selected_text = console_text.get(selected_index)
        except IndexError:
            return

        if selected_text not in ["Cliente não encontrado."]:
            if window1.active_entry:
                window1.active_entry.delete(0, tk.END)
                window1.active_entry.insert(0, selected_text)

            selected_text = str(selected_text)
            parts = selected_text.split('|')
            customer_name = None

            for part in parts:
                if "ID do Cliente:" in part:
                    customer_name = int(part.split(':')[1].strip())
                    break

            if window1.active_entry == name_entry:
                DataBase().connect()
                result = DataBase().read("SELECT * FROM Clientes WHERE ID = ?", [customer_name])
                DataBase().close_connection()

                if result:
                    edit_customer_window_on_click(window, result)

    name_entry.bind("<KeyRelease>", on_type_name)
    console_text.bind("<<ListboxSelect>>", on_click_suggestion)
    name_entry.bind("<FocusIn>", lambda e: set_active_entry(name_entry))

    window1.name_entry = name_entry
    window1.ok_button = ok_button
    window1.ok_button_2 = ok_button_2
    window1.console_text = console_text

    return window1