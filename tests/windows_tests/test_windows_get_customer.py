import tkinter as tk
from windows.view_customers_window import view_customers_window

def test_get_customers_ui_elements_exist():
    root = tk.Tk()
    root.withdraw()  # Não exibe a janela principal

    # Chama a função e captura o Frame retornado
    window1 = view_customers_window(root)

    # Verifica diretamente os widgets
    entries = window1.name_entry
    buttons = [window1.ok_button, window1.ok_button_2]
    console = window1.console_text

    # Asserções
    assert entries.winfo_exists()
    assert buttons[0].cget("text") == "Pesquisar"
    assert buttons[1].cget("text") == "Pesquisar Todos os Clientes"
    assert console.winfo_exists()

    root.destroy()