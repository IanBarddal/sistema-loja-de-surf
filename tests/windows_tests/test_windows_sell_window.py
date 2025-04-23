import tkinter as tk
from windows.sell_window import sell_window

def test_sales_sell_ui_elements_exist():
    root = tk.Tk()
    root.withdraw()  # Não exibe a janela principal

    # Chama a função e captura o Frame retornado
    window1 = sell_window(root)

    # Verifica diretamente os widgets
    entries = [
        window1.product_name_entry,
        window1.customer_name_entry,
        window1.cpf_entry,
        window1.amount_entry,
        window1.price_entry
    ]
    button = window1.ok_button
    console = window1.console_text

    # Asserções
    assert all(entry.winfo_exists() for entry in entries)
    assert button.cget("text") == "Efetuar Venda"
    assert console.winfo_exists()

    root.destroy()