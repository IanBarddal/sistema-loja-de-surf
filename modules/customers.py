from tkinter import END
from datetime import datetime
from modules.database import DataBase
from logs.log_class import Log
from support.verify import Verify
from support.requests_support import Requests

date_now = datetime.now()
date_formatted = date_now.strftime("%d/%m/%Y %H:%M")

class Customer():
    
    def __init__ (self, id_entry, name_entry, cpf_entry, telephone_entry, console_text, database=None): # Cria o construtor da classe "Cliente"
        self.customer_id = id_entry
        self.name_entry = name_entry 
        self.cpf_entry = cpf_entry
        self.telephone_entry = telephone_entry
        self.console_text = console_text
        self.database = database or DataBase() # Separação necessária para os testes

    def register_customer(self): # Função para registrar cliente

        # Pega todos os campos
        name = self.name_entry.get() 
        cpf = self.cpf_entry.get()
        cpf = str(cpf)
        telephone = self.telephone_entry.get()
        telephone = str(telephone)

        # Confere se os campos estão preenchidos

        if not Verify(self.console_text).verify_if_is_name(name):
            return

        if not Verify(self.console_text).verify_if_is_cpf(cpf):
            return
        
        if not Verify(self.console_text).verify_if_is_telephone(telephone):
            return
        
        if not Verify(self.console_text).verify_if_cpf_is_digit(cpf):
            return
        
        if not Verify(self.console_text).verify_if_telephone_is_digit(telephone):
            return
    
        # Chama a conexão ao banco de dados
        
        name_request = self.database.read("SELECT * FROM Clientes WHERE Nome = ?", [name])
        cpf_request = self.database.read("SELECT * FROM Clientes WHERE CPF = ?", [cpf])
        telephone_request = self.database.read("SELECT * FROM Clientes WHERE Telefone = ?", [telephone])

        requests_group = Requests(self.database, self.console_text)

        # Faz as verificações necessárias com base nas requisições ao banco de dados

        customer_name_request_result = requests_group.request_verify_customer_name_taken(name_request)
        customer_cpf_request_result = requests_group.request_verify_customer_cpf_taken(cpf_request)
        customer_telephone_request_result = requests_group.request_verify_customer_telephone_taken(telephone_request)

        if not customer_name_request_result or not customer_cpf_request_result or not customer_telephone_request_result:
            return # Se não atender aos requisitos das verificações, pára a função
        else: # Caso contrário, continua o fluxo da execução da função
            if len(telephone) == 11: # Verifica se é um telefone fixo ou celular
                telephone = f"({telephone[:2]}) {telephone[2:7]}-{telephone[7:]}"
            if len(telephone) == 10:
                telephone = f"({telephone[:2]}) {telephone[2:6]}-{telephone[6:]}"
            # Faz o comando de criar um novo registro no banco de dados
            self.database.create("INSERT INTO Clientes ('Nome', 'CPF', 'Telefone', 'Data de Adesão') VALUES (?, ?, ?, ?)", [name, cpf, telephone, date_formatted])
            # Informa as alterações no console
            self.console_text.delete(0, END)
            self.console_text.insert(0, "Cliente cadastrado com sucesso.")
            Log("customer_registered").log_info(f"Tentativa de cadastro de cliente feita com sucesso.")

            return name, cpf, telephone, date_formatted

    def edit_customer(self):

        # Pega todos os campos
        customer_id = self.customer_id.get()
        name = self.name_entry.get() 
        cpf = self.cpf_entry.get()
        cpf = str(cpf)
        telephone = self.telephone_entry.get()
        telephone = str(telephone)

        if not Verify(self.console_text).verify_if_edit_is_id(customer_id):
            return
        
        if not Verify(self.console_text).verify_if_id_changes(customer_id, name):
            return

        if not Verify(self.console_text).verify_if_edit_is_name(name):
            return
        
        if not Verify(self.console_text).verify_if_edit_is_cpf(cpf):
            return
        
        if not Verify(self.console_text).verify_if_edit_is_telephone(telephone):
            return

        if not Verify(self.console_text).verify_if_edit_telephone_is_digit(telephone):
            return

        if len(telephone) == 11:
            telephone = f"({telephone[:2]}) {telephone[2:7]}-{telephone[7:]}"
        if len(telephone) == 10:
            telephone = f"({telephone[:2]}) {telephone[2:6]}-{telephone[6:]}"
        
        # Confere se o CPF só contém números:

        if not Verify(self.console_text).verify_if_edit_cpf_is_digit(cpf):
            return

        # Faz a requisição

        update = self.database.update("UPDATE Clientes SET Nome = ?, CPF = ?, Telefone = ? WHERE ID = ?", [name, cpf, telephone, customer_id])

        # Imprime na tela os resultados
        self.console_text.delete(0, END)
        self.console_text.insert(0, "Cliente atualizado com sucesso.")
        Log("customers_edit_success").log_info(f"Tentativa de edição de cliente feita com sucesso.")

        return update
    
    def get_customer(self):
        # Cria a entrada para o nome do cliente
        name = self.name_entry.get()

        if not Verify(self.console_text).verify_if_get_customer_is_name(name): # Se o campo "nome" não for preenchido, emite um aviso no console
            return
        # Faz uma requisição ao banco de dados para encontrar os clientes
        name_request = self.database.read("SELECT * FROM Clientes WHERE Nome = ?", [name])
        # Faz as verificações necessárias (se o cliente foi ou não encontrado)
        request_result = Requests(self.database, self.console_text).request_verify_customer_get_customer(name_request, name)
        # Retorna o resultado
        return request_result

    def get_all_customers(self):
        # Faz uma requisição ao banco de dados
        id_request = self.database.read("SELECT * FROM Clientes ORDER BY ID DESC")
        # Faz as verificações necessárias
        request_result = Requests(self.database, self.console_text).request_verify_customer_get_all_customers(id_request)
        # Retorna o resultado da requisição
        return request_result