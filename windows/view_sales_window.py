from tkinter import Canvas, Entry, Button, Listbox
import tkinter as tk
from modules.sales import Sales
from modules.database import DataBase
from windows.edit_sale_window import *

active_entry = None

def view_sales_window(window):

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
    text="Pesquisar Vendas",
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

    price_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 18)
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

    new_quantity_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )
    
    difference_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )

    ok_button = Button (text="Visualizar", command=lambda:Sales(sale_id_entry, product_name_entry, customer_name_entry, cpf_entry, amount_entry, price_entry, new_quantity_entry, difference_entry, console_text, window1).get_sale())

    ok_button.place(
        x=750.0,
        y=300.0,
        width=157.0,
        height=29.0
    )

    all_sales_button = Button (text="Visualizar Todas as Vendas", command=lambda:Sales(sale_id_entry, product_name_entry, customer_name_entry, cpf_entry, amount_entry, price_entry, new_quantity_entry, difference_entry, console_text, window1).get_all_sales())

    all_sales_button.place(
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

    def on_type_id(event=None):
        typed_text = sale_id_entry.get().strip()
        console_text.delete(0, tk.END)
        
        if not typed_text:
            return
        
        DataBase().connect()
        filtered = DataBase().read("SELECT ID FROM Vendas WHERE ID LIKE ?", [f"%{typed_text}%"])
        
        filtered_ids = [ids[0] for ids in filtered] if filtered else ["Venda não encontrada."]
        for sales_ids in filtered_ids:
            console_text.insert(tk.END, sales_ids)

    def set_active_entry(entry):
        global active_entry
        active_entry = entry

    def on_click_suggestion(event):
        global active_entry

        if active_entry == sale_id_entry:
        
            try:
                selected_index = console_text.curselection()[0]
                selected_text = console_text.get(selected_index)
            except IndexError:
                return
            
            if selected_text not in ["Venda não encontrada."]:
                active_entry.delete(0, tk.END)
                active_entry.insert(0, selected_text)

                if isinstance (selected_text, str):

                    parts = selected_text.split("|")
                    sale_id = parts[0].split(":")[1].strip()

                    result = DataBase().read("SELECT * FROM Vendas WHERE ID = ?", [sale_id])

                    if result:
                        edit_sale_window_on_click(window, result)

        else:
            try:
                selected_index = console_text.curselection()[0]
                selected_text = console_text.get(selected_index)
            except IndexError:
                return

            if selected_text not in ["Venda não encontrada."]:
                parts = selected_text.split("|")
                
                try:
                    parts_split = parts[3].split(":")
                    parts_product = parts_split[1].strip()
                except IndexError:
                    print(f"Erro ao processar produto: {selected_text}")
                    return
                
                DataBase().connect()
                product_result = DataBase().read("SELECT * FROM Produtos WHERE Produto = ?", [parts_product])
                DataBase().close_connection()

                for product in product_result:
                    canvas.place(x=0, y=0)
                    product_image = Image.open(f"images/{product[5]}")  # Coluna 5 = nome do arquivo da imagem
                    product_image = product_image.resize((200, 300))
                    product_image_tk = ImageTk.PhotoImage(product_image)

                    canvas.create_image(800, 100, image=product_image_tk, anchor="nw")
                    canvas.image = product_image_tk  # Evita que a imagem seja deletada pelo Garbage Collector

    # Bindings
    sale_id_entry.bind("<KeyRelease>", on_type_id)
    sale_id_entry.bind("<FocusIn>", lambda e: set_active_entry(sale_id_entry))
    console_text.bind("<<ListboxSelect>>", on_click_suggestion)

    window1.sale_id_entry = sale_id_entry
    window1.ok_button = ok_button
    window1.all_sales_button = all_sales_button
    window1.console_text = console_text

    return window1