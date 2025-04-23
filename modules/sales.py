from tkinter import END
from datetime import datetime
from modules.database import DataBase
from tkinter import Canvas
from logs.log_class import Log
from support.verify import Verify
from support.requests_support import Requests

date_now = datetime.now()
date_formatted = date_now.strftime("%d/%m/%Y %H:%M")

class Sales():
    
    def __init__ (self, sale_id_entry, product_name_entry, customer_name_entry, cpf_entry, amount_entry, price_entry, new_quantity_entry, difference_entry, console_text, window1=None, database=None):
        self.sale_id_entry = sale_id_entry
        self.product_name_entry = product_name_entry
        self.customer_name_entry = customer_name_entry
        self.cpf_entry = cpf_entry
        self.amount_entry = amount_entry
        self.price_entry = price_entry
        self.new_quantity_entry = new_quantity_entry
        self.console_text = console_text
        self.difference_entry = difference_entry
        self.product_canvas = Canvas(window1, bg = "#ffffff", height = 300, width = 200, bd = 0, highlightthickness = 0, relief = "ridge")
        self.window1 = window1
        self.database = database or DataBase() # Separação necessária para os testes

    def get_all_sales(self):

        request = self.database.read("SELECT * FROM Vendas ORDER BY ID DESC")

        request_result = Requests(self.database, self.console_text).request_verify_get_all_sales(request)

        return request_result

    def get_sale(self): # Visualiza as vendas dos produtos

        sale_id = self.sale_id_entry.get()

        if not Verify(self.console_text).verify_if_get_sale_is_sale_id(sale_id):
            return

        request = self.database.read("SELECT * FROM Vendas WHERE ID = ?", [sale_id])

        request_verification = Requests(self.database, self.console_text, self.product_canvas).request_verify_get_sale(request, sale_id)

        return request_verification

    def sell(self): #Vende um produto

        product_name = self.product_name_entry.get()
        customer_name = self.customer_name_entry.get()
        cpf = self.cpf_entry.get()
        cpf = str(cpf)
        amount = self.amount_entry.get()
        price = self.price_entry.get()

        if not Verify(self.console_text).verify_if_sell_is_product_name(product_name):
            return
                
        if not Verify(self.console_text).verify_if_sell_is_customer_name(customer_name):
            return

        if not Verify(self.console_text).verify_if_sell_is_cpf(cpf):
            return
                
        if not Verify(self.console_text).verify_if_sell_amount_is_digit(amount):
            return
        
        if not Verify(self.console_text).verify_if_sell_amount_is_greater_than_zero(amount):
            return

        if not Verify(self.console_text).verify_if_sell_price_is_digit(price):
            return
        
        if not Verify(self.console_text).verify_if_sell_price_is_greater_than_zero(price):
            return
        
        amount = int(amount)
        price = price.replace(",",".")
        price = float(price)

        product_name_request = self.database.read("SELECT * FROM Produtos WHERE Produto = ?", [product_name])
        customer_name_request = self.database.read("SELECT * FROM Clientes WHERE Nome = ?", [customer_name])

        requests_group = Requests(self.database, self.console_text)

        product_request_verification_name = requests_group.request_verify_if_sell_is_product(product_name_request)
        product_request_verification_stock = requests_group.request_verify_if_sell_is_stock(product_name_request, amount)
        customer_request_verification_name = requests_group.request_verify_if_sell_is_customer(customer_name_request)
        customer_request_verification_cpf = requests_group.request_verify_if_sell_is_cpf(customer_name_request, customer_name, cpf)

        if not product_request_verification_name or not product_request_verification_stock or not customer_request_verification_name or not customer_request_verification_cpf:
            return
        
        else:
            self.database.update("UPDATE Produtos SET Estoque = Estoque - ? WHERE Produto = ?", [amount, product_name])
                
            self.total_value = amount * price

            self.total_value = float(self.total_value)
                
            self.database.create("INSERT INTO Vendas ('Cliente', 'CPF', 'Produto', 'Quantidade Vendida', 'Valor Total', 'Data da Venda') values (?, ?, ?, ?, ?, ?)", [customer_name, cpf, product_name, amount, self.total_value, date_formatted])

            self.console_text.delete(0, END)
            self.console_text.insert(0, "Venda concluída com sucesso.")
            Log("sale_success").log_info(f"Tentativa de cadastro de venda bem sucedida.")

            return customer_name, cpf, product_name, amount, self.total_value, date_formatted
                
    def edit_sale(self): # Edita uma venda

        sale_id = self.sale_id_entry.get()
        product_name = self.product_name_entry.get()
        customer_name = self.customer_name_entry.get()
        cpf = self.cpf_entry.get()
        new_amount = self.new_quantity_entry.get()
        price = self.price_entry.get()

        if not Verify(self.console_text).verify_if_edit_sale_is_id(sale_id):
            return
        
        if not Verify(self.console_text).verify_if_edit_sale_is_product_name(product_name):
            return
        
        if not Verify(self.console_text).verify_if_edit_sale_is_customer_name(customer_name):
            return
        
        if not Verify(self.console_text).verify_if_edit_sale_is_cpf(cpf):
            return

        if not Verify(self.console_text).verify_if_edit_sale_is_new_amount(new_amount):
            return
        
        if not Verify(self.console_text).verify_if_edit_sale_amount_is_greater_than_zero(new_amount):
            return
        
        if not Verify(self.console_text).verify_if_edit_sale_price_is_digit(price):
            return

        if not Verify(self.console_text).verify_if_edit_sale_price_is_greater_than_zero(price):
            return
        
        new_amount = int(new_amount)
        
        price = price.replace(",",".")
        price = float(price)

        customer_request = self.database.read("SELECT * FROM Clientes WHERE Nome = ?", [customer_name])
        product_request = self.database.read("SELECT * FROM Produtos WHERE Produto = ?", [product_name])
        id_request = self.database.read("SELECT * FROM Vendas WHERE ID = ?", [sale_id])

        requests_group = Requests(self.database, self.console_text)

        customer_request_verification_name = requests_group.request_verify_if_edit_sale_is_customer(customer_request)
        customer_request_verification_cpf = requests_group.request_verify_if_edit_sale_cpf_match(customer_request, customer_name, cpf)
        product_request_verification_name = requests_group.request_verify_if_edit_sale_product_exists(product_request)
        product_request_verification_stock = requests_group.request_verify_if_edit_sale_stock_support(product_request, new_amount)
        sale_id_request_verification = requests_group.request_verify_if_edit_sale_id_exists(id_request)

        if not customer_request_verification_name or not customer_request_verification_cpf or not product_request_verification_name or not product_request_verification_stock or not sale_id_request_verification:
            return
        else:
            total_value = new_amount * price # Faz um novo cálculo para o valor total

            new_product_request = self.database.read("SELECT * FROM Produtos WHERE Produto = ?", [product_name])

            # Atualiza os dados da venda no banco de dados
            self.database.update("UPDATE Vendas SET 'Cliente' = ?, 'CPF' = ?, 'Produto' = ?, 'Quantidade Vendida' = ?, 'Valor Total' = ? WHERE ID = ?", 
                               [customer_name, cpf, product_name, new_amount, total_value, sale_id])
        
            quantity_sold = id_request[0][4]

            # Pega os elementos para tratar as diferenças de quantidades em estoque, chamando a função necessária para isso logo em seguida

            old_product_request = self.database.read("SELECT * FROM Produtos WHERE Produto = ?", [id_request[0][3]])

            Verify(self.console_text).verify_edit_sale_quantities(old_product_request, new_product_request, new_amount, quantity_sold)

            self.console_text.delete(0, END)
            self.console_text.insert(0, "Venda editada com sucesso.")
            Log("sale_edit_success").log_info(f"Tentativa de edição de venda bem-sucedida.")

            return product_request

    def delete_sale(self): # Deleta uma venda

        sale_id = self.sale_id_entry.get() # Pede o ID da venda

        if not Verify(self.console_text).verify_delete_sale_not_id(sale_id): # Se o usuário não digitar um ID, reclama e sai da função
            return
        
        else: # Caso contrário, executa uma requisição ao banco
            request = self.database.read("SELECT * FROM Vendas WHERE ID = ?", [sale_id])

            # Executa uma verificação para ver se o ID da venda foi encontrado
            Requests(database=self.database, console_text=self.console_text).request_verify_if_delete_sale_is_sale_id(request, sale_id)

            if request:
                self.console_text.delete(0, END)
                self.console_text.insert(0, "Venda cancelada com sucesso.")
                Log("sale_delete_success").log_info(f"Tentativa de deletar a venda {sale_id} bem-sucedida.")