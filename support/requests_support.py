from tkinter import END
from PIL import Image, ImageTk
from logs.log_class import Log
from support.verify import Verify

class Requests(Verify):

    def __init__(self, database, console_text, product_canvas=None):
        super().__init__(console_text)
        self.database = database
        self.product_canvas = product_canvas

    def request_verify_customer_name_taken(self, name_result):

        if name_result:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Cliente já cadastrado com esse nome.")
            Log("customers_name_taken").log_warning(f"Tentativa de cadastro de cliente com nome já em uso.")
            return False
        else:
            return True
        
    def request_verify_customer_cpf_taken(self, cpf_result):

        if cpf_result:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "CPF já cadastrado.")
            Log("customers_cpf_taken").log_warning(f"Tentativa de cadastro de cliente com CPF já em uso.")
            return False
        else:
            return True
        
    def request_verify_customer_telephone_taken(self, telephone_result):

        if telephone_result:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Telefone já cadastrado. Escolha outro.")
            Log("customers_phone_taken").log_warning(f"Tentativa de cadastro de cliente com telefone já em uso.")
            return False
        else:
            return True
        
    def request_verify_customer_get_customer(self, name_result, name):

        if not name_result:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Cliente não encontrado.")
            Log("customer_not_found").log_warning(f"Tentativa de visualização de cliente {name} falhou (cliente não encontrado).")
            return False
        else:
            self.console_text.delete(0, END)
            for customer in name_result:
                self.console_text.insert(0, f"ID do Cliente: {customer[0]} | Nome do Cliente: {customer[1]} | CPF: {customer[2]} | Telefone: {customer[3]} | Data de Adesão: {customer[4]}")
            Log("customer_get_success").log_info(f"Tentativa de visualização do cliente {name} bem sucedida.")
            return True

    def request_verify_customer_get_all_customers(self, result):

        if result:
            self.console_text.delete(0, END)
            for customer in result:
                self.console_text.insert(0, f"ID do Cliente: {customer[0]} | Nome do Cliente: {customer[1]} | CPF: {customer[2]} | Telefone: {customer[3]} | Data de Adesão: {customer[4]}\n\n")
            Log("customers_get_success").log_info(f"Tentativa de visualização de clientes bem sucedida.")
            return True
        else:
            
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Não há clientes cadastrados.")
            Log("customers_not_found").log_warning(f"Tentativa de visualização de clientes falhou (não há clientes cadastrados).")
            return False
    
    def request_verify_get_all_products_if_products_exist(self, result):

        if result:
            
            for product in result:
                formatted_value = f"R$ {product[2]:.2f}".replace(".", ",")
                self.console_text.insert(0, f"ID do Produto: {product[0]} | Nome do Produto: {product[1]} | Preço Unitário: {formatted_value} | Quantidade em Estoque: {product[3]} | Data de Adição: {product[4]}\n\n")
                
            Log("products_found").log_info("Tentativa de visualização de produtos bem sucedida.")
            
            return True
        else:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Não há produtos cadastrados.")
            Log("products_not_found").log_warning("Não há produtos cadastrados.")

            return False
        
    def request_verify_if_create_product_name_taken(self, product_name_result):

        if product_name_result:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Produto já existe com esse nome.")
            Log("products_name_taken").log_warning("Tentativa de cadastro de produto cujo nome já existe.")
            return False
        else:
            return True
    
    def request_verify_if_delete_product_product_exists(self, result, name):

        if result:
            self.database.delete("DELETE FROM Produtos WHERE Produto = ?", [name])
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Produto deletado com sucesso.")
            Log("product_deleted").log_info(f"Produto {name} deletado com sucesso.")
            return True
        else:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Produto não encontrado.")
            Log("product_not_found").log_warning(f"Tentativa de visualização de produto {name} falhou (produto não encontrado)")
            return False

    def request_verify_if_get_product_product_exists(self, result, name):

        if result:
            self.console_text.delete(0, END)
            for product in result:
                formatted_value = f"R$ {product[2]:.2f}".replace(".", ",")
                self.console_text.insert(0, f"ID do Produto: {product[0]} | Nome do Produto: {product[1]} | Preço Unitário: {formatted_value} | Quantidade em Estoque: {product[3]} | Data de Adição: {product[4]}\n\n")     
                Log("product_found").log_info(f"Produto {name} procurado e encontrado.")
                
                for product in result:
                    self.product_canvas.place(x=800, y=100)
                    product_image = Image.open(f"images/{product[5]}")  # Coluna 5 deve ser o nome do arquivo
                    product_image = product_image.resize((200, 300))
                    product_image_tk = ImageTk.PhotoImage(product_image)

                    self.product_canvas.create_image(0, 0, image=product_image_tk, anchor="nw")
                    self.product_canvas.image = product_image_tk  # Evita que a imagem seja deletada pelo Garbage Collector

                    return True

        else:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Produto não encontrado.")
            Log("product_not_found").log_warning(f"Produto {name} procurado e não encontrado.")
            
            return False
        
    def request_verify_if_update_stock_is_product(self, result):

        if len(result) == 0:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Produto não encontrado.")
            Log("product_stock_not_found").log_warning(f"Tentativa de encontrar produto falhada.")
            return False
        
    def request_verify_if_update_stock_is_id(self, id_result, name, amount):

        if id_result == [] or name not in id_result[0][1]:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Produto não casa com o ID.")
            Log("product_stock_mismatch").log_warning(f"Tentativa de atualização de estoque em produto cujo ID e nome não casam.")
            return False
        
        else:
            self.database.update("UPDATE Produtos SET Estoque = Estoque + ? WHERE Produto = ?", [amount, name])
        
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Estoque atualizado com sucesso.")
            Log("product_stock_registered").log_info(f"Tentativa de atualização de estoque bem-sucedida: {name}, estoque: {amount}.")
            return True
        
    def request_verify_get_all_sales(self, result):

        if result:
            self.console_text.delete(0, END)
            
            for sale in result:
                formatted_value = f"R$ {sale[5]:.2f}".replace(".", ",")
                self.console_text.insert(0, f"ID da Venda: {sale[0]} | Cliente: {sale[1]} | CPF: {sale[2]} | Produto: {sale[3]} | Quantidade Vendida: {sale[4]} | Valor Total: {formatted_value} | Data da Venda: {sale[6]}\n\n")
            
            Log("sales_get_success").log_info(f"Tentativa de visualização de vendas bem sucedida.")

            return True
        else:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Não há vendas cadastradas.")
            Log("sales_not_found").log_warning(f"Tentativa de visualização de vendas falhou (não há vendas cadastradas).")
            return False
        
    def request_verify_get_sale(self, result, sale_id):

        if result:
            self.console_text.delete(0, END)
            for sale in result:
                formatted_value = f"R$ {sale[5]:.2f}".replace(".", ",")
                self.console_text.insert(0, f"ID da Venda: {sale[0]} | Cliente: {sale[1]} | CPF: {sale[2]} | Produto: {sale[3]} | Quantidade Vendida: {sale[4]} | Valor Total: {formatted_value} | Data da Venda: {sale[6]}")
                
                Log("sale_get_success").log_info(f"Tentativa de visualização de venda número {sale_id} bem sucedida.")

                products = self.database.read("SELECT * FROM Produtos WHERE Produto = ?", [sale[3]])

                for product in products:
                    self.product_canvas.place(x=800, y=100)
                    product_image = Image.open(f"images/{product[5]}")
                    product_image = product_image.resize((200, 300))
                    self.product_image_tk = ImageTk.PhotoImage(product_image)

                    self.product_canvas.create_image(0, 0, image=self.product_image_tk, anchor="nw")
                    self.product_canvas.image = self.product_image_tk  # Garante que o GC não apague a imagem

                    return True
        else:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Venda não encontrada.")
            Log("sale_not_found").log_warning(f"Tentativa de visualização de venda falhou (venda não encontrada).")
            return False

    def request_verify_if_sell_is_product(self, product_name_result):

        if not product_name_result:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Produto inexistente.")
            Log("sale_not_product_found").log_warning(f"Tentativa de cadastro de venda de produto inexistente.")
            return False
        else:
            return True
        
    def request_verify_if_sell_is_stock(self, product_name_result, amount):

        for product in product_name_result:
            if amount > product[3]:
                self.console_text.delete(0, END)
                self.console_text.insert(0, f"Produto não tem estoque disponível.")
                Log("sale_stock_unavailable").log_warning(f"Tentativa de cadastro de venda de produto com falta em estoque.")
                return False
            else:
                return True
            
    def request_verify_if_sell_is_customer(self, customer_result):

        if not customer_result:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Cliente não cadastrado.")
            Log("sale_not_customer_available").log_warning(f"Tentativa de cadastro de venda com cliente não cadastrado.")
            return False
        else:
            return True
        
    def request_verify_if_sell_is_cpf(self, customer_result, customer_name, cpf):

        for customer in customer_result:
            if customer[1] == customer_name:
                if customer[2] != cpf:
                    self.console_text.delete(0, END)
                    self.console_text.insert(0, "CPF não bate com o do cliente.")
                    Log("sale_cpf_mismatch").log_warning(f"Tentativa de cadastro de venda com CPF e cliente não casando.")
                    return False
                else:
                    return True

    def request_verify_if_edit_sale_is_customer(self, customer_result):

        if not customer_result:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Cliente não cadastrado.")
            Log("sale_edit_not_customer").log_warning(f"Tentativa de edição de venda sem cliente cadastrado.")
            return False
        else:
            return True
        
    def request_verify_if_edit_sale_cpf_match(self, customer_result, customer_name, cpf):

        for customer in customer_result:
            if customer[1] == customer_name:
                if customer[2] != cpf :
                    self.console_text.delete(0, END)
                    self.console_text.insert(0, "CPF não bate com o do cliente.")
                    Log("sale_edit_cpf_mismatch").log_warning(f"Tentativa de edição de venda onde CPF e nome do cliente não casam.")
                    return False
                else:
                    return True

    def request_verify_if_edit_sale_product_exists(self, product_result):

        if not product_result:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Produto inexistente.")
            Log("sale_edit_product_not_found").log_warning(f"Tentativa de edição de venda com produto inexistente.")
            return False
        else:
            return True
        
    def request_verify_if_edit_sale_stock_support(self, product_result, new_amount):

        for product in product_result:
            if new_amount > product[3]:
                self.console_text.delete(0, END)
                self.console_text.insert(0, "Venda não comporta estoque.")
                Log("sale_edit_stock_unavailable").log_warning(f"Tentativa de edição de venda com produto sem estoque.")
                return False
            else:
                return True
            
    def request_verify_if_edit_sale_id_exists(self, id_result):

        if not id_result: #Primeiro, verifica se a venda existe
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Venda não encontrada.")
            Log("sale_edit_not_found").log_warning(f"Tentativa de edição de venda (venda não foi não encontrada.)")
            return
        else:
            return True

    def request_verify_if_delete_sale_is_sale_id(self, result, sale_id):

        if not result:
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Venda não encontrada.")
            Log("sale_delete_not_found").log_warning(f"Tentativa de deletar uma venda não encontrada.")

            return False
        else:
            self.database.delete("DELETE FROM Vendas WHERE ID = ?", [sale_id])

            for sale in result:
                quantity = sale[4]
                produto = sale[3]

            self.database.update("UPDATE Produtos SET Estoque = Estoque + ? WHERE Produto = ?", [quantity, produto])
            Log("sale_stock_update_success").log_info(f"Tentativa de atualização de estoque bem-sucedida: {produto}, {quantity} unidades devolvidas ao estoque.")

            return True