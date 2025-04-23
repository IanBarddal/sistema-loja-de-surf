from tkinter import END
from datetime import datetime
from modules.database import DataBase
from tkinter import filedialog
from tkinter import Canvas
from logs.log_class import Log
from support.verify import Verify
from support.requests_support import Requests
import os

date_now = datetime.now()
date_formatted = date_now.strftime("%d/%m/%Y %H:%M")

class Products():

    def __init__ (self, id_entry, name_product_entry, price_entry, stock_entry, amount_entry, console_text, window1=None, database=None):
        self.id_entry = id_entry
        self.name_product_entry = name_product_entry
        self.price_entry = price_entry
        self.stock_entry = stock_entry
        self.console_text = console_text
        self.amount_entry = amount_entry
        self.product_canvas = Canvas(window1, bg = "#ffffff", height = 300, width = 200, bd = 0, highlightthickness = 0, relief = "ridge")
        self.window1 = window1
        self.database = database or DataBase() # Separação necessária para os testes

    def get_all_products(self):

        self.console_text.delete(0, END) # Limpa o console para exibir novas mensagens

        request = self.database.read("SELECT * FROM Produtos ORDER BY ID DESC") # Faz a requisição ao banco

        request_group = Requests(self.database, self.console_text).request_verify_get_all_products_if_products_exist(request)

        return request_group

    def create_product(self):

        name = self.name_product_entry.get()
        price = self.price_entry.get()
        stock = self.stock_entry.get()

        verifications = Verify(self.console_text)
        
        if not verifications.verify_if_create_product_is_name(name):
            return
        
        if not verifications.verify_if_create_product_is_price(price):
            return
                
        if not verifications.verify_if_create_product_is_stock(stock):
            return
        
        if not verifications.verify_if_create_product_price_is_digit(price):
            return
        
        if not verifications.verify_if_create_product_stock_is_digit(stock):
            return
        
        if not verifications.verify_if_create_product_price_is_not_negative(price):
            return
        
        price = price.replace(",",".")
        price = float(price)
        
        product_name_request = self.database.read("SELECT * FROM Produtos WHERE Produto = ?", [name])

        Requests(self.database, self.console_text).request_verify_if_create_product_name_taken(product_name_request)
        
        if name and price and stock:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Insira uma imagem para o produto.")
        
        image = Products(self.id_entry, self.name_product_entry, self.price_entry, self.stock_entry, self.amount_entry, self.console_text, self.window1).choose_image()

        if not Verify(self.console_text).verify_if_create_product_is_image(image):
            return
        
        self.database.create("INSERT INTO Produtos ('Produto', 'Preço Unitário', 'Estoque', 'Data de Adição', 'Imagem') VALUES (?, ?, ?, ?, ?)",
                    [name, price, stock, date_formatted, image])

        self.console_text.delete(0, END)
        self.console_text.insert(0, "Produto cadastrado com sucesso.")
        Log("product_registered").log_info(f"Produto {name} cadastrado com sucesso: R$ {price}, estoque: {stock}, data: {date_formatted}.")

        return name, price, stock, date_formatted, image

    def delete_product(self): # Deleta um produto do banco de dados

        # Primeiro, verificamos se o produto realmente existe

        name = self.name_product_entry.get()

        request = self.database.read("SELECT * FROM Produtos WHERE Produto = ?", [name])

        # Caso seja encontrado, fazemos uma requisição ao banco de dados para deletá-lo, senão, imprime que ele não existe.

        request_verification = Requests(self.database, self.console_text).request_verify_if_delete_product_product_exists(request, name)

        return request_verification
        
    def get_product(self): # Consulta a existência de um produto
        
        # Antes de tudo, deve-se verificar se o produto realmente existe:

        name = self.name_product_entry.get()

        request = self.database.read("SELECT * FROM Produtos WHERE Produto = ?", [name])

        # Se existe, a função irá retornar os dados deles e carregar suas fotos; senão, emite um aviso dizendo que o produto não foi encontrado

        request_verification = Requests(self.database, self.console_text, self.product_canvas).request_verify_if_get_product_product_exists(request, name)

        return request_verification

    def update_stock(self): # Atualiza o estoque

        name = self.name_product_entry.get()
        product_id = self.id_entry.get()
        product_id = int(product_id)
        amount = self.amount_entry.get()

        if not Verify(self.console_text).verify_if_update_stock_is_name(name):
            return
        
        if not Verify(self.console_text).verify_if_update_stock_is_id(product_id):
            return
                
        if not Verify(self.console_text).verify_if_update_stock_is_amount(amount):
            return

        request_product = self.database.read("SELECT * FROM Produtos WHERE Produto = ?", [name])

        requests_group = Requests(self.database, self.console_text)
        
        requests_group.request_verify_if_update_stock_is_product(request_product)
        
        id_request = self.database.read("SELECT * FROM Produtos WHERE ID = ?", [product_id])

        # Através de uma busca pelo ID, vê se o produto casa com o ID; se não casar, não deixa atualizar, mas caso contrário, faz a atualização do estoque

        final_verification = requests_group.request_verify_if_update_stock_is_id(id_request, name, amount)

        return final_verification
    
    def choose_image(self):

        image = filedialog.askopenfilename()
        
        self.name_product_entry = self.name_product_entry.get()

        if image:
            get_file = os.path.basename(image)
            Log("products_image").log_info(f"Imagem carregada com sucesso para o produto {self.name_product_entry}")

            return get_file
        
        else:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Selecione uma imagem para o produto.")