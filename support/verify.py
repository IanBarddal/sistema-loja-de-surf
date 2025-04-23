from tkinter import END
from logs.log_class import Log
from modules.database import DataBase

class Verify():

    def __init__ (self, console_text, database=None):
        self.console_text = console_text
        self.database = database or DataBase()

    def verify_if_is_name(self, name):

        if not name:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'Nome' não pode estar vazio.")
            Log("customers_not_name").log_warning(f"Tentativa de cadastro de cliente sem nome.")
            
            return False
        
        else:
            return True
        
    def verify_if_is_cpf(self, cpf):

        if not cpf:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'CPF' não pode estar vazio.")
            Log("customers_not_cpf").log_warning(f"Tentativa de cadastro de cliente sem CPF.")
            
            return False
        
        else:
            return True
        
    def verify_if_is_telephone(self, telephone):

        if not telephone:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'Telefone' não pode estar vazio.")
            Log("customers_not_phone").log_warning(f"Tentativa de cadastro de cliente sem telefone.")
            
            return False
        
        else:
            return True
        
    def verify_if_cpf_is_digit(self, cpf):
        
        for char in cpf:
            if not (char.isdigit() or char in ".-"):
                self.console_text.delete(0, END)
                self.console_text.insert(0, "Campo 'CPF' só pode conter números, pontos e hífen.")
                Log("customers_cpf_invalid_chars").log_warning("Tentativa de cadastro de CPF com caracteres inválidos.")
                return False
        else:
            return True
            
    def verify_if_telephone_is_digit(self, telephone):

        if not telephone.isdigit():
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'Telefone' só pode conter números.")
            Log("customers_phone_not_digit").log_warning(f"Tentativa de cadastro de cliente com telefone não contendo apenas dígitos.")
            
            return False
        
        else:
            return True
        
    def verify_if_edit_is_id(self, customer_id):

        if not customer_id:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'ID do Cliente' não pode estar vazio.")
            Log("customers_edit_not_id").log_warning(f"Tentativa de edição de cadastro de cliente sem ID.")
            
            return False
        
        else:
            return True
        
    def verify_if_id_changes(self, current_id, name):

        result = self.database.read("SELECT ID FROM Clientes WHERE Nome = ?", [name])

        for row in result:
            if str(row[0]) != str(current_id) or result == []:
                self.console_text.delete(0, END)
                self.console_text.insert(0, "Não foi possível alterar o ID.")
                Log("customer_invalid_id").log_warning("Tentativa de usar ID de outro cliente ou ID indisponível.")
                return False

        return True

    def verify_if_edit_is_name(self, name):

        if not name:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'Nome' não pode estar vazio.")
            Log("customers_edit_not_name").log_warning(f"Tentativa de edição de cadastro de cliente sem nome.")
            
            return False
        
        else:
            return True
        
    def verify_if_edit_is_cpf(self, cpf):

        if not cpf:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'CPF' não pode estar vazio.")
            Log("customers_edit_not_cpf").log_warning(f"Tentativa de edição de cliente com CPF vazio.")
            
            return False
        
        else:
            return True
        
    def verify_if_edit_is_telephone(self, telephone):

        if not telephone:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'Telefone' não pode estar vazio.")
            Log("customers_edit_not_phone").log_warning(f"Tentativa de edição de cliente com telefone vazio.")
            return False
        
        else:
            return True
    
    def verify_if_edit_telephone_is_digit(self, telephone):

        if not telephone.isdigit():
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'Telefone' só pode conter números.")
            Log("customers_edit_phone_not_digit").log_warning(f"Tentativa de edição de cliente com telefone com algo que não seja números.")
            return False
        
        else:
            return True
        
    def verify_if_edit_cpf_is_digit(self, cpf):

        for char in cpf:
            if not (char.isdigit() or char in ".-"):
                self.console_text.delete(0, END)
                self.console_text.insert(0, "Campo 'CPF' só pode conter números, pontos e hífen.")
                Log("customers_edit_cpf_invalid_chars").log_warning("Tentativa de edição de cliente cujo CPF contém caracteres inválidos.")
                return False
        else:
            return True
        
    def verify_if_get_customer_is_name(self, name):

        if not name:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'Nome' não pode estar vazio.")
            Log("customers_not_name").log_warning(f"Tentativa de visualização de clientes com nome vazio.")
            return False
        else:
            return True
        
    def verify_if_create_product_is_name(self, name):

        if not name:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'Nome do Produto' não pode estar vazio.")
            Log("products_not_name").log_warning("Tentativa de cadastro de produto sem nome.")
            return False
        else:
            return True
        
    def verify_if_create_product_is_price(self, price):

        if not price:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'Preço' não pode estar vazio.")
            Log("products_not_price").log_warning("Tentativa de cadastro de produto sem preço.")
            return False
        else:
            return True
        
    def verify_if_create_product_is_stock(self, stock):

        if not stock:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'Estoque' não pode estar vazio.")
            Log("products_not_stock").log_warning("Tentativa de cadastro de produto sem quantidade em estoque.")
            return False
        else:
            return True
        
    def verify_if_create_product_price_is_digit(self, price):

        if not price.replace(',', '', 1).isdigit():
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'Preço' só pode conter números.")
            Log("products_not_digit").log_warning("Tentativa de cadastro de produto com preço não sendo numérico.")
            return False
        else:
            return True
        
    def verify_if_create_product_price_is_not_negative(self, price):

        price = price.replace(",",".")

        if float(price) <= 0:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'Preço' não pode conter 0 ou números negativos.")
            Log("products_not_digit").log_warning("Tentativa de cadastro de produto com preço sendo número negativo ou zero.")
            return False
        else:
            return True
        
    def verify_if_create_product_stock_is_digit(self, stock):

        if not stock.isdigit():
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'Estoque' só pode conter números maiores que zero.")
            Log("products_stock_not_digit").log_warning("Tentativa de cadastro de produto com quantidade em estoque não sendo numérica.")
            return False
        else:
            return True
        
    def verify_if_create_product_is_image(self, image):

        if not image:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "O produto precisa ter uma imagem.")
            Log("products_not_image").log_warning("Tentativa de cadastro de produto sem imagem.")
            return False
        else:
            return True
        
    def verify_if_update_stock_is_name(self, name):

        if not name:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'Nome do Produto' não pode estar vazio.")
            Log("product_stock_not_name").log_warning(f"Tentativa de atualização de estoque em produto sem nome.")
            return False
        else:
            return True
        
    def verify_if_update_stock_is_id(self, product_id):

        if not product_id:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'ID do Produto' não pode estar vazio.")
            Log("product_stock_not_id").log_warning(f"Tentativa de atualização de estoque em produto sem ID.")
            return False
        else:
            return True
        
    def verify_if_update_stock_is_amount(self, amount):

        if not amount:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'Quantidade' não pode estar vazio.")
            Log("product_stock_not_amount").log_warning(f"Tentativa de atualização de estoque em produto sem colocar a quantidade em estoque.")
            return False
        else:
            return True
        
    def verify_if_get_sale_is_sale_id(self, sale_id):

        if not sale_id:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Preencha o campo 'ID da Venda'.")
            Log("sales_get_success").log_warning(f"Tentativa de visualização de vendas sem ID de venda.")
            return False
        else:
            return True
        
    def verify_if_sell_is_product_name(self, product_name):

        if not product_name:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Preencha o campo 'Produto'.")
            Log("sale_not_product").log_warning(f"Tentativa de cadastro de venda sem nome do produto.")
            return False
        else:
            return True
        
    def verify_if_sell_is_customer_name(self, customer_name):

        if not customer_name:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Preencha o campo 'Nome do Cliente'.")
            Log("sale_not_customer").log_warning(f"Tentativa de cadastro de venda sem nome do cliente.")
            return False
        else:
            return True
        
    def verify_if_sell_is_cpf(self, cpf):

        if not cpf:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Preencha o campo 'CPF'.")
            Log("sale_not_cpf").log_warning(f"Tentativa de cadastro de venda sem CPF do cliente.")
            return False
        else:
            return True
        
    def verify_if_sell_amount_is_digit(self, amount):

        if not amount.isdigit():
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'Quantidade' só aceita números.")
            Log("sale_not_amount_digit").log_warning(f"Tentativa de cadastro de venda com quantidade não sendo número.")
            return False
        else:
            return True
        
    def verify_if_sell_amount_is_greater_than_zero(self, amount):

        if not int(amount) > 0:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'Quantidade' só aceita números maiores que zero.")
            Log("sale_not_amount_digit").log_warning(f"Tentativa de cadastro de venda com quantidade igual ou menor a zero.")
            return False
        else:
            return True
        
    def verify_if_sell_price_is_digit(self, price):

        if not price.replace(',', '', 1).isdigit():
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Coloque um preço válido para o produto.")
            Log("sale_not_price").log_warning(f"Tentativa de cadastro de venda sem preço válido.")
            return False
        else:
            return True
        
    def verify_if_sell_price_is_greater_than_zero(self, price):

        price = price.replace(",",".")
        price = float(price)

        if not float(price) > 0:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Campo 'Preço Unitário' não aceita zero ou números negativos como valor.")
            Log("sale_not_price").log_warning(f"Tentativa de cadastro de venda com preço igual ou menor que zero.")
            return False
        else:
            return True
        
    def verify_if_edit_sale_is_id(self, sale_id):

        if not sale_id:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Preencha o campo 'ID da Venda'.")
            Log("sale_edit_not_id").log_warning(f"Tentativa de edição de venda sem ID do produto.")
            return False
        else:
            return True
        
    def verify_if_edit_sale_is_product_name(self, product_name):

        if not product_name:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Preencha o campo 'Nome do Produto'.")
            Log("sale_edit_not_product").log_warning(f"Tentativa de edição de venda sem nome do produto.")
            return False
        else:
            return True
        
    def verify_if_edit_sale_is_customer_name(self, customer_name):

        if not customer_name:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Preencha o campo 'Nome do Cliente'.")
            Log("sale_edit_not_customer").log_warning(f"Tentativa de edição de venda sem nome do cliente.")
            return False
        else:
            return True
        
    def verify_if_edit_sale_is_cpf(self, cpf):

        if not cpf:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Preencha o campo 'CPF'.")
            Log("sale_edit_not_id").log_warning(f"Tentativa de edição de venda sem CPF do cliente.")
            return False
        else:
            return True
        
    def verify_if_edit_sale_is_new_amount(self, new_amount):

        if not new_amount:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Coloque um valor válido para a quantidade.")
            Log("sale_edit_not_amount").log_warning(f"Tentativa de edição de venda com quantidade inválida.")
            return False
        else:
            return True
        
    def verify_if_edit_sale_amount_is_greater_than_zero(self, new_amount):

        if int(new_amount) <= 0:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "'Quantidade' não pode ser menor ou igual a zero.")
            Log("sale_edit_not_amount").log_warning(f"Tentativa de edição de venda com quantidade menor ou igual a zero.")
            return False
        else:
            return True
        
    def verify_if_edit_sale_price_is_digit(self, price):

        if not price.replace(',', '', 1).isdigit():
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Coloque um preço válido para o produto.")
            Log("sale_edit_price_not_digit").log_warning(f"Tentativa de edição de venda com preço de produto não sendo número.")
            return False
        else:
            return True
        
    def verify_if_edit_sale_price_is_greater_than_zero(self, price):

        price = price.replace(",",".")
        price = float(price)

        if float(price) <= 0:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "'Preço Unitário' não poder ser menor ou igual a zero.")
            Log("sale_edit_price_not_digit").log_warning(f"Tentativa de edição de venda com preço de produto menor ou igual a zero.")
            return False
        else:
            return True
        
    def verify_edit_sale_quantities(self, result1, result2, new_amount, quantity_sold):

        old_product = result1[0][1]
        new_product = result2[0][1]

        if old_product == new_product:
            if new_amount > quantity_sold: # Se a nova quantidade vendida for maior que a quantidade vendida anteriormente, ele coloca a diferença na nova quantidade
                difference = new_amount - quantity_sold
                self.database.update("UPDATE Produtos SET Estoque = Estoque - ? WHERE Produto = ?", [difference, new_product])
            
            elif new_amount < quantity_sold: # Mas se a nova quantidade vendida for menor que a quantidade vendida anteriormente, ele cobre a diferença
                difference = quantity_sold - new_amount
                self.database.update("UPDATE Produtos SET Estoque = Estoque + ? WHERE Produto = ?", [difference, new_product])

        else:
            if new_amount > quantity_sold: # Se a nova quantidade vendida for maior que a quantidade vendida anteriormente, ele coloca a diferença na nova quantidade
                difference_new_product = new_amount
                difference_old_product = quantity_sold
                self.database.update("UPDATE Produtos SET Estoque = Estoque - ? WHERE Produto = ?", [difference_new_product, new_product])
                self.database.update("UPDATE Produtos SET Estoque = Estoque + ? WHERE Produto = ?", [difference_old_product, old_product])

            elif new_amount < quantity_sold: # Mas se a nova quantidade vendida for menor que a quantidade vendida anteriormente, ele cobre a diferença
                difference_new_product = new_amount
                difference_old_product = quantity_sold
                self.database.update("UPDATE Produtos SET Estoque = Estoque + ? WHERE Produto = ?", [difference_old_product, old_product])
                self.database.update("UPDATE Produtos SET Estoque = Estoque - ? WHERE Produto = ?", [difference_new_product, new_product])     
            
            elif new_amount == quantity_sold: # Se forem iguais, a quantidade vendida inicialmente é a que vale
                difference_new_product = quantity_sold
                difference_old_product = quantity_sold
                self.database.update("UPDATE Produtos SET Estoque = Estoque - ? WHERE Produto = ?", [difference_new_product, new_product])
                self.database.update("UPDATE Produtos SET Estoque = Estoque + ? WHERE Produto = ?", [difference_old_product, old_product])

    def verify_delete_sale_not_id(self, id_sale):

        if not id_sale:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Preencha o campo 'ID da Venda'.")
            Log("sale_delete_not_id").log_warning(f"Tentativa de deletar venda sem ID do produto.")
            return False
        else:
            return True