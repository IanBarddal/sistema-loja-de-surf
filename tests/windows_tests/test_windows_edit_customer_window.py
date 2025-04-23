import tkinter as tk
from windows.edit_customer_window import edit_customer_window

def test_edit_customer_ui_elements_exist():
    root = tk.Tk()
    root.withdraw()  # Não exibe a janela principal

    # Chama a função e captura o Frame retornado
    window1 = edit_customer_window(root)

    # Verifica diretamente os widgets
    entries = [
        window1.name_entry,
        window1.cpf_entry,
        window1.telephone_entry
    ]
    button = window1.ok_button
    console = window1.console_text

    print(f"Entries encontrados: {len(entries)}")
    print(f"Button texto: {button.cget('text')}")
    print(f"Console tipo: {type(console)}")

    # Asserções
    assert all(entry.winfo_exists() for entry in entries), "Nem todos os campos de entrada existem"
    assert button.cget("text") == "Editar", "Botão 'Editar' não encontrado"
    assert console.winfo_exists(), "Listbox (console_text) não encontrado"

    root.destroy()