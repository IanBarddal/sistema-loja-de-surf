import pytest
import tkinter as tk
from windows.main_window import main_window
import inspect

@pytest.fixture
def app():
    # Cria a janela principal em modo de teste
    window = tk.Tk()
    window.withdraw()  # Evita mostrar a janela na tela
    return window

def test_buttons_exist_and_trigger(app):
    # Cria a janela de forma isolada para testes
    from windows.customer_register_window import register_customer_window
    from windows.edit_customer_window import edit_customer_window
    from windows.view_customers_window import view_customers_window
    from windows.product_register_window import product_register_window
    from windows.delete_product_window import delete_product_window
    from windows.view_products_window import view_products_window
    from windows.update_stock_window import update_stock_window
    from windows.sell_window import sell_window
    from windows.view_sales_window import view_sales_window
    from windows.edit_sale_window import edit_sale_window
    from windows.delete_sale_window import delete_sale_window
    from modules.print_report import print_report

    # Lista de botões com suas funções
    buttons = [
        ("Registrar Cliente", register_customer_window),
        ("Editar Cliente", edit_customer_window),
        ("Pesquisar Cliente", view_customers_window),
        ("Cadastrar Produto", product_register_window),
        ("Deletar Produto", delete_product_window),
        ("Pesquisar Produtos", view_products_window),
        ("Atualizar Estoque", update_stock_window),
        ("Efetuar Venda", sell_window),
        ("Pesquisar Vendas", view_sales_window),
        ("Editar Venda", edit_sale_window),
        ("Cancelar Venda", delete_sale_window),
        ("Imprimir Relatório", print_report),
    ]

    for name, func in buttons:
        try:
            sig = inspect.signature(func)
            if len(sig.parameters) == 1:
                func(app)  # Chama a função associada ao botão
            else:
                func()
        except Exception as e:
            pytest.fail(f"Botão '{name}' falhou ao abrir a janela: {e}")