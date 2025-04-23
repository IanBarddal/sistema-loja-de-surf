import tkinter as tk
from windows.view_sales_window import view_sales_window

def test_get_sales_ui_elements_exist():
    root = tk.Tk()
    root.withdraw()  # Não exibe a janela principal

    # Chama a função e captura o Frame retornado
    window1 = view_sales_window(root)

    # Verifica diretamente os widgets
    entries = window1.sale_id_entry
    buttons = [window1.ok_button, window1.all_sales_button]
    console = window1.console_text

    # Asserções
    assert entries.winfo_exists()
    assert buttons[0].cget("text") == "Visualizar"
    assert buttons[1].cget("text") == "Visualizar Todas as Vendas"
    assert console.winfo_exists()

    root.destroy()