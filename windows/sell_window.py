from tkinter import Canvas, Entry, Button, Listbox
import tkinter as tk
from PIL import Image, ImageTk
from modules.sales import Sales
from modules.database import DataBase

active_entry = None

def sell_window(window):

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
    text="Efetuar Venda",
    fill="#FFFFFF",
    font=("Arial-Bold", 55 * -1)
    )

    canvas.create_text(
    100.0,
    190.0,
    anchor="nw",
    text="Nome do Produto:",
    fill="#FFFFFF",
    font=("Arial", 22 * -1)
    )

    product_name_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 18)
    )

    product_name_entry.place (
        x=600.0,
        y=215.0,
        width=650.0,
        height=30.0
    )

    canvas.create_text(
    100.0,
    250.0,
    anchor="nw",
    text="Nome do Cliente:",
    fill="#FFFFFF",
    font=("Arial", 22 * -1)
    )

    customer_name_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 18)
    )

    customer_name_entry.place (
        x=600.0,
        y=275.0,
        width=650.0,
        height=30.0
    )

    canvas.create_text(
    100.0,
    310.0,
    anchor="nw",
    text="CPF:",
    fill="#FFFFFF",
    font=("Arial", 22 * -1)
    )

    cpf_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 18)
    )

    cpf_entry.place (
        x=600.0,
        y=335.0,
        width=650.0,
        height=30.0
    )

    canvas.create_text(
    100.0,
    370.0,
    anchor="nw",
    text="Quantidade:",
    fill="#FFFFFF",
    font=("Arial", 22 * -1)
    )

    amount_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 18)
    )

    amount_entry.place (
        x=600.0,
        y=395.0,
        width=650.0,
        height=30.0
    )

    canvas.create_text(
    100.0,
    430.0,
    anchor="nw",
    text="Preço Unitário:",
    fill="#FFFFFF",
    font=("Arial", 22 * -1)
    )

    price_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 18)
    )

    price_entry.place (
        x=600.0,
        y=455.0,
        width=650.0,
        height=30.0
    )
    sale_id_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
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

    ok_button = Button (text="Efetuar Venda", command=lambda:Sales(sale_id_entry, product_name_entry, customer_name_entry, cpf_entry, amount_entry, price_entry, new_quantity_entry, difference_entry, console_text, window1).sell())

    ok_button.place(
        x=850.0,
        y=495.0,
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
        y=530.0,
        width=650.0,
        height=200.0
    )
    # Função para autocompletar enquanto o usuário digita
    def on_type_product(event=None):
        typed_text = product_name_entry.get().strip()
        console_text.delete(0, tk.END)
        
        if not typed_text:
            return
        
        DataBase().connect()
        filtered = DataBase().read("SELECT Produto FROM Produtos WHERE Produto LIKE ?", [f"%{typed_text}%"])
        DataBase().close_connection()
        
        nomes_filtrados = [product[0] for product in filtered] if filtered else ["Nenhum produto encontrado"]
        for nome in nomes_filtrados:
            console_text.insert(tk.END, nome)

    # Função para autocompletar conforme o usuário digita
    def on_type_customer(event=None):
        typed_text = customer_name_entry.get().strip()
        console_text.delete(0, tk.END)
        
        if not typed_text:
            return
        
        DataBase().connect()
        filtered = DataBase().read("SELECT Nome FROM Clientes WHERE Nome LIKE ?", [f"%{typed_text}%"])
        DataBase().close_connection()
        
        nomes_filtrados = [customer[0] for customer in filtered] if filtered else ["Nenhum cliente encontrado"]
        for nome in nomes_filtrados:
            console_text.insert(tk.END, nome)
            
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
        
        if selected_text not in ["Nenhum cliente encontrado", "Nenhum produto encontrado"]:
            
            active_entry.delete(0, tk.END)
            active_entry.insert(0, selected_text)

            if active_entry == customer_name_entry:
                request = DataBase().read("SELECT CPF FROM Clientes WHERE Nome = ?", [selected_text])
                if request:
                    cpf_entry.delete(0, tk.END)
                    cpf_entry.insert(0, request[0][0])
            elif active_entry == product_name_entry:
                request = DataBase().read("SELECT * FROM Produtos WHERE Produto = ?", [selected_text])

                if request:
                    product_image = Image.open(f"images/{request[0][5]}")
                    product_image = product_image.resize((200, 300))
                    product_image_tk = ImageTk.PhotoImage(product_image)

                    canvas.create_image(800, 100, image=product_image_tk, anchor="nw")
                    canvas.image = product_image_tk  # Garante que o GC não apague a imagem -> quente!

                    price_entry.delete(0, tk.END)
                    price = request[0][2]
                    price = f"{price:.2f}"
                    price = str(price)
                    price = price.replace(".", ",")
                    price_entry.insert(0, price)

    product_name_entry.bind("<KeyRelease>", on_type_product)
    customer_name_entry.bind("<KeyRelease>", on_type_customer)
    console_text.bind("<<ListboxSelect>>", on_click_suggestion)

    product_name_entry.bind("<FocusIn>", lambda e: set_active_entry(product_name_entry))
    customer_name_entry.bind("<FocusIn>", lambda e: set_active_entry(customer_name_entry))

    window1.product_name_entry = product_name_entry
    window1.customer_name_entry = customer_name_entry
    window1.cpf_entry = cpf_entry
    window1.amount_entry = amount_entry
    window1.price_entry = price_entry
    window1.ok_button = ok_button
    window1.console_text = console_text

    return window1

def sell_window_on_click(window, result):

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
    text="Efetuar Venda",
    fill="#FFFFFF",
    font=("Arial-Bold", 55 * -1)
    )

    canvas.create_text(
    100.0,
    190.0,
    anchor="nw",
    text="Nome do Produto:",
    fill="#FFFFFF",
    font=("Arial", 22 * -1)
    )

    product_name_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 18)
    )

    product_name_entry.place (
        x=600.0,
        y=215.0,
        width=650.0,
        height=30.0
    )

    canvas.create_text(
    100.0,
    250.0,
    anchor="nw",
    text="Nome do Cliente:",
    fill="#FFFFFF",
    font=("Arial", 22 * -1)
    )

    customer_name_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 18)
    )

    customer_name_entry.place (
        x=600.0,
        y=275.0,
        width=650.0,
        height=30.0
    )

    canvas.create_text(
    100.0,
    310.0,
    anchor="nw",
    text="CPF:",
    fill="#FFFFFF",
    font=("Arial", 22 * -1)
    )

    cpf_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 18)
    )

    cpf_entry.place (
        x=600.0,
        y=335.0,
        width=650.0,
        height=30.0
    )

    canvas.create_text(
    100.0,
    370.0,
    anchor="nw",
    text="Quantidade:",
    fill="#FFFFFF",
    font=("Arial", 22 * -1)
    )

    amount_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 18)
    )

    amount_entry.place (
        x=600.0,
        y=395.0,
        width=650.0,
        height=30.0
    )

    canvas.create_text(
    100.0,
    430.0,
    anchor="nw",
    text="Preço Unitário:",
    fill="#FFFFFF",
    font=("Arial", 22 * -1)
    )

    price_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 18)
    )

    price_entry.place (
        x=600.0,
        y=455.0,
        width=650.0,
        height=30.0
    )
    sale_id_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
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

    ok_button = Button (text="Efetuar Venda", command=lambda:Sales(sale_id_entry, product_name_entry, customer_name_entry, cpf_entry, amount_entry, price_entry, new_quantity_entry, difference_entry, console_text, window1).sell())

    ok_button.place(
        x=850.0,
        y=495.0,
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
        y=530.0,
        width=650.0,
        height=200.0
    )

    product_name_entry.delete(0, tk.END)
    product_name_entry.insert(0, result[0][1])

    price_entry.delete(0, tk.END)
    price_entry.insert(0, result[0][2])

    # Função para autocompletar enquanto o usuário digita
    def on_type_product(event=None):
        typed_text = product_name_entry.get().strip()
        console_text.delete(0, tk.END)
        
        if not typed_text:
            return
        
        DataBase().connect()
        filtered = DataBase().read("SELECT Produto FROM Produtos WHERE Produto LIKE ?", [f"%{typed_text}%"])
        DataBase().close_connection()
        
        nomes_filtrados = [product[0] for product in filtered] if filtered else ["Nenhum produto encontrado"]
        for nome in nomes_filtrados:
            console_text.insert(tk.END, nome)

    # Função para autocompletar conforme o usuário digita
    def on_type_customer(event=None):
        typed_text = customer_name_entry.get().strip()
        console_text.delete(0, tk.END)
        
        if not typed_text:
            return
        
        DataBase().connect()
        filtered = DataBase().read("SELECT Nome FROM Clientes WHERE Nome LIKE ?", [f"%{typed_text}%"])
        DataBase().close_connection()
        
        nomes_filtrados = [customer[0] for customer in filtered] if filtered else ["Nenhum cliente encontrado"]
        for nome in nomes_filtrados:
            console_text.insert(tk.END, nome)
            
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
        
        if selected_text not in ["Nenhum cliente encontrado", "Nenhum produto encontrado"]:
            
            active_entry.delete(0, tk.END)
            active_entry.insert(0, selected_text)

            if active_entry == customer_name_entry:
                request = DataBase().read("SELECT CPF FROM Clientes WHERE Nome = ?", [selected_text])
                
                if request:
                    cpf_entry.delete(0, tk.END)
                    cpf_entry.insert(0, request[0][0])

    product_name_entry.bind("<KeyRelease>", on_type_product)
    customer_name_entry.bind("<KeyRelease>", on_type_customer)
    console_text.bind("<<ListboxSelect>>", on_click_suggestion)

    product_name_entry.bind("<FocusIn>", lambda e: set_active_entry(product_name_entry))
    customer_name_entry.bind("<FocusIn>", lambda e: set_active_entry(customer_name_entry))

    console_text.bind("<FocusIn>", lambda e: set_active_entry(console_text))

    if result:

        canvas.place(x=0, y=0)

        for products in result:
            product_image = Image.open(f"images/{products[5]}")  # Coluna 5 deve ser o nome do arquivo
            product_image = product_image.resize((200, 300))
            product_image_tk = ImageTk.PhotoImage(product_image)

            canvas.create_image(800, 100, image=product_image_tk, anchor="nw")
            canvas.image = product_image_tk  # Evita que a imagem seja deletada pelo Garbage Collector
                        
            price_entry.delete(0, tk.END)
            price = result[0][2]
            price = f"{price:.2f}"
            price = str(price)
            price = price.replace(".", ",")
            price_entry.insert(0, price)

    window1.product_name_entry = product_name_entry
    window1.customer_name_entry = customer_name_entry
    window1.cpf_entry = cpf_entry
    window1.amount_entry = amount_entry
    window1.price_entry = price_entry
    window1.ok_button = ok_button
    window1.console_text = console_text

    return window1