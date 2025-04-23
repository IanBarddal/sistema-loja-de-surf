from tkinter import Canvas, Entry, Listbox, Button
import tkinter as tk
from modules.sales import Sales
from modules.database import DataBase

def delete_sale_window(window):
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
    text="Cancelar Venda",
    fill="#FFFFFF",
    font=("Arial-Bold", 55 * -1)
    )

    canvas.create_text(
    100.0,
    200.0,
    anchor="nw",
    text="ID da Venda:",
    fill="#FFFFFF",
    font=("Arial", 36 * -1)
    )

    sale_id_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 18)
    )

    sale_id_entry.place (
        x=600.0,
        y=250.0,
        width=650.0,
        height=36.0
    )

    product_name_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 18)
    )

    customer_name_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 18)
    )

    cpf_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 18)
    )

    amount_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 18)
    )

    new_amount_entry = Entry (
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
        font=("Arial", 18)
    )
    
    difference_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )

    ok_button = Button (text="Cancelar", command=lambda:Sales(sale_id_entry, product_name_entry, customer_name_entry, cpf_entry, amount_entry, price_entry, new_amount_entry, difference_entry, console_text, window1).delete_sale())

    ok_button.place(
        x=850.0,
        y=300.0,
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
        y=350.0,
        width=650.0,
        height=200.0
    )

    def on_type_id(event=None):
        typed_text = sale_id_entry.get().strip()
        console_text.delete(0, tk.END)

        if not typed_text:
            return
        
        DataBase().connect()
        filtered = DataBase().read("SELECT ID FROM Vendas WHERE ID LIKE ?", [f"%{typed_text}%"])
        DataBase().close_connection()

        filtered_ids = [ids[0] for ids in filtered] if filtered else ["Nenhuma venda encontrada"]

        if filtered_ids:
            for sale_id in filtered_ids:
                console_text.insert(tk.END, sale_id)

    sale_id_entry.bind("<KeyRelease>", on_type_id)

    window1.sale_id_entry = sale_id_entry
    window1.ok_button = ok_button
    window1.console_text = console_text

    return window1