import tkinter as tk
from windows.view_products_window import view_products_window

def test_get_products_ui_elements_exist():
    root = tk.Tk()
    root.withdraw()  # Não exibe a janela principal

    # Chama a função e captura o Frame retornado
    window1 = view_products_window(root)

    # Verifica diretamente os widgets
    entries = window1.name_product_entry
    buttons = [window1.ok_button, window1.all_products_button]
    console = window1.console_text

    # Asserções
    assert entries.winfo_exists()
    assert buttons[0].cget("text") == "Visualizar Produtos"
    assert buttons[1].cget("text") == "Visualizar Todos os Produtos"
    assert console.winfo_exists()

    root.destroy()