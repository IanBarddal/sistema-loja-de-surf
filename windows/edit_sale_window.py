from tkinter import Canvas, Entry, Listbox, Button, END
import tkinter as tk
from PIL import Image, ImageTk
from modules.sales import Sales
from modules.database import DataBase

global event

def edit_sale_window(window):

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
    30.0,
    anchor="nw",
    text="Editar Venda",
    fill="#FFFFFF",
    font=("Arial-Bold", 55 * -1)
    )

    canvas.create_text(
    100.0,
    115.0,
    anchor="nw",
    text="ID da Venda:",
    fill="#FFFFFF",
    font=("Arial", 22 * -1)
    )

    canvas.create_text(
    100.0,
    180.0,
    anchor="nw",
    text="Nome do Produto:",
    fill="#FFFFFF",
    font=("Arial", 22 * -1)
    )

    sale_id_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )

    sale_id_entry.place (
        x=600.0,
        y=140.0,
        width=650.0,
        height=30.0
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
        y=205.0,
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

    new_amount_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )

    new_amount_entry.place (
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
    
    difference_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )

    ok_button = Button (text="Editar", command=lambda:Sales(sale_id_entry, product_name_entry, customer_name_entry, cpf_entry, amount_entry, price_entry, new_amount_entry, difference_entry, console_text, window1).edit_sale())

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

    quantity = new_amount_entry.get()

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

    def on_type_id(event=None):
        typed_text = sale_id_entry.get().strip()
        console_text.delete(0, tk.END)
        
        if not typed_text:
            return
        
        DataBase().connect()
        filtered = DataBase().read("SELECT ID FROM Vendas WHERE ID LIKE ?", [f"%{typed_text}%"])
        DataBase().close_connection()
        
        filteres_ids = [ids[0] for ids in filtered] if filtered else ["Nenhuma venda encontrada"]
        for ids in filteres_ids:
            console_text.insert(tk.END, ids)

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

    def on_click_suggestion():
        global active_entry

        try:
            selected_index = console_text.curselection()[0]
            selected_text = console_text.get(selected_index)
        except IndexError:
            return None
        
        if selected_text not in ["Nenhum cliente encontrado", "Nenhum produto encontrado", "Nenhuma venda encontrada"]:
            
            active_entry.delete(0, tk.END)
            active_entry.insert(0, selected_text)

            if active_entry == sale_id_entry:
                DataBase().connect()
                request = DataBase().read("SELECT * FROM Vendas WHERE ID = ?", [selected_text])
                DataBase().close_connection()

                if request:

                    customer_name_entry.delete(0, tk.END)
                    customer_name_entry.insert(0, request[0][1])

                    cpf_entry.delete(0, tk.END)
                    cpf_entry.insert(0, request[0][2])

                    product_name_entry.delete(0, tk.END)
                    product_name_entry.insert(0, request[0][3])

                    new_amount_entry.delete(0, tk.END)
                    new_amount_entry.insert(0, request[0][4])

                    products_request = DataBase().read("SELECT * FROM Produtos WHERE Produto = ?", [request[0][3]])
                    DataBase().close_connection()

                    if not products_request:
                        console_text.delete(0, tk.END)
                        console_text.insert(0, "Produto não está mais disponível.") 

                    price_entry.delete(0, tk.END)
                    price = products_request[0][2]
                    price = f"{price:.2f}"
                    price = str(price)
                    price = price.replace(".", ",")
                    price_entry.insert(0, price)

                    canvas.place(x=0, y=0)

                    product_image = Image.open(f"images/{products_request[0][5]}")  # Coluna 5 deve ser o nome do arquivo
                    product_image = product_image.resize((200, 300))
                    product_image_tk = ImageTk.PhotoImage(product_image)

                    canvas.create_image(800, 100, image=product_image_tk, anchor="nw")
                    canvas.image = product_image_tk  # Evita que a imagem seja deletada pelo Garbage Collector

            elif active_entry == customer_name_entry:
                DataBase().connect()
                client_request = DataBase().read("SELECT CPF FROM Clientes WHERE Nome = ?", [selected_text])
                DataBase().close_connection()
                
                if client_request:
                    cpf_entry.delete(0, tk.END)
                    cpf_entry.insert(0, client_request[0][0])
            
            elif active_entry == product_name_entry:
                DataBase().connect()
                product_request = DataBase().read("SELECT * FROM Produtos WHERE Produto = ?", [selected_text])
                DataBase().close_connection()

                if product_request:

                    canvas.place(x=0, y=0)

                    for products in product_request:
                        product_image = Image.open(f"images/{products[5]}")  # Coluna 5 deve ser o nome do arquivo
                        product_image = product_image.resize((200, 300))
                        product_image_tk = ImageTk.PhotoImage(product_image)

                        canvas.create_image(800, 100, image=product_image_tk, anchor="nw")
                        canvas.image = product_image_tk  # Evita que a imagem seja deletada pelo Garbage Collector

                        price_entry.delete(0, tk.END)
                        price = product_request[0][2]
                        price = f"{price:.2f}"
                        price = str(price)
                        price = price.replace(".", ",")
                        price_entry.insert(0, price)
                
    product_name_entry.bind("<KeyRelease>", on_type_product)
    customer_name_entry.bind("<KeyRelease>", on_type_customer)
    sale_id_entry.bind("<KeyRelease>", on_type_id)
    console_text.bind("<<ListboxSelect>>", lambda e: on_click_suggestion())

    product_name_entry.bind("<FocusIn>", lambda e: set_active_entry(product_name_entry))
    customer_name_entry.bind("<FocusIn>", lambda e: set_active_entry(customer_name_entry))
    sale_id_entry.bind("<FocusIn>", lambda e: set_active_entry(sale_id_entry))

    window1.sale_id_entry = sale_id_entry
    window1.product_name_entry = product_name_entry
    window1.customer_name_entry = customer_name_entry
    window1.cpf_entry = cpf_entry
    window1.new_amount_entry = new_amount_entry
    window1.price_entry = price_entry
    window1.ok_button = ok_button
    window1.console_text = console_text

    return window1

def edit_sale_window_on_click(window, result):

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
    30.0,
    anchor="nw",
    text="Editar Venda",
    fill="#FFFFFF",
    font=("Arial-Bold", 55 * -1)
    )

    canvas.create_text(
    100.0,
    115.0,
    anchor="nw",
    text="ID da Venda:",
    fill="#FFFFFF",
    font=("Arial", 22 * -1)
    )

    canvas.create_text(
    100.0,
    180.0,
    anchor="nw",
    text="Nome do Produto:",
    fill="#FFFFFF",
    font=("Arial", 22 * -1)
    )

    sale_id_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )

    sale_id_entry.place (
        x=600.0,
        y=140.0,
        width=650.0,
        height=30.0
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
        y=205.0,
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

    new_amount_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )

    new_amount_entry.place (
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
    
    difference_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )

    ok_button = Button (text="Editar", command=lambda:Sales(sale_id_entry, product_name_entry, customer_name_entry, cpf_entry, amount_entry, price_entry, new_amount_entry, difference_entry, console_text, window1).edit_sale())

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
                DataBase().close_connection()

                if request:

                    canvas.place(x=0, y=0)

                    for products in request:
                        product_image = Image.open(f"images/{products[5]}")  # Coluna 5 deve ser o nome do arquivo
                        product_image = product_image.resize((200, 300))
                        product_image_tk = ImageTk.PhotoImage(product_image)

                        canvas.create_image(800, 100, image=product_image_tk, anchor="nw")
                        canvas.image = product_image_tk  # Evita que a imagem seja deletada pelo Garbage Collector
                        
                    price_entry.delete(0, tk.END)
                    formatted_price = f"R$ {request[0][2]:.2f}".replace(".", ",")
                    price_entry.insert(0, formatted_price)

    product_name_entry.bind("<KeyRelease>", on_type_product)
    customer_name_entry.bind("<KeyRelease>", on_type_customer)
    console_text.bind("<<ListboxSelect>>", on_click_suggestion)

    product_name_entry.bind("<FocusIn>", lambda e: set_active_entry(product_name_entry))
    customer_name_entry.bind("<FocusIn>", lambda e: set_active_entry(customer_name_entry))

    canvas.place(x=0, y=0)

    for products in result:

        products_request = DataBase().read("SELECT * FROM Produtos WHERE Produto = ?", [result[0][3]])
        DataBase().close_connection()

        sale_id_entry.delete(0, tk.END)
        sale_id_entry.insert(0, result[0][0])

        product_name_entry.delete(0, tk.END)
        product_name_entry.insert(0, result[0][3])

        customer_name_entry.delete(0, tk.END)
        customer_name_entry.insert(0, result[0][1])

        cpf_entry.delete(0, tk.END)
        cpf_entry.insert(0, result[0][2])

        new_amount_entry.delete(0, tk.END)
        new_amount_entry.insert(0, result[0][4])

        if products_request:
            product_image = Image.open(f"images/{products_request[0][5]}")  # Coluna 5 deve ser o nome do arquivo
            product_image = product_image.resize((200, 300))
            product_image_tk = ImageTk.PhotoImage(product_image)

            canvas.create_image(800, 100, image=product_image_tk, anchor="nw")
            canvas.image = product_image_tk  # Evita que a imagem seja deletada pelo Garbage Collector

            price_entry.delete(0, tk.END)
            price = products_request[0][2]
            price = f"{price:.2f}"
            price = str(price)
            price = price.replace(".", ",")
            price_entry.insert(0, price)

        else:
            console_text.delete(0, tk.END)
            console_text.insert(0, "Produto não está mais disponível.")

    window1.sale_id_entry = sale_id_entry
    window1.product_name_entry = product_name_entry
    window1.customer_name_entry = customer_name_entry
    window1.cpf_entry = cpf_entry
    window1.new_amount_entry = new_amount_entry
    window1.price_entry = price_entry
    window1.ok_button = ok_button
    window1.console_text = console_text

    return window1