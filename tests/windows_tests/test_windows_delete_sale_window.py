import tkinter as tk
from windows.delete_sale_window import delete_sale_window

def test_delete_sale_ui_elements_exist():
    root = tk.Tk()
    root.withdraw()  # Não exibe a janela principal

    # Chama a função e captura o Frame retornado
    window1 = delete_sale_window(root)

    # Verifica diretamente os widgets
    entries = window1.sale_id_entry
    buttons = window1.ok_button
    console = window1.console_text

    # Asserções
    assert entries.winfo_exists()
    assert buttons.cget("text") == "Cancelar"
    assert console.winfo_exists()

    root.destroy()