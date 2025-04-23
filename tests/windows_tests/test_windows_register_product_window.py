import tkinter as tk
from windows.product_register_window import product_register_window

def test_register_product_ui_elements_exist():
    root = tk.Tk()
    root.withdraw()  # Não exibe a janela principal

    # Chama a função e captura o Frame retornado
    window1 = product_register_window(root)

    # Verifica diretamente os widgets
    entries = [
        window1.name_product_entry,
        window1.price_entry,
        window1.stock_entry
    ]
    button = window1.ok_button
    console = window1.console_text

    # Asserções
    assert all(entry.winfo_exists() for entry in entries), "Nem todos os campos de entrada existem"
    assert button.cget("text") == "Cadastrar", "Botão 'Cadastrar' não encontrado"
    assert console.winfo_exists(), "Listbox (console_text) não encontrado"

    root.destroy()