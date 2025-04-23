import tkinter as tk
from windows.sell_window import sell_window_on_click
from modules.database import DataBase
from unittest import mock

@mock.patch("windows.sell_window.Canvas.create_image")
@mock.patch("windows.sell_window.ImageTk.PhotoImage")
@mock.patch("windows.sell_window.Image.open")
def test_sell_on_click_ui_elements_exist(mock_open, mock_photoimage, mock_create_image):
    mock_open.return_value.resize.return_value = mock.Mock()
    mock_photoimage.return_value = mock.Mock()
    mock_create_image.return_value = None  # Evita o uso real da imagem no canvas

    root = tk.Tk()
    root.withdraw()

    database = DataBase(":memory:")
    database.create_database()
    database.create(
        "INSERT INTO Produtos ('ID', 'Produto', 'Preço Unitário', 'Estoque', 'Imagem') VALUES (?, ?, ?, ?, ?)",
        [1, "Prancha de Surf", 2300.00, 20, "teste.jpg"]
    )
    result = database.read("SELECT * FROM Produtos WHERE Produto = ?", ["Prancha de Surf"])

    window1 = sell_window_on_click(root, result)

    entries = [
        window1.product_name_entry,
        window1.customer_name_entry,
        window1.cpf_entry,
        window1.amount_entry,
        window1.price_entry
    ]
    button = window1.ok_button
    console = window1.console_text

    assert all(entry.winfo_exists() for entry in entries)
    assert button.cget("text") == "Efetuar Venda"
    assert console.winfo_exists()

    root.destroy()