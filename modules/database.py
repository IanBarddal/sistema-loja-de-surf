import sqlite3
from contextlib import closing
import os
from tkinter import messagebox
from logs.log_class import Log

class DataBase():

    connection = None

    # Abaixo, os comandos para criação do banco de dados

    def __init__ (self, db_name="surfstore.db", auto_connect=True):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)

        if not auto_connect:
            self.connect()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_connection()

    def create_database(self): # Cria o banco de dados, mas apenas se ele não existir

        database =  '''
                CREATE TABLE IF NOT EXISTS Produtos
                ("ID" integer primary key autoincrement, 'Produto' text, 'Preço Unitário' real, 'Estoque' integer, 'Data de Adição' text, 'Imagem' text);

                CREATE TABLE IF NOT EXISTS Clientes
                ("ID" integer primary key autoincrement, 'Nome' text, 'CPF' text, 'Telefone' text, 'Data de Adesão' text);

                CREATE TABLE IF NOT EXISTS Vendas
                ("ID" integer primary key autoincrement, 'Cliente' text, 'CPF' text, 'Produto' text, 'Quantidade Vendida' integer, 'Valor Total' real, 'Data da Venda' text);
                '''
        
        if not os.path.isfile(self.db_name):
            messagebox.showinfo(title="Banco de Dados", message="Criando banco de dados...")
            Log("database_creating").log_info(f"Tentativa de criar banco de dados.")

            with closing(self.connection.cursor()) as cursor:
                cursor.executescript(database)
        else:
            messagebox.showinfo(title="Banco de Dados", message=f"Carregando banco de dados...")
            Log("database_loading").log_info(f"Tentativa de carregar banco de dados.")

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            Log("database_connect").log_info("Tentativa de conexão com o banco de dados bem sucedida.")
            return self.connection
        except sqlite3.Error as error:
            Log("database_connect").log_warning(f"Erro ao conectar com o banco de dados: {error}")
            return None
    
    def close_connection(self):
        
        try:
            if self.connection:
                
                self.connection.commit()
                self.connection.close()
                self.connection = None
                
                Log("database_close_connection").log_info(f"Tentativa de fechamento de conexão com o banco de dados bem sucedida.")

        except Exception as exception:
            Log("database_close_connection_failure").log_warning(f"Tentativa de fechamento de conexão com o banco de dados falhou. Motivo: {exception}")
        
    def create(self, command, parameters):
        
        with closing(self.connection.cursor()) as cursor:
            cursor.execute(command, parameters)
            Log("database_create_info").log_info(f"Tentativa de CREATE no banco de dados bem sucedida.")
        self.connection.commit()
            
    def read(self, command, parameters=()):
    
        with closing(self.connection.cursor()) as cursor:
            cursor.execute(command, parameters)
            Log("database_read_info").log_info(f"Tentativa de READ no banco de dados bem sucedida.")

            return cursor.fetchall()
            
    def update(self, command, parameters):
        
        with closing(self.connection.cursor()) as cursor:
            cursor.execute(command, parameters)
            Log("database_update_info").log_info(f"Tentativa de UPDATE no banco de dados bem sucedida.")
        self.connection.commit()

    def delete(self, command, parameters):
        
        with closing(self.connection.cursor()) as cursor:
            cursor.execute(command, parameters)
            Log("database_delete_info").log_info(f"Tentativa de DELETE no banco de dados bem sucedida.")
        self.connection.commit()