import tkinter as tk
from windows.update_stock_window import update_stock_window

def test_update_stock_ui_elements_exist():
    root = tk.Tk()
    root.withdraw()  # Não exibe a janela principal

    # Chama a função e captura o Frame retornado
    window1 = update_stock_window(root)

    # Verifica diretamente os widgets
    entries = [
        window1.name_product_entry,
        window1.id_entry,
        window1.amount_entry
    ]
    button = window1.ok_button
    console = window1.console_text

    # Asserções
    assert all(entry.winfo_exists() for entry in entries)
    assert button.cget("text") == "Atualizar"
    assert console.winfo_exists()

    root.destroy()