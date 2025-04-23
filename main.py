from windows.main_window import main_window
from modules.database import DataBase

database = DataBase()
database.create_database() # Cria o banco de dados

main_window() # Chama a janela principal