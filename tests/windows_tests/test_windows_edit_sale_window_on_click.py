import tkinter as tk
from windows.edit_sale_window import edit_sale_window_on_click
from modules.database import DataBase
from unittest import mock

@mock.patch("windows.sell_window.Canvas.create_image")
@mock.patch("windows.sell_window.ImageTk.PhotoImage")
@mock.patch("windows.sell_window.Image.open")
def test_edit_sale_on_click_ui_elements_exist(mock_open, mock_photoimage, mock_create_image):
    mock_open.return_value.resize.return_value = mock.Mock()
    mock_photoimage.return_value = mock.Mock()
    mock_create_image.return_value = None  # Evita o uso real da imagem no canvas

    root = tk.Tk()
    root.withdraw()

    database = DataBase(":memory:")
    database.create_database()
    database.create(
        "INSERT INTO Vendas ('ID', 'Cliente', 'CPF', 'Produto', 'Quantidade Vendida', 'Valor Total') VALUES (?, ?, ?, ?, ?, ?)",
        [1, "João da Silva", "555.555.555-55", "Prancha de Surf", 1, 2300.00]
    )
    result = database.read("SELECT * FROM Vendas WHERE ID = ?", [1])

    window1 = edit_sale_window_on_click(root, result)

    entries = [
        window1.sale_id_entry,
        window1.product_name_entry,
        window1.customer_name_entry,
        window1.cpf_entry,
        window1.new_amount_entry,
        window1.price_entry
    ]
    button = window1.ok_button
    console = window1.console_text

    assert all(entry.winfo_exists() for entry in entries)
    assert button.cget("text") == "Editar"
    assert console.winfo_exists()

    root.destroy()