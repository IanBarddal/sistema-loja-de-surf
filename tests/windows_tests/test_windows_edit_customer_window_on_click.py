import tkinter as tk
from windows.edit_customer_window import edit_customer_window_on_click
from modules.database import DataBase

def test_edit_customer_on_click_ui_elements_exist():
    root = tk.Tk()
    root.withdraw()  # Não exibe a janela principal

    database = DataBase(":memory:")
    database.create_database()

    database.create("INSERT INTO Clientes ('ID', 'Nome', 'CPF', 'Telefone') VALUES (?, ?, ?, ?)", [1, "João da Silva", "555.555.555-55", "48999999999"])

    result = database.read("SELECT * FROM Clientes WHERE ID = ?", [1])

    # Chama a função e captura o Frame retornado
    window1 = edit_customer_window_on_click(root, result)

    # Verifica diretamente os widgets
    entries = [
        window1.name_entry,
        window1.cpf_entry,
        window1.telephone_entry
    ]
    button = window1.ok_button
    console = window1.console_text

    # Asserções
    assert all(entry.winfo_exists() for entry in entries)
    assert button.cget("text") == "Editar"
    assert console.winfo_exists()

    root.destroy()