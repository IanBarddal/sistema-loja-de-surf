from tkinter import Canvas, Entry, Listbox, Button
import tkinter as tk
from PIL import Image, ImageTk
from modules.products import Products
from modules.database import DataBase

def delete_product_window(window):
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
    text="Deletar Produto",
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

    stock_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
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
        y=350.0,
        width=650.0,
        height=200.0
    )

    ok_button = Button (text="Deletar", command=lambda:Products(id_entry, name_product_entry, price_entry, stock_entry, amount_entry, console_text, window1).delete_product())

    ok_button.place(
        x=850.0,
        y=300.0,
        width=157.0,
        height=29.0
    )

    def on_type_product(event=None):
        typed_text = name_product_entry.get().strip()
        console_text.delete(0, tk.END)
        
        if not typed_text:
            return
        
        DataBase().connect()
        filtered = DataBase().read("SELECT Produto FROM Produtos WHERE Produto LIKE ?", [f"%{typed_text}%"])
        
        filtered_names = [product[0] for product in filtered] if filtered else ["Produto não encontrado."]
        for products in filtered_names:
            console_text.insert(tk.END, products)

    def set_active_entry(entry):
        global active_entry
        active_entry = entry
                    
    def on_click_suggestion(event):
        global active_entry

        if not active_entry:
            return
        try:
            selected_index = console_text.curselection()[0]
            selected_text = console_text.get(selected_index)
        except IndexError:
            return
        
        if selected_text not in ["Produto não encontrado."]:

            active_entry.delete(0, tk.END)
            active_entry.insert(0, selected_text)

            selected_text = str(selected_text)

            products_request = DataBase().read("SELECT * FROM Produtos WHERE Produto = ?", [selected_text])
            DataBase().close_connection()
            
            product_image = Image.open(f"images/{products_request[0][5]}")
            product_image = product_image.resize((200, 300))
            product_image_tk = ImageTk.PhotoImage(product_image)

            canvas.create_image(800, 100, image=product_image_tk, anchor="nw")
            canvas.image = product_image_tk  # Garante que o GC não apague a imagem

    name_product_entry.bind("<KeyRelease>", on_type_product)
    console_text.bind("<<ListboxSelect>>", on_click_suggestion)
    name_product_entry.bind("<FocusIn>", lambda e: set_active_entry(name_product_entry))

    window1.name_product_entry = name_product_entry
    window1.ok_button = ok_button
    window1.console_text = console_text

    return window1